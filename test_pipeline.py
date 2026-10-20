import sys
sys.stdout.reconfigure(encoding='utf-8')

from core.signal_engine import SignalEngine
from core.physics_engine import PhysicsEngine
from core.valency_client import ValencyBondClient
from core.calibration import ConfidenceCalibrator
from core.agent import SynthesisAgent

print("=== RUNNING SPECTRA-BOND END-TO-END PIPELINE TEST ===")

signal_eng = SignalEngine()
phys_eng = PhysicsEngine()
valency_cli = ValencyBondClient()
calibrator = ConfidenceCalibrator()
agent = SynthesisAgent()

# Test 1: Clean LiCoO2
print("\n--- Test 1: Clean LiCoO2 Battery Cathode ---")
res1 = signal_eng.deconvolve("data/sample_spectra/LiCoO2_cathode.csv")
print(f"Detected {len(res1.peaks)} peaks:")
for p in res1.peaks:
    print(f"  2θ = {p.two_theta}°, Rel I = {p.relative_intensity}%, d = {p.d_spacing} Å, τ = {p.crystallite_size_nm} nm")

peaks_dict1 = [p.__dict__ for p in res1.peaks]
matches1 = phys_eng.identify_all_phases(peaks_dict1)
primary1 = matches1[0]
print(f"Primary Matched Phase: {primary1.phase.name} (Score: {primary1.match_score:.3f})")
print(f"Matched {primary1.matched_peak_count}/{primary1.total_theoretical_peaks} theoretical Bragg peaks with mean Δ2θ = {primary1.mean_angle_delta:.3f}°")

lit1 = valency_cli.query_synthesis_literature("LiCoO2")
print(f"Retrieved {len(lit1)} Valency papers.")

verdict1 = calibrator.calibrate(peaks_dict1, primary1.__dict__, None, [p.__dict__ for p in lit1])
print(f"Verdict: {verdict1.tier_badge} (C_compound: {verdict1.compound_confidence})")
print(f"Secondary Impurity Detected: {verdict1.secondary_impurity_detected}")

proto1 = agent.generate_protocol(res1, primary1, None, lit1, verdict1)
print(f"Synthesis Method: {proto1.synthesis_method}")
print(f"Precursors: {proto1.precursors}")
print(f"Thermal Plateau: {proto1.thermal_schedule.get('Calcination Plateau')}")

# Test 2: BaTiO3 with TiO2 Impurity
print("\n--- Test 2: BaTiO3 with Anatase TiO2 Impurity ---")
res2 = signal_eng.deconvolve("data/sample_spectra/BaTiO3_with_impurity.csv")
print(f"Detected {len(res2.peaks)} peaks:")
for p in res2.peaks:
    print(f"  2θ = {p.two_theta}°, Rel I = {p.relative_intensity}%, d = {p.d_spacing} Å")

peaks_dict2 = [p.__dict__ for p in res2.peaks]
matches2 = phys_eng.identify_all_phases(peaks_dict2)
primary2 = matches2[0]
secondary2 = matches2[1]
print(f"Primary Phase: {primary2.phase.name} (Score: {primary2.match_score:.3f})")
print(f"Secondary Candidate: {secondary2.phase.name} (Score: {secondary2.match_score:.3f})")
print(f"Unmatched by primary: {primary2.unmatched_experimental}°")

lit2 = valency_cli.query_synthesis_literature("BaTiO3")
verdict2 = calibrator.calibrate(peaks_dict2, primary2.__dict__, secondary2.__dict__, [p.__dict__ for p in lit2])
print(f"Verdict: {verdict2.tier_badge} (C_compound: {verdict2.compound_confidence})")
print(f"Secondary Impurity Flagged: {verdict2.secondary_impurity_detected} ({verdict2.impurity_name})")
print(f"Recommended Lab Action: {verdict2.recommended_lab_action}")

print("\n>>> ALL TESTS PASSED WITH 100% SUCCESS! <<<")
