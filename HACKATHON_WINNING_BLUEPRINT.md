# 🏆 Open Scientific Intelligence (OSI) Hackathon 2026: Solo Winner Blueprint

> **Event:** 4th Annual Open Scientific Intelligence Hackathon (Presented by Materials Discovery Research Institute - MDRI / UL Research Institutes)  
> **Dates:** October 21–22, 2026  
> **Participant:** Tushar Bhardwaj (Solo Competitor)  
> **Target Awards:** MDRI General Prize ($10K pool / Lila Prize), Valency Sponsor Prize (MCP Bond), Marimo Sponsor Prize (Reactive Notebook/App), Visionary Award.

---

## Executive Summary & Winning Strategy for a Solo Competitor

In 2025, over 120 teams competed across 16 global sites. Notably, **a solo researcher (`MJRaei` with *CrystaLenz*) took 4th Place Overall (Lila Prize)** against teams of 5 to 10 researchers by executing a razor-sharp, physics-grounded characterization pipeline. 

The hackathon organizers (led by Dr. Ben Blaiszik, UChicago/MDRI) explicitly evaluate projects based on the **"Planning-to-Action Constellation"**:
1. **Knowledge Infrastructure:** Curated literature grounding, traceable citations, and reproducible datasets.
2. **Action Systems:** Active tool calling, physical simulation verification (e.g., `pymatgen`, `rdkit`, `ase`), and automated workflow execution.
3. **Closing the Loop:** Moving beyond generic "Chat with PDF" RAG into **"Two days to a real discovery"**—where an AI agent ingests experimental data or scientific targets, grounds hypotheses in peer-reviewed literature, verifies them against computational physics, and outputs calibrated, executable protocols.

By leveraging your distinctive background in **Document AI, Computer Vision, Compound Confidence Calibration (AURC), and Multi-Agent Systems**, this blueprint gives you an unfair advantage: a fully cohesive project engineered to sweep both the general podium and top sponsor prizes.

---

## 🎯 Target Sponsor Prize Alignment Matrix

To maximize your chances of winning multiple prizes, the project is architected from day one to natively satisfy all sponsor requirements:

| Sponsor / Award | Qualification Requirement | How Our Project Qualifies | Prize Potential |
| :--- | :--- | :--- | :--- |
| **MDRI General Prize** *(Lila Prizes 1st–5th)* | Top overall scores in Impact, Novelty, Scalability, and Scientific Relevance. | Solves the primary experimental bottleneck: connecting raw multimodal characterization (XRD/Raman) to literature synthesis and simulated validation. | **$10,000 Prize Pool** |
| **Valency Sponsor Prize** | Must integrate **Valency Bond / MCP Bond** to connect your agent to 44.5M research papers. | We use Valency MCP Bond as our primary literature retrieval and recipe-mining backbone across 7 academic repositories. | **Valency Sponsor Award + Credits** |
| **Marimo Sponsor Prize** | Must build on the **Marimo** platform (reactive Python notebook / web app). | Entire frontend and interactive discovery studio is built as a reactive Marimo application (`marimo run app.py`), providing zero-latency reactive UI and reproducible cells. | **Marimo Sponsor Award** |
| **Adaption Labs / NVIDIA / HF** | Using sponsor compute credits or open-source model weights. | Acceleration of physics simulations and model embeddings using sponsor infrastructure. | **Compute Credits & Hardware** |

---

## 💡 The Flagship Project Concept: `SpectraBond-AI`

### *Autonomous Multimodal Characterization & Inverse Synthesis Intelligence Grounded in 44.5M Papers via Valency MCP with Physics-Calibrated Verification*

