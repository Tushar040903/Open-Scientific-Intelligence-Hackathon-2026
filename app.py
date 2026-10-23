import marimo

__generated_with = "0.25.2"
app = marimo.App(
    width="medium",
    app_title="SpectraBond-AI | Open Scientific Intelligence Studio",
)


@app.cell
def __():
    import os
    import sys
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    import marimo as mo

    from core.signal_engine import SignalEngine, SpectrumResult
    from core.physics_engine import PhysicsEngine
    from core.valency_client import ValencyBondClient
    from core.calibration import ConfidenceCalibrator
    from core.agent import SynthesisAgent

    return (
        ConfidenceCalibrator,
        PhysicsEngine,
        SignalEngine,
        SpectrumResult,
        SynthesisAgent,
        ValencyBondClient,
        go,
        make_subplots,
        mo,
        np,
        os,
        pd,
        sys,
    )


@app.cell
def __(mo):
    return mo.md(
        """
        # 🔬 SpectraBond-AI
        ### *Autonomous Multimodal Characterization & Inverse Synthesis Intelligence*
        **4th Annual Open Scientific Intelligence (OSI) Hackathon 2026**  
        *Presented by Materials Discovery Research Institute (MDRI / UL Research Institutes)*

        ---
        `🏆 MDRI General Prize Candidate` | `⚡ Valency MCP Bond Grounded (44.5M Papers)` | `🚀 Marimo Reactive Studio` | `🧠 Gemini 2.5 Science Engine`
        """
    )


@app.cell
def __(mo):
    preset_selector = mo.ui.dropdown(
        options={
            "🔋 LiCoO2 — High-Rate Battery Cathode (Clean Single-Phase R-3m)": "data/sample_spectra/LiCoO2_cathode.csv",
            "⚡ BaTiO3 — Ferroelectric Perovskite (Contains TiO2 Unreacted Impurity)": "data/sample_spectra/BaTiO3_with_impurity.csv",
            "☀️ MAPbI3 — Solar Halide Perovskite (Tetragonal I4/mcm)": "data/sample_spectra/MAPbI3_perovskite.csv",
        },
        value="🔋 LiCoO2 — High-Rate Battery Cathode (Clean Single-Phase R-3m)",
        label="Select Benchmark Spectrum Preset:",
    )

    tolerance_slider = mo.ui.slider(
        start=0.1,
        stop=0.8,
        step=0.05,
        value=0.35,
        label="Crystallographic Match Tolerance (Δ2θ deg):",
    )

    prominence_slider = mo.ui.slider(
        start=0.01,
        stop=0.10,
        step=0.01,
        value=0.03,
        label="Peak Prominence Detection Threshold:",
    )

    file_uploader = mo.ui.file(
        filetypes=[".csv", ".tsv", ".txt"],
        label="Or Upload Custom Experimental Spectrum (CSV):",
    )

    return (
        file_uploader,
        preset_selector,
        prominence_slider,
        tolerance_slider,
        mo.vstack([
            mo.hstack([preset_selector, tolerance_slider, prominence_slider], justify="start", gap=2),
            file_uploader,
        ])
    )


