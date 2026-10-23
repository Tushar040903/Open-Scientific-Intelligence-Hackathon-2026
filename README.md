# 🔬 SpectraBond-AI
### *Autonomous Multimodal Characterization & Inverse Synthesis Intelligence Grounded in 44.5M Papers via Valency MCP with Physics-Calibrated Verification*

[![OSI Hackathon 2026](https://img.shields.io/badge/OSI_Hackathon-2026-blue.svg)](https://llmhackathon.github.io/)
[![Valency MCP Bond](https://img.shields.io/badge/Grounded_in-Valency_Bond_(44.5M_Papers)-7C3AED.svg)](https://valency.io)
[![Marimo App](https://img.shields.io/badge/Built_with-Marimo_Reactive_Platform-10B981.svg)](https://marimo.io)
[![Gemini 2.5](https://img.shields.io/badge/AI_Engine-Google_Gemini_2.5-EA4335.svg)](https://deepmind.google/technologies/gemini/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![SpectraBond-AI Cover](https://raw.githubusercontent.com/Tushar040903/Open-Scientific-Intelligence-Hackathon-2026/main/assets/cover_image.png)

> 🎥 **Video Demo (Loom):** [https://www.loom.com/share/c1895a5418994d77a9ceeff7419004b6](https://www.loom.com/share/c1895a5418994d77a9ceeff7419004b6)  
> 💻 **GitHub Repository:** [https://github.com/Tushar040903/Open-Scientific-Intelligence-Hackathon-2026](https://github.com/Tushar040903/Open-Scientific-Intelligence-Hackathon-2026)  
> 👨‍💻 **Author:** Tushar Bhardwaj (Solo Competitor, National Institute of Technology Kurukshetra)

---

## 🌟 Executive Summary

In experimental physical sciences and chemistry, bridging the gap between raw laboratory measurements and actionable synthesis protocols is a notorious bottleneck. When an experimentalist synthesizes a candidate functional material and measures an X-ray diffraction (XRD) or spectroscopic curve:
1. **Manual Deconvolution is Slow:** Peak deconvolution, background subtraction, and phase identification take hours of tedious, subjective fitting.
2. **LLMs Suffer from Hallucinations:** Monolithic LLMs hallucinate non-existent Bragg reflection angles, violate crystal space group symmetries, and suggest dangerous, uncalibrated reaction temperatures.
3. **Literature is Fragmented:** 44.5 million published scientific papers contain exact precursors and calcination schedules, but querying and cross-referencing them with raw experimental data has remained manual.

**SpectraBond-AI** solves this challenge through an autonomous **"Planning-to-Action Constellation"**:
- **Ingests** experimental spectra or microstructural curves (CSV, TSV, or raw instrument curves).
- **Deconvolves** physical diffraction peaks with baseline removal and calculates lattice $d$-spacing and Scherrer crystallite domain sizes.
- **Validates** against crystallographic physics (Bragg's law, crystal systems, space group symmetry).
- **Retrieves** peer-reviewed synthesis recipes and precursor guardrails in real time across **44.5 million papers via Valency Bond MCP**.
- **Calibrates** an end-to-end compound confidence metric ($C_{\text{compound}} = C_{\text{sig}} \times C_{\text{phys}} \times C_{\text{lit}}$) that **flags unreacted trace impurities** before expensive laboratory resources are wasted.
- **Deploys** as a reactive, zero-latency dashboard built on the **Marimo** platform (`marimo run app.py`).

---

## 🏛️ System Architecture

```
                 ┌─────────────────────────────────────────────────────────────┐
                 │                 USER INPUT VIA MARIMO STUDIO                │
                 │  - Experimental Spectrum (XRD/Raman/FTIR CSV or Preset)     │
                 │  - Real-time sliders: Tolerance (Δ2θ) & Prominence Threshold │
                 └──────────────────────────────┬──────────────────────────────┘
                                                │
                                                ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
 │                                   AGENTIC CORE ENGINE                                       │
 │                                                                                             │
 │   ┌─────────────────────────────┐                    ┌──────────────────────────────────┐   │
 │   │  1. Signal Engine           │                    │  2. Valency MCP Bond Engine      │   │
 │   │  - Savitzky-Golay baseline  │                    │  - Queries 44.5M Papers          │   │
 │   │  - Pseudo-Voigt peak fit    │◄──────────────────►│  - Precedent Synthesis Mining    │   │
 │   │  - d-spacing / Mode Match   │                    │  - Precursor Safety & Yields     │   │
 │   │  - Scherrer crystallite size│                    │  - Verified DOIs & Citations     │   │
 │   └──────────────┬──────────────┘                    └─────────────────┬────────────────┘   │
 │                  │                                                     │                    │
 │                  └───────────────────────┬─────────────────────────────┘                    │
 │                                          ▼                                                  │
 │                      ┌───────────────────────────────────────┐                              │
 │                      │      3. Physics Validation Engine     │                              │
 │                      │  - Theoretical Bragg stick generation │                              │
 │                      │  - Space group & lattice verification │                              │
 │                      │  - Impurity candidate cross-matching  │                              │
 │                      └───────────────────┬───────────────────┘                              │
 │                                          │                                                  │
 │                                          ▼                                                  │
 │                      ┌───────────────────────────────────────┐                              │
 │                      │ 4. Compound Confidence Calibration    │                              │
 │                      │    C_compound = C_sig × C_lit × C_phy │                              │
 │                      │  - Risk-Coverage Optimization         │                              │
 │                      │  - Trace Impurity Failure Attribution │                              │
 │                      └───────────────────┬───────────────────┘                              │
 └──────────────────────────────────────────┼──────────────────────────────────────────────────┘
                                            │
                                            ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
 │                                INTERACTIVE MARIMO OUTPUT                                    │
 │  - Reactive Plotly Overlays: Experimental Curve vs. Baseline vs. Theoretical Bragg Peaks     │
 │  - Secondary Phase Alert: Visual markers highlighting unreacted precursor impurities        │
 │  - Step-by-Step Executable Synthesis Protocol with Real DOI Citations from Valency          │
 │  - Calibrated Confidence Gauge (High / Moderate / Risk Alert) with Recommended Actions      │
 └─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏆 Hackathon Sponsor Qualifications

### 1. Materials Discovery Research Institute (MDRI) General Prize
- Directly targets the hackathon core mission: accelerating materials discovery from knowledge to physical action.
- Sits at the nexus of **Knowledge Infrastructure** (Valency literature grounding) and **Action Systems** (physics-based diffraction validation and executable synthesis formulation).

### 2. Valency Sponsor Prize (`Valency MCP Bond`)
- Integrated into `core/valency_client.py` using Valency Bond MCP (Model Context Protocol).
- Queries 44.5 million academic research papers across PubMed, arXiv, ChemRxiv, and CrossRef to ground all recommended precursors, sintering temperatures, dwell times, and reference XRD reflections in peer-reviewed literature.

### 3. Marimo Sponsor Prize (`marimo`)
- Built natively using the **Marimo** reactive application framework (`app.py`).
- Delivers reactive cell re-execution, interactive Plotly visualizations, parameter sliders, and zero-latency synthesis report generation with pure Python reproducibility.

---

## ⚡ Quick Start Guide

### 1. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/Tushar040903/Open-Scientific-Intelligence-Hackathon-2026.git
cd Open-Scientific-Intelligence-Hackathon-2026
pip install -r requirements.txt
```

### 2. Configure Environment (Optional)
To enable live Valency MCP literature search and Gemini reasoning, create a `.env` file:
```env
VALENCY_BOND_TOKEN="your_valency_bearer_token_here"
GEMINI_API_KEY="your_google_gemini_api_key_here"
```
*(Note: SpectraBond-AI includes pre-indexed offline scientific knowledge so all features and demos run seamlessly even without API keys!)*

### 3. Launch the Marimo Reactive Studio
Run the application in web mode:
```bash
marimo run app.py
```
Or open in interactive notebook editing mode:
```bash
marimo edit app.py
```
Open your browser to the local URL (e.g., `http://localhost:2718`).

### 4. Run Automated Test Suite
To verify the full end-to-end scientific pipeline:
```bash
python test_pipeline.py
```

---

## 📊 Benchmark Demonstrations

| Benchmark Material | Target Formula | Primary Identified Phase | Detected Peaks | Confidence Score ($C_{\text{compound}}$) | Impurity Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Battery Cathode** | $\text{LiCoO}_2$ | Layered Trigonal ($R\bar{3}m$) | 8 reflections matched ($\Delta 2\theta = 0.020^\circ$) | **`84.8%` (High Confidence)** | Single-phase pure |
| **Ferroelectric** | $\text{BaTiO}_3$ | Tetragonal Perovskite ($P4mm$) | 7 reflections matched | **`59.9%` (Impurity Alert)** | **Flagged unreacted $\text{TiO}_2$ anatase ($25.3^\circ$)** |
| **Solar Perovskite** | $\text{CH}_3\text{NH}_3\text{PbI}_3$ | Tetragonal Halide ($I4/mcm$) | 8 reflections matched | **`82.5%` (High Confidence)** | Single-phase pure |

---

## 🎥 4-Minute Submission Video Script Outline

| Timestamp | Screen Display | Voiceover / Talking Points |
| :--- | :--- | :--- |
| **0:00 – 0:40** | Slide with Architecture & Problem | *"Hello judges! Experimental materials discovery suffers from a painful disconnect: after collecting a noisy XRD spectrum, researchers spend hours guessing phases, while LLMs hallucinate non-physical crystal symmetries. Here is SpectraBond-AI."* |
| **0:40 – 1:30** | Marimo Studio UI | *"Built on the reactive Marimo platform, SpectraBond-AI combines signal deconvolution with two grounded pillars: physics-based Bragg simulation and Valency Bond MCP connecting to 44.5 million papers."* |
| **1:30 – 2:30** | Live Demo: $\text{LiCoO}_2$ | Selects the $\text{LiCoO}_2$ preset. Shows instantaneous peak deconvolution, Scherrer crystallite sizing, and overlay of theoretical Bragg reflections. Demonstrates the calibrated confidence score ($C_{\text{compound}} = 84.8\%$) and Valency citations with real DOIs. |
| **2:30 – 3:20** | Live Demo: $\text{BaTiO}_3$ Impurity | Switches to the $\text{BaTiO}_3$ with impurity preset. Points to the red vertical marker at $25.3^\circ$. *"Notice how our compound confidence calibrator detects this unreacted anatase $\text{TiO}_2$ impurity, dropping the confidence and advising the researcher to increase sintering temperature by +50°C!"* |
| **3:20 – 4:00** | Synthesis Card & Conclusion | Shows the executable synthesis protocol card with precursor safety rules. Acknowledges MDRI, Valency, and Marimo. Closes with open-source link. |

---

## 👨‍💻 Author & Acknowledgments

- **Developer:** Tushar Bhardwaj (Senior Undergraduate, B.Tech ECE, NIT Kurukshetra)
- **Presented at:** 4th Annual Open Scientific Intelligence (OSI) Hackathon (Oct 21–22, 2026)
- **Sponsors:** Materials Discovery Research Institute (MDRI), Valency, Marimo, Google DeepMind.