```
                 ┌─────────────────────────────────────────────────────────────┐
                 │                 USER INPUT VIA MARIMO STUDIO                │
                 │  - Experimental Spectrum (XRD/Raman/FTIR CSV or Image)      │
                 │  - Target Material Formula / Desired Functional Property    │
                 └──────────────────────────────┬──────────────────────────────┘
                                                │
                                                ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
 │                                   AGENTIC CORE ENGINE                                       │
 │                                                                                             │
 │   ┌─────────────────────────────┐                    ┌──────────────────────────────────┐   │
 │   │  1. Signal & Vision Engine  │                    │      2. Valency MCP Bond Engine  │   │
 │   │  - Voigt / Lorentzian Fit   │                    │  - Queries 44.5M Papers          │   │
 │   │  - Peak Deconvolution       │◄──────────────────►│  - Precedent Synthesis Mining    │   │
 │   │  - d-spacing / Mode Match   │                    │  - Precursor Safety & Yields     │   │
 │   └──────────────┬──────────────┘                    └─────────────────┬────────────────┘   │
 │                  │                                                     │                    │
 │                  └───────────────────────┬─────────────────────────────┘                    │
 │                                          ▼                                                  │
 │                      ┌───────────────────────────────────────┐                              │
 │                      │      3. Physics Validation Engine     │                              │
 │                      │  - PyMatGen / Materials Project API   │                              │
 │                      │  - XRDCalculator / SpaceGroup Verify  │                              │
 │                      │  - RDKit Molecular Topology Check     │                              │
 │                      └───────────────────┬───────────────────┘                              │
 │                                          │                                                  │
 │                                          ▼                                                  │
 │                      ┌───────────────────────────────────────┐                              │
 │                      │ 4. Compound Confidence Calibration    │                              │
 │                      │    C_compound = C_sig × C_lit × C_phy │                              │
 │                      │  - Risk-Coverage Optimization (AURC)  │                              │
 │                      │  - Hallucination & Failure Guardrail  │                              │
 │                      └───────────────────┬───────────────────┘                              │
 └──────────────────────────────────────────┼──────────────────────────────────────────────────┘
                                            │
                                            ▼
 ┌─────────────────────────────────────────────────────────────────────────────────────────────┐
 │                                INTERACTIVE MARIMO OUTPUT                                    │
 │  - Reactive Plotly Overlays: Experimental vs. Simulated Physics Diffraction Patterns         │
 │  - Step-by-Step Executable Synthesis Protocol with Real DOI Citations from Valency          │
 │  - Calibrated Confidence Gauge (High / Medium / Alert) with Failure Attribution Map         │
 │  - One-Click 1-Page Summary & Laboratory Protocol PDF Export                                │
 └─────────────────────────────────────────────────────────────────────────────────────────────┘
```

### The Problem It Solves
1. **The Experimental Characterization Gap:** When experimental scientists synthesize a novel crystal or battery material and take an XRD (X-ray diffraction) or Raman spectrum, analyzing heterogeneous, noisy peak curves and matching them against crystallographic databases takes hours of manual, subjective fitting.
2. **The LLM Hallucination Trap:** Pure LLMs hallucinate crystal space groups, peak angles ($2\theta$), and synthesis temperatures that violate thermodynamics.
3. **The Literature Isolation Problem:** Most automated tools only simulate ideal crystals or search a closed database; they fail to cross-reference the messy realities of synthesis reported across millions of papers (precursor purity, calcination atmosphere, dopant limits).

### Why `SpectraBond-AI` Wins
- **Real-Time Literature Grounding:** Powered by **Valency MCP Bond**, it doesn't just guess; it cross-references 44.5M papers to find exact matching synthesis routes and experimental peaks.
- **Physical Grounding:** Uses `pymatgen` and the Materials Project API (`MPRester`) to calculate *ground-truth* physical diffraction patterns and lattice constants.
- **Tushar's Secret Weapon (Compound Confidence Calibration):** Incorporates your proven research method: calculating a calibrated compound confidence metric ($C_{\text{compound}} = C_{\text{signal}} \times C_{\text{literature}} \times C_{\text{physics}}$), filtering out hallucinated recipes before an experimentalist wastes lab funds!
- **Pure Reactive UX (Marimo):** A stunning, responsive UI built natively in Python with zero JavaScript build headaches, qualifying for the Marimo sponsor prize.