@app.cell
def __(
    ConfidenceCalibrator,
    PhysicsEngine,
    SignalEngine,
    SynthesisAgent,
    ValencyBondClient,
    file_uploader,
    preset_selector,
    prominence_slider,
    tolerance_slider,
):
    # Initialize engines
    signal_eng = SignalEngine()
    phys_eng = PhysicsEngine()
    valency_cli = ValencyBondClient()
    calibrator = ConfidenceCalibrator(tolerance=tolerance_slider.value)
    agent = SynthesisAgent()

    # Determine data source
    if file_uploader.value:
        import io
        csv_bytes = file_uploader.value[0].contents
        source = io.BytesIO(csv_bytes)
        source_name = file_uploader.value[0].name
    else:
        source = preset_selector.value
        source_name = str(preset_selector.value).split("/")[-1]

    # 1. Signal Deconvolution
    spec_result = signal_eng.deconvolve(source, prominence=prominence_slider.value)
    peaks_df = spec_result.to_peak_dataframe()
    peaks_dict = [p.__dict__ for p in spec_result.peaks]

    # 2. Physics & Crystallographic Matching
    matched_phases = phys_eng.identify_all_phases(peaks_dict, angle_tolerance=tolerance_slider.value)
    primary_phase = matched_phases[0] if matched_phases else None
    secondary_phase = matched_phases[1] if len(matched_phases) > 1 else None

    # Check if primary phase candidate name is identified
    target_key = "LiCoO2"
    if primary_phase:
        if "LiCoO2" in primary_phase.phase.formula:
            target_key = "LiCoO2"
        elif "BaTiO3" in primary_phase.phase.formula:
            target_key = "BaTiO3"
        elif "Pb" in primary_phase.phase.formula or "MA" in primary_phase.phase.formula:
            target_key = "MAPbI3"

    # 3. Valency Bond MCP Literature Retrieval (44.5M Papers)
    literature_papers = valency_cli.query_synthesis_literature(target_key)

    # 4. Compound Confidence Calibration
    verdict = calibrator.calibrate(
        signal_peaks=peaks_dict,
        primary_match=primary_phase.__dict__ if primary_phase else None,
        secondary_match=secondary_phase.__dict__ if secondary_phase else None,
        literature_papers=[p.__dict__ for p in literature_papers],
    )

    # 5. Agentic Synthesis Protocol
    protocol = agent.generate_protocol(
        spectrum_result=spec_result,
        primary_match=primary_phase,
        secondary_match=secondary_phase,
        literature=literature_papers,
        verdict=verdict,
    )

    return (
        agent,
        calibrator,
        literature_papers,
        matched_phases,
        peaks_df,
        peaks_dict,
        phys_eng,
        primary_phase,
        protocol,
        secondary_phase,
        signal_eng,
        source_name,
        spec_result,
        target_key,
        valency_cli,
        verdict,
    )


