import pymupdf

html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    font-family: Helvetica, Arial, sans-serif;
    color: #1E293B;
    line-height: 1.5;
    font-size: 11pt;
  }
  .header-card {
    background-color: #0F172A;
    color: #FFFFFF;
    padding: 18px 20px;
    border-radius: 8px;
    margin-bottom: 20px;
  }
  .title {
    font-size: 18pt;
    font-weight: bold;
    color: #38BDF8;
    margin: 0 0 6px 0;
  }
  .subtitle {
    font-size: 11pt;
    color: #94A3B8;
    margin: 0 0 10px 0;
  }
  .meta-tag {
    display: inline-block;
    background-color: #1E293B;
    color: #F8FAFC;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 8.5pt;
    font-weight: bold;
    margin-right: 6px;
    border: 1px solid #334155;
  }
  .scene-card {
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 16px;
    background-color: #FFFFFF;
  }
  .scene-header {
    border-bottom: 2px solid #E2E8F0;
    padding-bottom: 6px;
    margin-bottom: 10px;
  }
  .scene-title {
    font-size: 13pt;
    font-weight: bold;
    color: #0F172A;
    margin: 0;
  }
  .scene-timing {
    float: right;
    background-color: #DBEAFE;
    color: #1E40AF;
    font-weight: bold;
    font-size: 9pt;
    padding: 3px 8px;
    border-radius: 12px;
  }
  .action-box {
    background-color: #F8FAFC;
    border-left: 4px solid #3B82F6;
    padding: 8px 12px;
    margin-bottom: 10px;
    font-size: 9.5pt;
    color: #334155;
  }
  .action-title {
    font-weight: bold;
    color: #1D4ED8;
    text-transform: uppercase;
    font-size: 8pt;
    margin-bottom: 3px;
  }
  .speech-box {
    background-color: #EFF6FF;
    border: 1px solid #BFDBFE;
    border-radius: 6px;
    padding: 12px 14px;
    margin-bottom: 10px;
  }
  .speech-title {
    font-weight: bold;
    color: #1E3A8A;
    font-size: 8.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
  }
  .speech-text {
    font-size: 11.5pt;
    font-weight: bold;
    color: #0F172A;
    line-height: 1.55;
  }
  .tip-box {
    background-color: #FEF3C7;
    border-left: 4px solid #F59E0B;
    padding: 6px 10px;
    font-size: 8.5pt;
    color: #92400E;
    font-style: italic;
  }
  .checklist {
    background-color: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-radius: 6px;
    padding: 12px 16px;
    margin-top: 15px;
  }
  .checklist-title {
    font-size: 11pt;
    font-weight: bold;
    color: #166534;
    margin-top: 0;
    margin-bottom: 6px;
  }
</style>
</head>
<body>

<div class="header-card">
  <div class="title">🎬 SpectraBond-AI: Video Demo Script</div>
  <div class="subtitle">4th Annual Open Scientific Intelligence Hackathon (MDRI / UL Research Institutes)</div>
  <div>
    <span class="meta-tag">Target Duration: 3 min 20 sec</span>
    <span class="meta-tag">Presenter: Tushar Bhardwaj (Solo)</span>
    <span class="meta-tag">Platform: Marimo (localhost:2718)</span>
  </div>
</div>

<!-- SCENE 1 -->
<div class="scene-card">
  <div class="scene-header">
    <span class="scene-timing">0:00 – 0:35 (35s)</span>
    <div class="scene-title">SCENE 1: The Hook & The Problem</div>
  </div>
  <div class="action-box">
    <div class="action-title">🎥 Screen Action</div>
    Keep browser fullscreen at the very top. Show title banner, badges, and preset dropdown. Slowly hover cursor across the title.
  </div>
  <div class="speech-box">
    <div class="speech-title">🎙️ What to Say (Word-for-Word)</div>
    <div class="speech-text">
      "Hello judges! My name is Tushar Bhardwaj, participating solo in the 4th Annual Open Scientific Intelligence Hackathon. Today, I am thrilled to present SpectraBond-AI: an autonomous multimodal characterization and inverse synthesis intelligence deployed natively on the reactive Marimo platform.<br><br>
      In solid-state chemistry and materials discovery, converting raw XRD and spectroscopic detector scans into verified crystal phases takes hours of manual, subjective peak-fitting. Worse, generic LLMs suffer from severe hallucinations—inventing non-physical Bragg peak angles and violating crystal space-group symmetries.<br><br>
      SpectraBond-AI solves this by bridging mathematical signal deconvolution with two grounded pillars: crystallographic physics simulation and real-time literature retrieval across 44.5 million papers via Valency MCP Bond."
    </div>
  </div>
  <div class="tip-box">
    💡 <b>Director's Tip:</b> Speak with steady, confident energy. Keep your cursor smooth.
  </div>
