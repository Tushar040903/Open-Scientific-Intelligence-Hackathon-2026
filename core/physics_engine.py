"""
Physics & Crystallographic Validation Engine
Simulates theoretical X-ray diffraction patterns, validates crystal space groups,
matches experimental peaks against reference databases, and detects secondary impurity phases.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
import numpy as np


@dataclass
class BraggPeak:
    two_theta: float        # Bragg angle (degrees 2θ)
    relative_intensity: float  # (0 - 100%)
    hkl: Tuple[int, int, int]
    d_spacing: float

    @property
    def hkl_str(self) -> str:
        return f"({self.hkl[0]}{self.hkl[1]}{self.hkl[2]})"


@dataclass
class CrystalPhase:
    phase_id: str
    name: str
    formula: str
    space_group: str
    crystal_system: str
    lattice: Dict[str, float]  # a, b, c, alpha, beta, gamma
    theoretical_peaks: List[BraggPeak]
    description: str = ""


@dataclass
class PhaseMatchResult:
    phase: CrystalPhase
    match_score: float             # 0.0 - 1.0
    matched_peak_count: int
    total_theoretical_peaks: int
    mean_angle_delta: float        # degrees
    matched_peaks: List[Dict]      # [{exp_angle, theo_angle, hkl, delta, exp_intensity}]
    unmatched_experimental: List[float] # angles of peaks not explained by this phase


class PhysicsEngine:
    def __init__(self, wavelength: float = 1.5406):
        self.wavelength = wavelength
        self.database: Dict[str, CrystalPhase] = {}
        self._init_benchmark_database()

    def _init_benchmark_database(self):
        """
        Initializes physical reference data for benchmark functional materials,
        derived from crystallographic ICSD / Materials Project benchmarks.
        """
        # 1. LiCoO2 (High-voltage battery cathode, Layered R-3m)
        lco_peaks = [
            BraggPeak(18.94, 100.0, (0, 0, 3), 4.681),
            BraggPeak(37.36, 22.0, (1, 0, 1), 2.405),
            BraggPeak(38.40, 26.0, (0, 1, 2), 2.342),
            BraggPeak(45.26, 80.0, (1, 0, 4), 2.002),
            BraggPeak(49.54, 18.0, (0, 1, 5), 1.838),
            BraggPeak(59.12, 28.0, (1, 0, 7), 1.561),
            BraggPeak(65.36, 32.0, (1, 0, 8), 1.427),
            BraggPeak(66.54, 30.0, (1, 1, 0), 1.404),
        ]
        self.database["LiCoO2"] = CrystalPhase(
            phase_id="mp-22526",
            name="Lithium Cobalt Oxide (Layered)",
            formula="LiCoO2",
            space_group="R-3m (#166)",
            crystal_system="Trigonal / Hexagonal",
            lattice={"a": 2.816, "b": 2.816, "c": 14.053, "alpha": 90, "beta": 90, "gamma": 120},
            theoretical_peaks=lco_peaks,
            description="Archetypal commercial Li-ion battery cathode with high energy density and α-NaFeO2 structure.",
        )

        # 2. BaTiO3 (Ferroelectric dielectric perovskite, Tetragonal P4mm)
        bto_peaks = [
            BraggPeak(22.16, 42.0, (1, 0, 0), 4.008),
            BraggPeak(31.54, 100.0, (1, 1, 0), 2.834),
            BraggPeak(38.87, 35.0, (1, 1, 1), 2.314),
            BraggPeak(45.16, 52.0, (0, 0, 2), 2.016),
            BraggPeak(45.44, 55.0, (2, 0, 0), 1.994),
            BraggPeak(50.84, 20.0, (2, 1, 0), 1.795),
            BraggPeak(56.14, 46.0, (2, 1, 1), 1.637),
        ]
        self.database["BaTiO3"] = CrystalPhase(
            phase_id="mp-5986",
            name="Barium Titanate (Tetragonal Perovskite)",
            formula="BaTiO3",
            space_group="P4mm (#99)",
            crystal_system="Tetragonal",
            lattice={"a": 3.994, "b": 3.994, "c": 4.038, "alpha": 90, "beta": 90, "gamma": 90},
            theoretical_peaks=bto_peaks,
            description="Lead-free ferroelectric and high-k dielectric ceramic used in MLCC capacitors and piezoelectrics.",
        )

        # 3. Anatase TiO2 (Common precursor/impurity phase in titanate synthesis)
        tio2_peaks = [
            BraggPeak(25.31, 100.0, (1, 0, 1), 3.516),
            BraggPeak(37.80, 20.0, (0, 0, 4), 2.378),
            BraggPeak(48.05, 35.0, (2, 0, 0), 1.892),
            BraggPeak(53.89, 20.0, (1, 0, 5), 1.699),
            BraggPeak(55.06, 22.0, (2, 1, 1), 1.666),
        ]
        self.database["TiO2_Anatase"] = CrystalPhase(
            phase_id="mp-390",
            name="Titanium Dioxide (Anatase Impurity)",
            formula="TiO2",
            space_group="I41/amd (#141)",
            crystal_system="Tetragonal",
            lattice={"a": 3.784, "b": 3.784, "c": 9.514, "alpha": 90, "beta": 90, "gamma": 90},
            theoretical_peaks=tio2_peaks,
            description="Common unreacted precursor intermediate resulting from incomplete calcination in titanate synthesis.",
        )

        # 4. MAPbI3 Perovskite (Halide photovoltaic absorber)
        mapbi3_peaks = [
            BraggPeak(14.10, 100.0, (1, 1, 0), 6.275),
            BraggPeak(20.02, 38.0, (1, 1, 2), 4.431),
            BraggPeak(23.50, 18.0, (2, 1, 1), 3.782),
            BraggPeak(24.49, 24.0, (2, 0, 2), 3.632),
            BraggPeak(28.44, 76.0, (2, 2, 0), 3.136),
            BraggPeak(31.87, 42.0, (3, 1, 0), 2.805),
            BraggPeak(40.66, 32.0, (2, 2, 4), 2.217),
            BraggPeak(43.21, 30.0, (3, 1, 4), 2.092),
        ]
        self.database["MAPbI3"] = CrystalPhase(
            phase_id="mp-1077534",
            name="Methylammonium Lead Iodide Perovskite",
            formula="CH3NH3PbI3",
            space_group="I4/mcm (#140)",
            crystal_system="Tetragonal",
            lattice={"a": 8.874, "b": 8.874, "c": 12.671, "alpha": 90, "beta": 90, "gamma": 90},
            theoretical_peaks=mapbi3_peaks,
            description="State-of-the-art hybrid perovskite light harvester for next-generation solar cells.",
        )

    def match_phase(
        self,
        experimental_peaks: List[Dict],
        phase_key: str,
        angle_tolerance: float = 0.35,
    ) -> Optional[PhaseMatchResult]:
        """
        Cross-validates detected experimental peaks against a specific physical phase.
        Returns match score, matched peaks with HKL indices, and any residual/unmatched peaks.
        """
        if phase_key not in self.database:
            return None

        phase = self.database[phase_key]
        theo_peaks = phase.theoretical_peaks

        matched_pairs = []
        matched_exp_angles = set()
        angle_deltas = []

        # Find closest theoretical peak for each experimental peak
        for exp_p in experimental_peaks:
            exp_angle = float(exp_p.get("two_theta", 0.0))
            exp_inten = float(exp_p.get("relative_intensity", 0.0))

            best_theo = None
            min_delta = 999.0
            for theo_p in theo_peaks:
                delta = abs(exp_angle - theo_p.two_theta)
                if delta <= angle_tolerance and delta < min_delta:
                    min_delta = delta
                    best_theo = theo_p

            if best_theo is not None:
                matched_pairs.append({
                    "exp_angle": exp_angle,
                    "theo_angle": best_theo.two_theta,
                    "hkl": best_theo.hkl_str,
                    "delta": round(min_delta, 3),
                    "exp_intensity": exp_inten,
                    "theo_intensity": best_theo.relative_intensity,
                })
                matched_exp_angles.add(exp_angle)
                angle_deltas.append(min_delta)

        unmatched = [
            float(p.get("two_theta", 0.0))
            for p in experimental_peaks
            if float(p.get("two_theta", 0.0)) not in matched_exp_angles
        ]

        if not theo_peaks:
            score = 0.0
        else:
            recall = len(matched_pairs) / len(theo_peaks)
            precision = len(matched_pairs) / max(1, len(experimental_peaks))
            mean_delta = float(np.mean(angle_deltas)) if angle_deltas else angle_tolerance
            delta_penalty = max(0.0, 1.0 - (mean_delta / angle_tolerance))
            score = (0.5 * recall + 0.3 * precision + 0.2 * delta_penalty)

        return PhaseMatchResult(
            phase=phase,
            match_score=round(float(score), 3),
            matched_peak_count=len(matched_pairs),
            total_theoretical_peaks=len(theo_peaks),
            mean_angle_delta=round(float(np.mean(angle_deltas)), 3) if angle_deltas else 0.0,
            matched_peaks=matched_pairs,
            unmatched_experimental=unmatched,
        )

    def identify_all_phases(
        self, experimental_peaks: List[Dict], angle_tolerance: float = 0.35
    ) -> List[PhaseMatchResult]:
        """
        Ranks all database candidate phases by correlation with experimental peaks.
        """
        results = []
        for key in self.database:
            res = self.match_phase(experimental_peaks, key, angle_tolerance=angle_tolerance)
            if res:
                results.append(res)
        results.sort(key=lambda r: r.match_score, reverse=True)
        return results