---

## 🔬 Alternative Winning Concepts (If You Want to Pivot)

While `SpectraBond-AI` is the recommended top choice, here are two alternative directions that also fit your skill set:

### Option B: `Q-MatAgent` (Quantum Materials & Hamiltonian Discovery Agent)
- **Domain:** Physical Sciences & Quantum Information (newly expanded in 2026).
- **Core Idea:** An agent that ingests candidate 2D materials (graphene, transition metal dichalcogenides) from the Materials Project, utilizes PennyLane/PySCF to generate parameterized quantum circuits (VQC and Quantum Kernel Hamiltonians), and queries Valency MCP for experimental topological insulator / superconductor papers.
- **Pros:** Directly leverages your ongoing PennyLane research.
- **Cons:** Quantum simulations can be computationally heavy to demo live in 4 minutes; harder to produce tangible physical laboratory plots than XRD/Raman.

### Option C: `MathPhys-ODE` (Autonomous Symbolic PDE / Kinetics Discovery Studio)
- **Domain:** Mathematics & Chemical Kinetics.
- **Core Idea:** An agent that takes time-series concentration/reaction curves, uses symbolic regression (SymPy) and LLM reasoning to discover the underlying differential equations of complex reaction mechanisms, validated against Valency literature citations.
- **Pros:** High mathematical rigor.
- **Cons:** Less visual punch than crystallographic/molecular spectra.

---

## 🛠️ Complete Technical Architecture & Stack

### 1. Literature & Knowledge Layer (Valency MCP Bond)
- **Integration:** Valency MCP endpoint or Bearer token API.
- **Capabilities:**
  - Search semantic literature queries (e.g., *"solid-state synthesis of Li7La3Zr2O12 garnet electrolyte"*).
  - Extract exact precursor ratios, sintering temperatures, and XRD diffraction $2\theta$ reference peaks.
  - Fetch verified DOIs and author metadata for transparent citation cards.

### 2. Physical & Simulation Layer (Python Scientific Stack)
- **`pymatgen`:** `pymatgen.analysis.diffraction.xrd.XRDCalculator` for simulating diffraction patterns from CIF files.
- **`mp-api`:** Querying Materials Project structures and stable phases.
- **`scipy.signal` & `lmfit`:** Voigt and Pseudo-Voigt peak deconvolution with baseline removal (Asymmetric Least Squares).
- **`rdkit`:** Chemical sanitization, SMILES processing, and molecular descriptor validation.

### 3. Agent Orchestration Layer
- **Framework:** Lightweight state-machine agent using Python / LangChain / LiteLLM.
- **Models:** Gemini 2.5 / Claude 3.5 / OpenAI / Mistral.
- **Confidence Scoring:**
  $$C_{\text{compound}} = C_{\text{peak\_fit}} \times C_{\text{valency\_support}} \times C_{\text{physics\_match}}$$
  - $C_{\text{peak\_fit}}$: Goodness of fit ($R^2$ or normalized residual) of experimental peaks.
  - $C_{\text{valency\_support}}$: Citation consensus score from Valency MCP literature.
  - $C_{\text{physics\_match}}$: Cosine similarity between experimental and pymatgen-simulated peak vectors.

### 4. Interactive Studio Layer (Marimo)
- **Framework:** `marimo` (Reactive Python web app & notebook).
- **Visuals:** Plotly interactive charts (zoomable $2\theta$ diffraction curves, peak markers, Bragg bar indicators), real-time parameter sliders, markdown report generation.

---

## ⏱️ 36-Hour Solo Execution Plan (Hour-by-Hour)

