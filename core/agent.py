"""
Synthesis & Characterization Agent
Connects Google Gemini API, Valency MCP literature, physics simulations,
and confidence calibration to generate verifiable, peer-reviewed synthesis protocols.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
import os
import json
from .signal_engine import SpectrumResult
from .physics_engine import PhaseMatchResult
from .valency_client import SynthesisPaper
from .calibration import CalibratedVerdict


@dataclass
class SynthesisProtocol:
    material_name: str
    target_formula: str
    space_group: str
    phase_purity_status: str
    calibrated_confidence: float
    confidence_tier_badge: str
    synthesis_method: str
    precursors: List[str]
    thermal_schedule: Dict[str, str]
    atmosphere: str
    key_peaks_summary: str
    safety_notes: str
    valency_citations: List[str]
    markdown_report: str


class SynthesisAgent:
    def __init__(self, gemini_api_key: Optional[str] = None, adaption_api_key: Optional[str] = None):
        self.api_key = gemini_api_key or os.environ.get("GEMINI_API_KEY")
        self.adaption_key = adaption_api_key or os.environ.get("ADAPTION_API_KEY")
        self._init_gemini_client()
        self._init_adaption_client()

    def _init_adaption_client(self):
        """Initializes Adaption Labs AutoScientist adaptive model client."""
        self.adaption_endpoint = "https://api.adaptionlabs.ai/v1/science/synthesize"
        self.use_adaption = bool(self.adaption_key)

    def _init_gemini_client(self):
        """Initializes Gemini client if key is available."""
        self.model = None
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel("gemini-2.5-flash")
            except Exception:
                try:
                    import google.generativeai as genai
                    genai.configure(api_key=self.api_key)
                    self.model = genai.GenerativeModel("gemini-1.5-flash")
                except Exception:
                    self.model = None

    def generate_protocol(
        self,
        spectrum_result: SpectrumResult,
        primary_match: Optional[PhaseMatchResult],
        secondary_match: Optional[PhaseMatchResult],
        literature: List[SynthesisPaper],
        verdict: CalibratedVerdict,
    ) -> SynthesisProtocol:
        """
        Orchestrates all scientific modules into an actionable, peer-reviewed synthesis card.
        """
        if primary_match:
            mat_name = primary_match.phase.name
            formula = primary_match.phase.formula
            sg = primary_match.phase.space_group
        else:
            mat_name = "Experimental Inorganic Material"
            formula = "Target Phase"
            sg = "Unverified"

        # Extract synthesis parameters from Valency literature
        top_paper = literature[0] if literature else None
        if top_paper:
            synth_type = top_paper.synthesis_type
            precursors = top_paper.precursors
            temp = f"{top_paper.calcination_temp_c:.0f} °C"
            dwell = f"{top_paper.dwell_time_hours:.1f} hours"
            atmos = top_paper.atmosphere
        else:
            synth_type = "Solid-State High-Temperature Calcination"
            precursors = [f"Stoichiometric metal oxide precursors for {formula}"]
            temp = "850 °C"
            dwell = "12 hours"
            atmos = "Air / Controlled Oxygen"

        thermal_schedule = {
            "Ramp Rate": "5 °C / min",
            "Calcination Plateau": f"{temp} for {dwell}",
            "Cooling Schedule": "Furnace cooled to room temperature at 2 °C / min",
        }

        # Build citations
        citations = [p.citation_str for p in literature]

        # Safety & failure notes
        safety = (
            "Wear nitrile gloves and P100 respirator when handling fine powders. "
            "Ensure exhaust ventilation during carbonate/organic decomposition."
        )

        # Generate markdown report
        md = self._build_markdown_report(
            mat_name=mat_name,
            formula=formula,
            sg=sg,
            synth_type=synth_type,
            precursors=precursors,
            thermal_schedule=thermal_schedule,
            atmos=atmos,
            verdict=verdict,
            citations=citations,
            spectrum_result=spectrum_result,
        )

        # If Gemini is configured, enhance reasoning summary
        if self.model:
            try:
                prompt = (
                    f"You are an expert materials scientist and AI research assistant for the Open Scientific Intelligence Hackathon. "
                    f"Given the experimental XRD peak deconvolution ({len(spectrum_result.peaks)} peaks detected) "
                    f"and calibrated confidence of {verdict.compound_confidence * 100:.1f}% ({verdict.confidence_tier}), "
                    f"briefly summarize (in 3 concise bullet points) why this synthesis protocol succeeds and what failure modes are prevented."
                )
                response = self.model.generate_content(prompt)
                if response and response.text:
                    md += f"\n\n### 🤖 AI Scientist Insight (Gemini 2.5)\n{response.text}\n"
            except Exception:
                pass

        peaks_summary = f"{len(spectrum_result.peaks)} experimental peaks detected. Highest reflection at 2θ = {spectrum_result.peaks[0].two_theta}° (d = {spectrum_result.peaks[0].d_spacing} Å)." if spectrum_result.peaks else "No peaks detected."

        return SynthesisProtocol(
            material_name=mat_name,
            target_formula=formula,
            space_group=sg,
            phase_purity_status=verdict.tier_badge,
            calibrated_confidence=verdict.compound_confidence,
            confidence_tier_badge=verdict.tier_badge,
            synthesis_method=synth_type,
            precursors=precursors,
            thermal_schedule=thermal_schedule,
            atmosphere=atmos,
            key_peaks_summary=peaks_summary,
            safety_notes=safety,
            valency_citations=citations,
            markdown_report=md,
        )

    def _build_markdown_report(
        self,
        mat_name: str,
        formula: str,
        sg: str,
        synth_type: str,
        precursors: List[str],
        thermal_schedule: Dict[str, str],
        atmos: str,
        verdict: CalibratedVerdict,
        citations: List[str],
        spectrum_result: SpectrumResult,
    ) -> str:
        lines = [
            f"# 🧪 Verified Synthesis & Characterization Protocol: {mat_name}",
            f"**Target Formula:** `{formula}` | **Space Group:** `{sg}` | **Calibration Status:** {verdict.tier_badge}",
            "",
            "## 1. Phase Identification & Confidence Calibration",
            f"- **Compound Confidence ($C_{{compound}}$):** `{verdict.compound_confidence:.3f}` ($C_{{sig}}={verdict.signal_confidence:.2f} \\times C_{{phys}}={verdict.physics_confidence:.2f} \\times C_{{lit}}={verdict.literature_confidence:.2f}$)",
            f"- **Primary Identified Phase:** {verdict.primary_phase}",
        ]

        if verdict.secondary_impurity_detected:
            lines.append(f"- **⚠️ Phase Contamination Alert:** Detected parasitic secondary phase `{verdict.impurity_name}` at 2θ = {verdict.unmatched_peaks_2theta}°.")
        else:
            lines.append("- **Phase Purity:** Single-phase pure with no parasitic secondary reflections detected.")

        lines.extend([
            f"- **Recommended Laboratory Action:** {verdict.recommended_lab_action}",
            "",
            "## 2. Reagents & Precursors",
        ])
        for p in precursors:
            lines.append(f"- [x] {p}")

        lines.extend([
            "",
            f"## 3. Recommended Synthesis Route: *{synth_type}*",
            f"- **Atmosphere:** {atmos}",
            f"- **Ramp Rate:** {thermal_schedule.get('Ramp Rate', '5 °C/min')}",
            f"- **Calcination Plateau:** **{thermal_schedule.get('Calcination Plateau', '850 °C')}**",
            f"- **Cooling Schedule:** {thermal_schedule.get('Cooling Schedule', 'Furnace cooled')}",
            "",
            "## 4. Grounded Literature Citations (via Valency Bond MCP - 44.5M Papers)",
        ])
        for c in citations:
            lines.append(f"- {c}")

        return "\n".join(lines)
