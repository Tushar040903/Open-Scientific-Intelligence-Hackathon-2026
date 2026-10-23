# SpectraBond-AI: Autonomous Multimodal Characterization & Inverse Synthesis Intelligence
**Participant:** Tushar Bhardwaj (Solo Competitor) | **Affiliation:** National Institute of Technology Kurukshetra  
**Event:** 4th Annual Open Scientific Intelligence (OSI) Hackathon (Oct 21–22, 2026)  
**Presented by:** Materials Discovery Research Institute (MDRI / UL Research Institutes)  
**GitHub Repository:** [https://github.com/Tushar040903/Open-Scientific-Intelligence-Hackathon-2026](https://github.com/Tushar040903/Open-Scientific-Intelligence-Hackathon-2026)  
**Video Demo (Loom):** [https://www.loom.com/share/c1895a5418994d77a9ceeff7419004b6](https://www.loom.com/share/c1895a5418994d77a9ceeff7419004b6)

---

### Abstract
In experimental materials discovery, bridging raw structural characterization data to executable synthesis protocols remains a critical bottleneck. Large Language Models frequently hallucinate non-physical crystallographic space groups and uncalibrated reaction parameters. Here, we introduce **SpectraBond-AI**, an autonomous closed-loop intelligence system deployed on **Marimo** that unifies:
1. **Mathematical Signal Deconvolution:** Automated background estimation, Pseudo-Voigt peak fitting, lattice $d$-spacing via Bragg's Law, and domain sizing via the Scherrer equation.
2. **Crystallographic Physics Validation:** Cross-referencing experimental peak reflections against space group symmetries and theoretical Bragg sticks to detect parasitic secondary phases.
3. **Valency MCP Bond Grounding:** Direct semantic querying of 44.5 million peer-reviewed papers to extract empirical precursor ratios, calcination schedules, and verified DOIs.
4. **Compound Confidence Calibration:** A calibrated scoring metric ($C_{\text{compound}} = C_{\text{sig}} \times C_{\text{phys}} \times C_{\text{lit}}$) that calculates risk-coverage trade-offs and provides failure attribution.

---

### System Architecture
```
[Raw Spectrum CSV] ──► [Signal Engine: Voigt Fit & Scherrer] ──► [Detected Peaks (2θ, d, I)]
                                                                           │
       ┌───────────────────────────────────────────────────────────────────┴───────────────────────────────────┐
       ▼                                                                                                       ▼
[Physics Engine: Bragg Verification]                                                        [Valency MCP Bond: 44.5M Papers]
  - Space Group Symmetry Match                                                                - Verified Precursor Precedents
  - Theoretical Stick Calculation                                                             - Sintering Temperature & Atmosphere
  - Trace Impurity Isolation                                                                  - Peer-Reviewed DOI Citations
       │                                                                                                       │
       └───────────────────────────────────┬───────────────────────────────────────────────────────────────────┘
                                           ▼
                    [Compound Confidence Calibration Engine]
                       C_compound = C_sig × C_phys × C_lit
                                           │
                                           ▼
             [Marimo Reactive Studio (Interactive Plotly + Protocol Export)]
```

---

### Benchmark Results & Impurity Detection

| Benchmark Material | Formula | Primary Phase Identified | Correlation | Confidence ($C_{\text{compound}}$) | Impurity / Phase Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Battery Cathode** | $\text{LiCoO}_2$ | Layered Trigonal ($R\bar{3}m$) | 8/8 Bragg Peaks ($\Delta 2\theta = 0.020^\circ$) | **`84.8%` (High)** | Single-phase pure |
| **Ferroelectric** | $\text{BaTiO}_3$ | Tetragonal Perovskite ($P4mm$) | 7/7 Bragg Peaks Matched | **`59.9%` (Alert)** | **Flagged unreacted Anatase $\text{TiO}_2$ ($25.3^\circ$)** |
| **Solar Perovskite** | $\text{CH}_3\text{NH}_3\text{PbI}_3$ | Tetragonal Halide ($I4/mcm$) | 8/8 Bragg Peaks Matched | **`82.5%` (High)** | Single-phase pure |

**Key Innovation:** In the contaminated $\text{BaTiO}_3$ test, SpectraBond-AI detected a lone unreacted peak at $2\theta = 25.31^\circ$, accurately flagged the unreacted $\text{TiO}_2$ precursor phase, penalized the compound confidence to 59.9%, and issued an automated laboratory directive to raise the sintering temperature by $+50^\circ\text{C}$ to complete phase conversion.

---

### Sponsor & Platform Integrations
- **MDRI General Track:** Direct acceleration of planning-to-action workflows for solid-state chemistry and materials discovery.
- **Valency MCP Bond:** Connected to 44.5M papers via the Model Context Protocol to extract grounded synthesis cards.
- **Marimo Platform:** Pure reactive Python dashboard with live Plotly re-rendering and reproducible execution (`marimo run app.py`).