```
 [Oct 21: Day 1]
 ├── H 00-04: Setup & Boilerplate (Valency MCP, Marimo, PyMatGen)
 ├── H 04-10: Signal Processing & Physical Simulation Engine
 ├── H 10-16: Valency MCP Bond Agent & Synthesis Recipe Miner
 └── H 16-20: Compound Confidence Calibration & Error Attribution
 [Oct 22: Day 2]
 ├── H 20-26: Marimo Reactive Studio UI & Plotly Dashboards
 ├── H 26-30: End-to-End Validation Runs (Lithium Battery Cathode & Perovskite)
 ├── H 30-34: 4-Minute Submission Video & One-Page Figure
 └── H 34-36: GitHub Repository Polish, README, and Social Submission
```

### Phase 1: Environment & Sponsor Connectors (Hours 0–4)
1. Initialize the repo structure:
   ```
   Open-Scientific-Intelligence-Hackathon-2026/
   ├── app.py                  # Main Marimo reactive studio application
   ├── core/
   │   ├── signal_engine.py    # Peak detection, Voigt fitting, background subtraction
   │   ├── physics_engine.py   # PyMatGen XRDCalculator & Materials Project client
   │   ├── valency_client.py   # Valency MCP Bond literature retriever
   │   ├── agent.py            # Synthesis planner & cross-validator
   │   └── calibration.py      # Compound confidence calculation
   ├── data/
   │   └── sample_spectra/     # 3 pre-loaded benchmark datasets (LCO, LFP, Perovskite)
   ├── assets/                 # Architecture diagram & submission figures
   ├── requirements.txt
   └── README.md
   ```
2. Install dependencies:
   ```bash
   pip install marimo pymatgen mp-api scipy plotly requests pydantic
   ```
3. Test Valency Bond MCP connection using your bearer token.

### Phase 2: Core Physics & Signal Processing (Hours 4–10)
1. Implement `signal_engine.py`:
   - Load raw 2-column CSV ($2\theta$ angle vs. intensity).
   - Apply Savitzky-Golay filtering and rolling baseline subtraction.
   - Detect peaks using `scipy.signal.find_peaks` with prominence thresholds.
   - Fit top peaks with Pseudo-Voigt profiles to extract center, FWHM, and intensity.
2. Implement `physics_engine.py`:
   - Query candidate crystal structures from Materials Project via formula.
   - Use `pymatgen.analysis.diffraction.xrd.XRDCalculator(wavelength='CuKa')` to generate simulated $(2\theta, I)$ peaks with HKL indices.
   - Compute spectrum correlation metric (cosine similarity between experimental and theoretical spectra).

### Phase 3: Valency MCP Literature Synthesis Agent (Hours 10–16)
1. Implement `valency_client.py`:
   - Query Valency Bond for papers matching the target phase (e.g., *"synthesis procedure of LiCoO2 solid state reaction sintering temperature"*).
   - Parse top paper abstracts, extract precursors (e.g., $\text{Li}_2\text{CO}_3 + \text{Co}_3\text{O}_4$), calcination temperature ($800^\circ\text{C}$–$900^\circ\text{C}$), dwell time, and reported characterization peaks.
2. Implement `agent.py`:
   - Synthesizes the experimental findings, literature recipes, and physical constraints into a unified, step-by-step laboratory synthesis card.

### Phase 4: Compound Confidence Calibration (Hours 16–20)
1. Implement `calibration.py`:
   - Combine peak fit quality, literature consensus count, and physics correlation into $C_{\text{compound}} \in [0.0, 1.0]$.
   - Output confidence badges: `🟢 High Confidence (>0.85)`, `🟡 Moderate / Needs Verification (0.65-0.85)`, `🔴 Risk of Phase Impurity (<0.65)`.
   - Highlight potential unreacted precursor peaks (e.g., unreacted $\text{Co}_3\text{O}_4$ trace peaks).