@app.cell
def __(go, make_subplots, np, primary_phase, spec_result, verdict):
    # Plotly Reactive Scientific Visualizer
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.08,
        subplot_titles=(
            f"Experimental Spectrum Deconvolution & Bragg Reflections ({verdict.primary_phase})",
            "Simulated Theoretical Reference & Impurity Trace",
        ),
        row_heights=[0.65, 0.35],
    )

    # 1. Experimental Raw Intensity
    fig.add_trace(
        go.Scatter(
            x=spec_result.two_theta,
            y=spec_result.raw_intensity,
            mode="lines",
            name="Experimental Raw",
            line=dict(color="#2563EB", width=1.5),
        ),
        row=1,
        col=1,
    )

    # 2. Estimated Baseline
    fig.add_trace(
        go.Scatter(
            x=spec_result.two_theta,
            y=spec_result.background,
            mode="lines",
            name="Estimated Baseline",
            line=dict(color="#9CA3AF", width=1.2, dash="dash"),
        ),
        row=1,
        col=1,
    )

    # 3. Deconvolved Peaks
    peak_x = [p.two_theta for p in spec_result.peaks]
    peak_y = [spec_result.raw_intensity[p.index] for p in spec_result.peaks]
    peak_labels = [f"2θ={p.two_theta}°<br>d={p.d_spacing}Å<br>τ={p.crystallite_size_nm}nm" for p in spec_result.peaks]

    fig.add_trace(
        go.Scatter(
            x=peak_x,
            y=peak_y,
            mode="markers+text",
            name="Deconvolved Peaks",
            marker=dict(color="#DC2626", size=8, symbol="triangle-down"),
            text=[f"{p.two_theta}°" for p in spec_result.peaks],
            textposition="top center",
            hovertext=peak_labels,
        ),
        row=1,
        col=1,
    )

    # 4. Theoretical Bragg Diffraction Bars
    if primary_phase:
        theo_peaks = primary_phase.phase.theoretical_peaks
        max_exp = float(np.max(spec_result.corrected_intensity))
        for tp in theo_peaks:
            bar_height = (tp.relative_intensity / 100.0) * max_exp
            fig.add_trace(
                go.Scatter(
                    x=[tp.two_theta, tp.two_theta],
                    y=[0, bar_height],
                    mode="lines",
                    name=f"Theor. {tp.hkl_str}",
                    line=dict(color="#059669", width=2.5),
                    hoverinfo="text",
                    hovertext=f"Theor. 2θ={tp.two_theta}° {tp.hkl_str} (Rel I={tp.relative_intensity}%)",
                    showlegend=False,
                ),
                row=2,
                col=1,
            )

    # 5. Highlight Secondary Phase Impurities if Detected
    if verdict.secondary_impurity_detected and verdict.unmatched_peaks_2theta:
        for u_angle in verdict.unmatched_peaks_2theta:
            fig.add_vline(
                x=u_angle,
                line_width=2,
                line_dash="dot",
                line_color="#E11D48",
                annotation_text="⚠️ Impurity",
                annotation_position="top right",
                row=1,
                col=1,
            )

    fig.update_layout(
        height=580,
        margin=dict(l=40, r=40, t=50, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white",
    )
    fig.update_xaxes(title_text="Diffraction Angle 2θ (degrees, Cu Kα)", row=2, col=1)
    fig.update_yaxes(title_text="Intensity (counts)", row=1, col=1)
    fig.update_yaxes(title_text="Theoretical Rel. I", row=2, col=1)

    return fig, peak_labels, peak_x, peak_y


@app.cell
def __(fig, mo, peaks_df, verdict):
    # UI Layout: Visual Status Badges and Spectrum Plot
    status_markdown = f"""
    ### 🛡️ Compound Confidence Calibration ($C_{{compound}} = C_{{sig}} \\times C_{{phys}} \\times C_{{lit}}$)
    | Metric | Calibrated Value | Status / Description |
    | :--- | :--- | :--- |
    | **Overall Compound Confidence ($C_{{compound}}$)** | **`{verdict.compound_confidence:.3f}`** | **{verdict.tier_badge}** |
    | **Signal Quality Score ($C_{{sig}}$)** | `{verdict.signal_confidence:.3f}` | Deconvolved from experimental detector curve |
    | **Crystallographic Physics Score ($C_{{phys}}$)** | `{verdict.physics_confidence:.3f}` | Bragg law & lattice symmetry validation |
    | **Literature Concordance Score ($C_{{lit}}$)** | `{verdict.literature_confidence:.3f}` | Grounded via Valency Bond MCP (44.5M papers) |
    | **Identified Primary Phase** | `{verdict.primary_phase}` | Space group & lattice parameters verified |
    """

    if verdict.secondary_impurity_detected:
        status_markdown += f"\n> ⚠️ **SECONDARY IMPURITY DETECTED:** Unreacted `{verdict.impurity_name}` flagged at 2θ = {verdict.unmatched_peaks_2theta}°. Recommended action: {verdict.recommended_lab_action}\n"
    else:
        status_markdown += f"\n> ✅ **PHASE PURITY VERIFIED:** Single-phase crystal structure confirmed with high fidelity.\n"

    return mo.vstack([
        mo.md(status_markdown),
        mo.ui.plotly(fig),
        mo.accordion({"📊 Deconvolved Peak Parameter Table (d-spacing & Scherrer Size)": mo.ui.table(peaks_df)}),
    ])


@app.cell
def __(literature_papers, mo, protocol):
    # Literature & Synthesis Output Cards
    lit_md = "### 📚 Valency Bond MCP Literature Grounding (44.5M Research Papers)\n"
    for i, paper in enumerate(literature_papers):
        lit_md += f"""
        #### {i+1}. {paper.title}
        - **Authors & Journal:** {paper.authors} ({paper.year}) — *{paper.journal}*
        - **Verified DOI:** [{paper.doi}](https://doi.org/{paper.doi})
        - **Reported Route:** `{paper.synthesis_type}` | **Calcination:** `{paper.calcination_temp_c:.0f}°C` for `{paper.dwell_time_hours:.1f}h` in `{paper.atmosphere}`
        - **Precursors:** {', '.join(paper.precursors)}
        - **Extracted Insight:** *"{paper.key_findings}"*
        ---
        """

    synth_card = f"""
    ### ⚗️ Autonomous Executable Laboratory Synthesis Protocol
    **Target Material:** `{protocol.material_name}` (`{protocol.target_formula}`) | **Space Group:** `{protocol.space_group}`  
    **Confidence Status:** {protocol.confidence_tier_badge}

    #### 1. Precursors & Stoichiometry:
    {chr(10).join(['- ' + p for p in protocol.precursors])}

    #### 2. Thermal Calcination Schedule:
    - **Heating Ramp:** {protocol.thermal_schedule.get('Ramp Rate')}
    - **Target Plateau:** **{protocol.thermal_schedule.get('Calcination Plateau')}**
    - **Cooling Rate:** {protocol.thermal_schedule.get('Cooling Schedule')}
    - **Atmospheric Control:** {protocol.atmosphere}

    #### 3. Safety & Precautionary Guardrails:
    > 🛡️ {protocol.safety_notes}
    """

    return mo.tabs({
        "⚗️ Executable Synthesis Card": mo.md(synth_card),
        "📚 Valency Literature Citations": mo.md(lit_md),
        "📄 Full Markdown Report": mo.md(f"```markdown\n{protocol.markdown_report}\n```"),
    })


if __name__ == "__main__":
    app.run()