</div>

<!-- SCENE 2 -->
<div class="scene-card">
  <div class="scene-header">
    <span class="scene-timing">0:35 – 1:25 (50s)</span>
    <div class="scene-title">SCENE 2: Benchmark 1 — Clean Battery Cathode (LiCoO2)</div>
  </div>
  <div class="action-box">
    <div class="action-title">🎥 Screen Action</div>
    1. Keep default preset selected (LiCoO2).<br>
    2. Scroll down to show the Compound Confidence Calibration Scorecard.<br>
    3. Scroll down to the Plotly chart: point out the blue curve, baseline dashed line, and hover over a red peak marker to show the tooltip (2θ, d-spacing, crystallite size τ).<br>
    4. Point to the green theoretical Bragg reflection bars on the bottom graph.
  </div>
  <div class="speech-box">
    <div class="speech-title">🎙️ What to Say (Word-for-Word)</div>
    <div class="speech-text">
      "Let’s test our first benchmark: an experimental XRD scan of a commercial Lithium Cobalt Oxide (LiCoO2) high-rate battery cathode.<br><br>
      Instantly, our system outputs a calibrated compound confidence score: 84.8% High Confidence. Notice our mathematical formulation: C_compound = C_sig × C_phys × C_lit, ensuring every prediction is grounded across signal quality, physical symmetry, and published literature.<br><br>
      Here in the top chart, our Signal Engine applies Savitzky-Golay baseline subtraction and fits Pseudo-Voigt profiles to isolate genuine diffraction peaks from background detector noise. When I hover over a peak, you can see the Bragg reflection angle, the interplanar lattice d-spacing calculated via Bragg’s Law, and the crystallite domain size via the Scherrer equation.<br><br>
      On the bottom panel, our Physics Engine simulates the theoretical Bragg sticks for space group R-3m. All 8 reflections match perfectly with a mean angular deviation of just 0.020 degrees!"
    </div>
  </div>
  <div class="tip-box">
    💡 <b>Director's Tip:</b> Hovering over the peak to show the live tooltip proves this is an active mathematical engine, not a static mockup.
  </div>
</div>

<!-- SCENE 3 -->
<div class="scene-card">
  <div class="scene-header">
    <span class="scene-timing">1:25 – 2:20 (55s)</span>
    <div class="scene-title">SCENE 3: The Climax — Catching Trace Impurities (BaTiO3)</div>
  </div>
  <div class="action-box">
    <div class="action-title">🎥 Screen Action</div>
    1. Scroll back up to the Preset Dropdown and select: <b>BaTiO3 — Ferroelectric Perovskite (Contains TiO2 Unreacted Impurity)</b>.<br>
    2. Watch the dashboard reactively update in under 1 second.<br>
    3. Scroll down to the Plotly chart and point your cursor directly at the <b>RED vertical dashed line at 25.3° labeled ⚠️ Impurity</b>.<br>
    4. Scroll up slightly to point at the yellow alert banner and confidence scorecard.
  </div>
  <div class="speech-box">
    <div class="speech-title">🎙️ What to Say (Word-for-Word)</div>
    <div class="speech-text">
      "Now, let's examine the key failure mode in materials chemistry: incomplete solid-state reactions that leave trace unreacted precursors. Standard LLMs completely miss trace peaks and mistakenly declare the sample pure. Let's see what SpectraBond-AI does.<br><br>
      Thanks to Marimo’s reactive state execution, the entire pipeline re-computes with zero latency.<br><br>
      Look right here at 2θ = 25.31 degrees. Our system flags a prominent red marker labeled 'Impurity'. While the primary reflections match Barium Titanate, this lone reflection is an anomaly.<br><br>
      Instead of hallucinating, our failure attribution engine identifies this peak as the (101) reflection of unreacted Anatase TiO2 precursor! It immediately penalizes our compound confidence down to 59.9% Impurity Alert, and automatically outputs a laboratory directive: 'Secondary phase present. Increase sintering temperature by +50°C or extend dwell time to complete solid-state conversion.' This directly saves experimentalists days of wasted lab work!"
    </div>
  </div>
  <div class="tip-box">
    💡 <b>Director's Tip:</b> This is the winning scientific moment of your presentation. Speak with excitement!
  </div>