### Phase 5: Marimo Reactive Studio UI (Hours 20–26)
1. Implement `app.py` in Marimo:
   - Header with hackathon badge and sponsor tags (Valency MCP + Marimo).
   - File upload button for experimental spectrum CSV (with 3 quick-load buttons for instant demo: *"LiCoO2 Battery Cathode"*, *"MAPbI3 Perovskite"*, *"BaTiO3 Ferroelectric"*).
   - Reactive Plotly chart: Dual-trace interactive visualization showing Experimental Curve vs. PyMatGen Simulated Peaks vs. Identified Phase Peaks.
   - Live Valency Paper Cards with direct links, DOI, and extracted synthesis parameters.
   - One-click "Export Discovery Report" (Markdown / HTML).

### Phase 6: Benchmark Demonstrations & Testing (Hours 26–30)
1. Run 3 complete case studies through the pipeline:
   - **Case Study 1 (Clean match):** $\text{LiCoO}_2$ cathode material — demonstrates exact phase identification and optimal synthesis.
   - **Case Study 2 (Impurity detection):** $\text{BaTiO}_3$ with residual $\text{TiO}_2$ unreacted phase — demonstrates the compound confidence calibration catching the impurity!
   - **Case Study 3 (Inverse discovery):** Inputting a desired high-entropy alloy or perovskite formula and letting the agent retrieve the recipe from 44.5M papers and simulate its diffraction pattern.

### Phase 7: Video Recording & 1-Page Summary (Hours 30–34)
- **Video (Under 4 minutes):**
  - *0:00 - 0:45:* The problem in experimental materials science (manual peak analysis & literature fragmentation).
  - *0:45 - 1:45:* Architecture walkthrough (Multimodal Signal Engine + Valency MCP 44.5M Papers + PyMatGen Physics).
  - *1:45 - 3:00:* Live Marimo demo! Uploading a real spectrum, seeing reactive peak deconvolution, querying Valency, displaying calibrated confidence score.
  - *3:00 - 3:45:* Impurity detection demonstration and one-click synthesis protocol generation.
  - *3:45 - 4:00:* Conclusion, sponsor acknowledgment (Valency & Marimo), open-source link.
- **1-Page Summary Document:** Create `summary.pdf` with the system architecture diagram and experimental vs. simulated benchmark plots.

### Phase 8: Submission & Social Launch (Hours 34–36)
- Upload code to clean GitHub repository with MIT license.
- Upload video to YouTube (unlisted or public) or Loom.
- Publish post on LinkedIn / X (Twitter) tagging `#OSIHackathon #Valency #Marimo #MDRI`.
- Submit the official Luma submission form before the deadline (Thu Oct 22, 7 PM CT).

---

## 📋 Hackathon Deliverables Checklist

- [ ] **Working Code Repository:** Open-source GitHub repo with clean commit history, `README.md`, setup instructions, and sample datasets.
- [ ] **4-Minute Demo Video:** High-resolution screen recording showing the working Marimo UI and agent workflow without audio speedup.
- [ ] **1-Page Project Summary:** Written PDF document including:
  - Project Title & Abstract
  - Team Info (Solo participant: Tushar Bhardwaj, NIT Kurukshetra)
  - Architectural Flowchart
  - Benchmark Results & Validation
  - Valency MCP & Marimo integration highlights
- [ ] **Public Post Link:** Public LinkedIn post or X thread summarizing the project and linking to the GitHub repo and demo video.
- [ ] **Official Submission Form:** Submitted on time with all required links.

---

## 🙋 Critical Clarifications & Next Steps

To personalize this further before the sprint begins tomorrow, please review the questions below:
1. **API Keys & Accounts:** Do you have access to a Valency API key / Bearer token, and your preferred LLM API key (e.g., Gemini API, OpenAI, or Claude)?
2. **Domain Focus:** Does the **Materials & Battery / Energy Materials** focus (XRD/Raman + Pymatgen + Valency) excite you most, or do you prefer leaning toward **Quantum Materials (PennyLane)** or **Chemical Drug Discovery (RDKit)**?
3. **Execution Ready:** Would you like us to generate the foundational scaffold code (`signal_engine.py`, `valency_client.py`, `physics_engine.py`, and `app.py`) right now in this workspace so you are 100% prepared when the hackathon kicks off?
