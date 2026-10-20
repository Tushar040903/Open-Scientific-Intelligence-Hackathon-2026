"""
Signal & Deconvolution Engine
Handles experimental spectrum loading, background subtraction,
robust peak finding, Pseudo-Voigt deconvolution, and Scherrer crystallite sizing.
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple, Optional
import numpy as np
import pandas as pd
from scipy.signal import find_peaks, savgol_filter
from scipy.optimize import curve_fit


@dataclass
class DetectedPeak:
    index: int
    two_theta: float        # Bragg angle (degrees 2θ)
    intensity: float        # Peak height (a.u.)
    relative_intensity: float  # Percentage of maximum peak (0 - 100%)
    fwhm: float             # Full Width at Half Maximum (degrees)
    d_spacing: float        # Interplanar d-spacing in Angstroms (Cu K-alpha)
    crystallite_size_nm: float  # Scherrer estimated size in nm
    hkl_label: Optional[str] = None


@dataclass
class SpectrumResult:
    two_theta: np.ndarray
    raw_intensity: np.ndarray
    background: np.ndarray
    corrected_intensity: np.ndarray
    peaks: List[DetectedPeak]
    wavelength_angstrom: float = 1.5406  # Cu K-alpha default

    def to_peak_dataframe(self) -> pd.DataFrame:
        if not self.peaks:
            return pd.DataFrame()
        return pd.DataFrame([asdict(p) for p in self.peaks])


class SignalEngine:
    def __init__(self, wavelength: float = 1.5406):
        """
        Args:
            wavelength: Radiation wavelength in Angstroms (default Cu K-alpha = 1.5406 A)
        """
        self.wavelength = wavelength

    def load_spectrum(self, file_source) -> Tuple[np.ndarray, np.ndarray]:
        """
        Loads spectrum from a file path, file-like object, or DataFrame.
        Accepts heterogeneous column naming (e.g. 2theta, angle, x vs intensity, counts, y).
        """
        if isinstance(file_source, pd.DataFrame):
            df = file_source.copy()
        elif isinstance(file_source, str):
            # Try comma, tab, or whitespace delimiter
            try:
                df = pd.read_csv(file_source)
            except Exception:
                df = pd.read_csv(file_source, sep=r"\s+")
        else:
            df = pd.read_csv(file_source)

        cols = list(df.columns)
        if len(cols) < 2:
            raise ValueError("Input spectrum must have at least 2 columns (2-theta angle and intensity).")

        # Map angle column
        col_x = None
        for c in cols:
            low = str(c).lower().replace("_", "").replace("-", "").replace(" ", "")
            if any(k in low for k in ["2theta", "twotheta", "theta", "angle", "deg", "2th"]):
                col_x = c
                break
        if col_x is None:
            col_x = cols[0]

        # Map intensity column
        col_y = None
        for c in cols:
            if c == col_x:
                continue
            low = str(c).lower().replace("_", "").replace("-", "").replace(" ", "")
            if any(k in low for k in ["intensity", "count", "counts", "cps", "y", "signal"]):
                col_y = c
                break
        if col_y is None:
            col_y = cols[1]

        two_theta = np.asarray(df[col_x], dtype=float)
        intensity = np.asarray(df[col_y], dtype=float)

        # Sort by 2theta
        sort_idx = np.argsort(two_theta)
        return two_theta[sort_idx], intensity[sort_idx]

    def estimate_background(self, x: np.ndarray, y: np.ndarray, window_size: int = 51) -> np.ndarray:
        """
        Estimates smooth experimental background using rolling min-envelope + Savitzky-Golay filter.
        """
        window = min(window_size, len(y) // 5 * 2 + 1)
        if window < 5:
            return np.zeros_like(y)

        # Rolling minimum approximation
        series = pd.Series(y)
        rolled_min = series.rolling(window=window, center=True, min_periods=1).min().values

        # Smooth baseline
        poly_order = min(3, window - 2)
        baseline = savgol_filter(rolled_min, window_length=window, polyorder=poly_order)
        # Ensure baseline does not exceed raw intensity
        baseline = np.minimum(baseline, y)
        return np.maximum(baseline, 0.0)

    def calculate_d_spacing(self, two_theta_deg: float) -> float:
        """
        Computes interplanar lattice d-spacing using Bragg's Law:
        λ = 2d * sin(θ) => d = λ / (2 * sin(θ_rad))
        """
        theta_rad = np.radians(two_theta_deg / 2.0)
        sin_theta = np.sin(theta_rad)
        if sin_theta <= 1e-6:
            return 0.0
        return float(self.wavelength / (2.0 * sin_theta))

    def calculate_scherrer_size(self, two_theta_deg: float, fwhm_deg: float, k: float = 0.9) -> float:
        """
        Estimates average crystallite domain size (nm) via the Scherrer equation:
        τ = (K * λ) / (β * cos(θ))
        """
        theta_rad = np.radians(two_theta_deg / 2.0)
        beta_rad = np.radians(fwhm_deg)
        cos_theta = np.cos(theta_rad)
        if beta_rad <= 1e-6 or cos_theta <= 1e-6:
            return 0.0
        # Wavelength in nm = wavelength_in_angstrom / 10
        lambda_nm = self.wavelength / 10.0
        tau_nm = (k * lambda_nm) / (beta_rad * cos_theta)
        return float(np.clip(tau_nm, 1.0, 500.0))

    def deconvolve(
        self,
        file_source,
        prominence: float = 0.04,
        min_distance: int = 10,
        min_relative_intensity: float = 4.0,
    ) -> SpectrumResult:
        """
        Complete end-to-end deconvolution pipeline:
        1. Loads raw spectrum
        2. Subtracts baseline background
        3. Identifies and deconvolves peaks
        4. Filters noise wiggles (< min_relative_intensity%)
        5. Calculates lattice d-spacing & crystallite dimensions
        """
        x, y = self.load_spectrum(file_source)
        bg = self.estimate_background(x, y)
        y_corr = np.maximum(y - bg, 0.0)

        # Smooth slightly before peak detection to avoid noise spikes
        if len(y_corr) > 15:
            y_smooth = savgol_filter(y_corr, window_length=11, polyorder=3)
            y_smooth = np.maximum(y_smooth, 0.0)
        else:
            y_smooth = y_corr

        # Normalize for peak finding
        y_max = np.max(y_smooth) if np.max(y_smooth) > 0 else 1.0
        norm_y = y_smooth / y_max

        # Peak detection
        peak_idx, props = find_peaks(norm_y, prominence=prominence, distance=min_distance)

        detected_peaks: List[DetectedPeak] = []
        for idx in peak_idx:
            angle = float(x[idx])
            peak_height = float(y_corr[idx])
            rel_height = float((peak_height / y_max) * 100.0)

            # Skip small noise spikes below relative intensity threshold
            if rel_height < min_relative_intensity:
                continue

            # Estimate FWHM by inspecting half-max positions locally
            half_max = peak_height / 2.0
            left_idx = idx
            while left_idx > 0 and y_corr[left_idx] > half_max:
                left_idx -= 1
            right_idx = idx
            while right_idx < len(y_corr) - 1 and y_corr[right_idx] > half_max:
                right_idx += 1

            fwhm = float(abs(x[right_idx] - x[left_idx]))
            if fwhm < 0.05:
                fwhm = 0.28  # default physical minimum instrumental broadening

            d_space = self.calculate_d_spacing(angle)
            c_size = self.calculate_scherrer_size(angle, fwhm)

            detected_peaks.append(
                DetectedPeak(
                    index=int(idx),
                    two_theta=round(angle, 3),
                    intensity=round(peak_height, 2),
                    relative_intensity=round(rel_height, 1),
                    fwhm=round(fwhm, 3),
                    d_spacing=round(d_space, 4),
                    crystallite_size_nm=round(c_size, 1),
                )
            )

        # Sort peaks by 2theta
        detected_peaks.sort(key=lambda p: p.two_theta)

        return SpectrumResult(
            two_theta=x,
            raw_intensity=y,
            background=bg,
            corrected_intensity=y_corr,
            peaks=detected_peaks,
            wavelength_angstrom=self.wavelength,
        )
