SpectraBond-AI is an autonomous closed-loop intelligence system built on the reactive Marimo platform that bridges raw experimental materials characterization with actionable laboratory synthesis. By unifying mathematical signal deconvolution, crystallographic space-group physics, and real-time literature grounding across 44.5 million research papers via Valency MCP Bond, the system eliminates LLM hallucinations and autonomously isolates parasitic trace phase impurities before expensive experimental runs are conducted.

### 1. What We Built
In solid-state chemistry and materials discovery, researchers routinely collect X-ray diffraction (XRD) and spectroscopic measurements. However, converting these noisy, overlapping curves into validated crystal structures and reproducible synthesis protocols has traditionally required hours of manual curve-fitting and literature search. Standard LLMs frequently hallucinate non-physical Bragg peak angles and violate space group symmetry. 

To solve this, we built **SpectraBond-AI**—an end-to-end "planning-to-action" system designed for both computational and experimental physical scientists. It accepts raw experimental spectra, mathematically deconvolves reflections, validates the pattern against theoretical space groups, retrieves verified precursor recipes from peer-reviewed literature, and scores the result using a calibrated compound confidence metric.

### 2. How It Works
The architecture couples knowledge infrastructure directly to physical action through four modular components:

1. **Signal & Deconvolution Engine:** Performs Savitzky-Golay baseline subtraction and fits Pseudo-Voigt profiles to extract peak centers ($2\theta$), full-width at half-maximum ($\beta$), and interplanar lattice $d$-spacing via Bragg's Law:
   $$\lambda = 2d \sin\theta \implies d = \frac{\lambda}{2\sin\theta}$$
   Crystallite domain sizes ($\tau$) are calculated via the Scherrer equation:
   $$\tau = \frac{K \lambda}{\beta \cos\theta}$$
2. **Crystallographic Physics Engine:** Computes theoretical Bragg reflection sticks and validates experimental peak positions against space group symmetries (e.g., $R\bar{3}m$, $P4mm$, $I4/mcm$) with configurable angular tolerance ($\Delta 2\theta$).
3. **Valency MCP Bond Literature Engine:** Connects via the Model Context Protocol to 44.5 million research papers (spanning arXiv, PubMed, ChemRxiv, and CrossRef) to extract empirical precursors, stoichiometric ratios, calcination temperatures, dwell times, and verified DOIs.
4. **Compound Confidence Calibration:** Implements a compound confidence framework with risk-coverage trade-offs:
   $$C_{\text{compound}} = C_{\text{sig}} \times C_{\text{phys}} \times C_{\text{lit}}$$
   where $C_{\text{sig}}$ evaluates signal-to-noise and peak sharpness, $C_{\text{phys}}$ assesses Bragg angular precision and reflection recall, and $C_{\text{lit}}$ measures peer-reviewed precedent consensus.

### 3. What We Found & Benchmark Results
We validated SpectraBond-AI across multiple benchmark energy and electronic materials:
- **Single-Phase Battery Cathode ($\text{LiCoO}_2$):** Successfully detected all 8 major reflections, matching theoretical $R\bar{3}m$ symmetry with a mean angular delta of $\Delta 2\theta = 0.020^\circ$. The system achieved a **`84.8%` High Confidence score ($C_{\text{compound}} = 0.848$)** and extracted the optimal solid-state calcination protocol ($850^\circ\text{C}$ for 12h in $\text{O}_2$) with peer-reviewed citations.
- **Trace Impurity Detection ($\text{BaTiO}_3$ with unreacted $\text{TiO}_2$):** In a simulated incomplete solid-state reaction, the system successfully matched the primary tetragonal perovskite phase while isolating an unexplained reflection at $2\theta = 25.31^\circ$. It cross-matched this reflection to unreacted Anatase $\text{TiO}_2$ (101), penalized the compound confidence to **`59.9%` (Impurity Alert)**, and issued an automated laboratory directive to increase the calcination temperature by $+50^\circ\text{C}$ to complete phase conversion.

### 4. Implementation & Availability
SpectraBond-AI is fully open-source and built using `marimo`, `scipy`, `numpy`, and `plotly`. The interactive discovery studio is launchable with a single command (`marimo run app.py`), providing reactive dual-trace plots, parameter sliders, and one-click synthesis protocol exports.

- **GitHub Repository:** [https://github.com/Tushar040903/Open-Scientific-Intelligence-Hackathon-2026](https://github.com/Tushar040903/Open-Scientific-Intelligence-Hackathon-2026)  
- **Team / Developer:** Tushar Bhardwaj (Solo Competitor, National Institute of Technology Kurukshetra)
