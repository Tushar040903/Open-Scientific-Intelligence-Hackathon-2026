import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set up 16:9 canvas at high resolution
fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis("off")

# 1. Dark Futuristic Gradient Background
fig.patch.set_facecolor('#0B0F19')
ax.set_facecolor('#0B0F19')

# Subtle background decorative grid lines
for x in np.linspace(0, 16, 33):
    ax.axvline(x, color='#1E293B', lw=0.5, alpha=0.3)
for y in np.linspace(0, 9, 19):
    ax.axhline(y, color='#1E293B', lw=0.5, alpha=0.3)

# 2. Glowing Mathematical / Spectroscopic Waves in Background
x_vals = np.linspace(0, 16, 1000)
# Sine wave superposition simulating diffraction spectra
y_wave1 = 2.2 + 0.9 * np.sin(1.2 * x_vals) * np.exp(-((x_vals - 8)**2) / 25) + 0.4 * np.sin(3.5 * x_vals)
y_wave2 = 2.4 + 1.2 * np.sin(1.1 * x_vals + 0.5) * np.exp(-((x_vals - 8)**2) / 20) + 0.5 * np.sin(4.0 * x_vals)

ax.plot(x_vals, y_wave1, color='#06B6D4', lw=2.5, alpha=0.8, zorder=2)
ax.plot(x_vals, y_wave2, color='#6366F1', lw=3.0, alpha=0.9, zorder=3)
ax.fill_between(x_vals, y_wave1, 0, color='#06B6D4', alpha=0.08, zorder=1)
ax.fill_between(x_vals, y_wave2, 0, color='#6366F1', alpha=0.06, zorder=1)

# Bragg reflection sticks
peaks_x = [3.5, 5.2, 7.8, 9.4, 11.6, 13.2]
peaks_h = [4.5, 3.8, 5.8, 4.2, 5.0, 3.6]
for px, ph in zip(peaks_x, peaks_h):
    ax.vlines(px, ymin=1.8, ymax=ph, color='#10B981', lw=2.5, alpha=0.85, zorder=4)
    ax.scatter(px, ph, color='#34D399', s=60, zorder=5)

# 3. Main Center Card / Header
# Glowing pill for event
pill = patches.FancyBboxPatch((4.2, 7.5), 7.6, 0.65, boxstyle="round,pad=0.2",
                             fc='#1E1B4B', ec='#6366F1', lw=1.5, zorder=5)
ax.add_patch(pill)
ax.text(8.0, 7.82, "4th ANNUAL OPEN SCIENTIFIC INTELLIGENCE HACKATHON 2026",
        ha='center', va='center', fontsize=11, fontweight='bold', color='#A5B4FC', zorder=6)

# Main Title
ax.text(8.0, 6.4, "SPECTRA-BOND AI", 
        ha='center', va='center', fontsize=38, fontweight='black', color='#FFFFFF', zorder=6)

# Subtitle
ax.text(8.0, 5.5, "Autonomous Multimodal Characterization & Inverse Synthesis Intelligence",
        ha='center', va='center', fontsize=16, fontweight='bold', color='#38BDF8', zorder=6)

# Descriptive Pitch
ax.text(8.0, 4.85, "Bridging Raw Spectroscopic Data to Executable Laboratory Synthesis via Valency MCP & Crystallographic Physics",
        ha='center', va='center', fontsize=12, color='#94A3B8', style='italic', zorder=6)

# 4. Feature Badges at Bottom
badges = [
    ("Valency MCP Bond", "Grounded in 44.5M Papers", "#8B5CF6", 2.2),
    ("Space-Group Physics", "Bragg Extinction & Law", "#10B981", 6.0),
    ("Compound Calibration", "Catches Trace Impurities", "#EF4444", 9.8),
    ("Reactive Studio", "Built on Marimo Platform", "#0284C7", 13.6),
]

for title, sub, color, cx in badges:
    b_box = patches.FancyBboxPatch((cx - 1.6, 0.7), 3.2, 0.95, boxstyle="round,pad=0.15",
                                  fc='#0F172A', ec=color, lw=1.8, zorder=5)
    ax.add_patch(b_box)
    ax.text(cx, 1.25, title, ha='center', va='center', fontsize=10, fontweight='bold', color='#FFFFFF', zorder=6)
    ax.text(cx, 0.92, sub, ha='center', va='center', fontsize=8, color='#94A3B8', zorder=6)

plt.tight_layout()
fig.savefig("assets/cover_image.png", bbox_inches='tight', dpi=300)
plt.close(fig)
print("Saved assets/cover_image.png")