</div>

<!-- SCENE 4 -->
<div class="scene-card">
  <div class="scene-header">
    <span class="scene-timing">2:20 – 3:00 (40s)</span>
    <div class="scene-title">SCENE 4: Grounding in 44.5M Papers & Executable Lab Card</div>
  </div>
  <div class="action-box">
    <div class="action-title">🎥 Screen Action</div>
    1. Click on the <b>📊 Deconvolved Peak Parameter Table</b> accordion to expand it.<br>
    2. Scroll down to the bottom tabs and click <b>📚 Valency Literature Citations</b>.<br>
    3. Scroll through the paper citations showing the real DOIs.<br>
    4. Click the first tab: <b>⚗️ Executable Synthesis Card</b> to show the precursor list and heating schedule.
  </div>
  <div class="speech-box">
    <div class="speech-title">🎙️ What to Say (Word-for-Word)</div>
    <div class="speech-text">
      "For crystallographers, every single deconvolved peak is tabulated with exact d-spacings, full-width at half-maximum, and Scherrer domain sizes.<br><br>
      Next, we ground our findings in peer-reviewed literature. By connecting via the Model Context Protocol to Valency Bond MCP, our agent queries 44.5 million research papers across PubMed, arXiv, and CrossRef. Here you can see empirical papers from Acta Materialia and Nature Materials with clickable, verified DOIs.<br><br>
      Finally, our agent translates this into an actionable synthesis card: exact precursor stoichiometric masses, heating ramp rates, calcination plateaus, and safety guardrails."
    </div>
  </div>
  <div class="tip-box">
    💡 <b>Director's Tip:</b> Switching between the tabs visually reinforces that you built a complete end-to-end product.
  </div>
</div>

<!-- SCENE 5 -->
<div class="scene-card">
  <div class="scene-header">
    <span class="scene-timing">3:00 – 3:25 (25s)</span>
    <div class="scene-title">SCENE 5: Conclusion & Sponsor Acknowledgments</div>
  </div>
  <div class="action-box">
    <div class="action-title">🎥 Screen Action</div>
    Scroll smoothly back to the top of the app, showing the SpectraBond-AI header.
  </div>
  <div class="speech-box">
    <div class="speech-title">🎙️ What to Say (Word-for-Word)</div>
    <div class="speech-text">
      "To summarize, SpectraBond-AI bridges knowledge infrastructure and action systems: automated signal deconvolution, space-group physics validation, real-time literature grounding via Valency MCP, and reactive deployment on Marimo.<br><br>
      The entire pipeline is open-source, reproducible in pure Python, and ready for deployment into autonomous self-driving labs. Thank you to the Materials Discovery Research Institute, Valency, and Marimo for hosting this incredible hackathon!"
    </div>
  </div>
</div>

<div class="checklist">
  <div class="checklist-title">📋 Pre-Recording Quick Checklist</div>
  • Browser at 100% or 110% zoom at http://localhost:2718<br>
  • Open this PDF on your phone screen<br>
  • Hit Win + Alt + R to record screen and speak aloud<br>
  • Upload to YouTube as Public or Unlisted, and paste link into your submission form!
</div>

</body>
</html>
"""

pdf_path = "SpectraBond_AI_Video_Demo_Script.pdf"
writer = pymupdf.DocumentWriter(pdf_path)
page_rect = pymupdf.Rect(0, 0, 595, 842) # A4 page
story = pymupdf.Story(html=html_content)

while True:
    device = writer.begin_page(page_rect)
    more, _ = story.place(pymupdf.Rect(30, 30, 565, 812))
    story.draw(device)
    writer.end_page()
    if not more:
        break

writer.close()
doc = pymupdf.open(pdf_path)
print(f"Successfully generated {pdf_path} with {len(doc)} pages.")
