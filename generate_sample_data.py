import numpy as np
import pandas as pd
import os

os.makedirs("data/sample_spectra", exist_ok=True)

def pseudo_voigt(x, x0, intensity, fwhm, eta=0.5):
    """Pseudo-Voigt peak profile: combination of Gaussian and Lorentzian."""
    sigma = fwhm / (2 * np.sqrt(2 * np.log(2)))
    gamma = fwhm / 2.0
    gauss = np.exp(-((x - x0) ** 2) / (2 * sigma ** 2))
    lorentz = (gamma ** 2) / ((x - x0) ** 2 + gamma ** 2)
    return intensity * (eta * lorentz + (1 - eta) * gauss)

two_theta = np.linspace(10.0, 75.0, 1500)

# 1. LiCoO2 Battery Cathode (Layered R-3m)
peaks_lco = [
    (18.92, 1000.0, 0.28, "(003)"),
    (37.35, 220.0, 0.32, "(101)"),
    (38.38, 250.0, 0.32, "(012)"),
    (45.24, 780.0, 0.35, "(104)"),
    (49.52, 190.0, 0.34, "(015)"),
    (59.10, 280.0, 0.38, "(107)"),
    (65.34, 310.0, 0.40, "(108)"),
    (66.52, 290.0, 0.40, "(110)"),
]

bg_lco = 80.0 + 150.0 * np.exp(-two_theta / 18.0)
y_lco = bg_lco.copy()
for pos, inten, w, hkl in peaks_lco:
    y_lco += pseudo_voigt(two_theta, pos, inten, w)

# Add realistic experimental detector noise
np.random.seed(42)
y_lco += np.random.normal(0, 12.0, len(two_theta))
y_lco = np.maximum(y_lco, 0.0)

df_lco = pd.DataFrame({"two_theta": np.round(two_theta, 3), "intensity": np.round(y_lco, 2)})
df_lco.to_csv("data/sample_spectra/LiCoO2_cathode.csv", index=False)
print("Saved data/sample_spectra/LiCoO2_cathode.csv")

# 2. BaTiO3 Ferroelectric with TiO2 Unreacted Impurity
peaks_bto = [
    (22.15, 420.0, 0.26, "(100)"),
    (31.52, 1000.0, 0.30, "(110)"),
    (38.85, 360.0, 0.32, "(111)"),
    (45.18, 510.0, 0.34, "(002)"),
    (45.42, 540.0, 0.34, "(200)"),
    (50.82, 210.0, 0.36, "(210)"),
    (56.12, 450.0, 0.38, "(211)"),
    # Impurity: Anatase TiO2 (101) peak indicating incomplete solid-state reaction
    (25.32, 215.0, 0.30, "TiO2_impurity_(101)"),
]

bg_bto = 70.0 + 120.0 * np.exp(-two_theta / 22.0)
y_bto = bg_bto.copy()
for pos, inten, w, hkl in peaks_bto:
    y_bto += pseudo_voigt(two_theta, pos, inten, w)

y_bto += np.random.normal(0, 10.0, len(two_theta))
y_bto = np.maximum(y_bto, 0.0)

df_bto = pd.DataFrame({"two_theta": np.round(two_theta, 3), "intensity": np.round(y_bto, 2)})
df_bto.to_csv("data/sample_spectra/BaTiO3_with_impurity.csv", index=False)
print("Saved data/sample_spectra/BaTiO3_with_impurity.csv")

# 3. MAPbI3 Perovskite (Tetragonal Solar Absorber)
peaks_mapbi3 = [
    (14.08, 1000.0, 0.22, "(110)"),
    (20.01, 380.0, 0.25, "(112)"),
    (23.48, 180.0, 0.28, "(211)"),
    (24.47, 240.0, 0.28, "(202)"),
    (28.42, 750.0, 0.30, "(220)"),
    (31.85, 410.0, 0.32, "(310)"),
    (40.64, 320.0, 0.35, "(224)"),
    (43.19, 290.0, 0.36, "(314)"),
]

bg_mapbi3 = 60.0 + 100.0 * np.exp(-two_theta / 20.0)
y_mapbi3 = bg_mapbi3.copy()
for pos, inten, w, hkl in peaks_mapbi3:
    y_mapbi3 += pseudo_voigt(two_theta, pos, inten, w)

y_mapbi3 += np.random.normal(0, 9.0, len(two_theta))
y_mapbi3 = np.maximum(y_mapbi3, 0.0)

df_mapbi3 = pd.DataFrame({"two_theta": np.round(two_theta, 3), "intensity": np.round(y_mapbi3, 2)})
df_mapbi3.to_csv("data/sample_spectra/MAPbI3_perovskite.csv", index=False)
print("Saved data/sample_spectra/MAPbI3_perovskite.csv")
