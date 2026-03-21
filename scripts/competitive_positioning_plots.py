"""
Generate competitive positioning visualizations for BL-005 blog post.

Data source: DSM Central competitive-positioning-map.md and competitive-landscape.md
Axes:
  X: Human Oversight (1=per-turn gating, 5=full autonomy)
  Y: Knowledge Provenance (1=pretrained only, 5=comprehensive curated)
  Z: Experience Accumulation (0=stateless, 5=distributed evolution)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path

# Output directory
OUT_DIR = Path(__file__).parent.parent / "static" / "images" / "blog" / "competitive-positioning"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# --- Data ---
data = pd.DataFrame([
    {"System": "DSM",                   "X": 1,   "Y": 5,   "Z": 5,   "Class": "DSM"},
    {"System": "autoresearch",          "X": 5,   "Y": 2,   "Z": 0.5, "Class": "Philosophical opposite"},
    {"System": "claude-sci-skills",     "X": 3,   "Y": 3,   "Z": 1,   "Class": "Complement"},
    {"System": "Cline / Roo Code",      "X": 1,   "Y": 3,   "Z": 1,   "Class": "Partial overlap"},
    {"System": "Cursor",                "X": 3,   "Y": 3,   "Z": 0.5, "Class": "Tool"},
    {"System": "Devin",                 "X": 4.5, "Y": 1,   "Z": 0,   "Class": "Philosophical opposite"},
    {"System": "Engage-META",           "X": 2.5, "Y": 4,   "Z": 2.5, "Class": "Complement"},
    {"System": "GSD",                   "X": 4,   "Y": 3.5, "Z": 1,   "Class": "Philosophical opposite"},
    {"System": "Kilo Code",             "X": 2,   "Y": 3.5, "Z": 2,   "Class": "Competitor (partial)"},
    {"System": "Kiro",                  "X": 2,   "Y": 3.5, "Z": 2,   "Class": "Competitor (partial)"},
    {"System": "BMAD",                  "X": 3,   "Y": 3,   "Z": 1,   "Class": "Competitor (partial)"},
    {"System": "OpenHands",             "X": 4.5, "Y": 1.5, "Z": 0,   "Class": "Philosophical opposite"},
    {"System": "Paperclip",             "X": 4.5, "Y": 2.5, "Z": 2,   "Class": "Orthogonal"},
    {"System": "Picobot",               "X": 4,   "Y": 3.5, "Z": 3,   "Class": "Complement"},
    {"System": "SPARC",                 "X": 2,   "Y": 3,   "Z": 1.5, "Class": "Competitor (partial)"},
])

# --- Color palette by classification ---
class_colors = {
    "DSM":                     "#E63946",  # red accent
    "Philosophical opposite":  "#457B9D",  # steel blue
    "Competitor (partial)":    "#F4A261",  # sandy orange
    "Complement":              "#2A9D8F",  # teal
    "Partial overlap":         "#E9C46A",  # gold
    "Orthogonal":              "#264653",  # dark teal
    "Tool":                    "#A8DADC",  # light blue
}

# Classifications present in the data (for legend)
CLASS_ORDER = ["DSM", "Philosophical opposite", "Competitor (partial)",
               "Complement", "Partial overlap", "Orthogonal", "Tool"]

# --- Shared style ---
sns.set_theme(style="whitegrid", font_scale=1.1)
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["figure.dpi"] = 150

# Marker size for all scatter plots
MARKER_SIZE = 110


def _add_classification_legend(ax, loc="lower left"):
    """Add a shared classification color legend to an axis."""
    legend_handles = [
        mpatches.Patch(color=class_colors[c], label=c)
        for c in CLASS_ORDER
    ]
    ax.legend(
        handles=legend_handles, title="Classification",
        loc=loc, fontsize=7.5, title_fontsize=8.5,
        framealpha=0.9,
    )


def _smart_labels(ax, df, xcol, ycol, offsets=None):
    """Add system name labels with manual offsets to avoid overlap."""
    if offsets is None:
        offsets = {}
    for _, row in df.iterrows():
        dx, dy = offsets.get(row["System"], (0.15, 0.1))
        fontweight = "bold" if row["System"] == "DSM" else "normal"
        fontsize = 10 if row["System"] == "DSM" else 8.5
        ax.annotate(
            row["System"],
            (row[xcol], row[ycol]),
            xytext=(row[xcol] + dx, row[ycol] + dy),
            fontsize=fontsize,
            fontweight=fontweight,
            color="#1d1d1d",
            zorder=4,
        )


def _scatter_points(ax, df, xcol, ycol):
    """Plot scatter points colored by classification."""
    for _, row in df.iterrows():
        color = class_colors[row["Class"]]
        ax.scatter(
            row[xcol], row[ycol],
            s=MARKER_SIZE,
            c=color,
            alpha=0.8,
            edgecolors="white",
            linewidth=1.2,
            zorder=3,
        )
    # Plot DSM again on top to ensure visibility
    dsm = df[df["System"] == "DSM"].iloc[0]
    ax.scatter(
        dsm[xcol], dsm[ycol],
        s=MARKER_SIZE * 1.6,
        c=class_colors["DSM"],
        alpha=0.95,
        edgecolors="#B71C2C",
        linewidth=2,
        zorder=5,
    )


def plot_xy_oversight_vs_provenance(data, out_path):
    """Plot 1: Human Oversight (X) vs Knowledge Provenance (Y)."""
    fig, ax = plt.subplots(figsize=(11, 8))

    _scatter_points(ax, data, "X", "Y")

    offsets = {
        "DSM":              (0.18, 0.12),
        "autoresearch":     (-0.15, 0.18),
        "claude-sci-skills": (0.18, -0.22),
        "Cline / Roo Code": (0.18, -0.28),
        "Cursor":           (0.18, 0.15),
        "Devin":            (0.18, 0.12),
        "Engage-META":      (0.18, 0.12),
        "GSD":              (0.18, 0.12),
        "Kilo Code":        (-1.1, 0.18),
        "Kiro":             (-0.65, -0.28),
        "BMAD":             (-0.55, 0.18),
        "OpenHands":        (0.18, 0.12),
        "Paperclip":        (0.18, -0.22),
        "Picobot":          (-0.1, -0.28),
        "SPARC":            (0.18, -0.22),
    }
    _smart_labels(ax, data, "X", "Y", offsets)

    ax.set_xlabel("Human Oversight Model\n(1 = per-turn gating    \u2192    5 = full autonomy)", fontsize=11)
    ax.set_ylabel("Knowledge Provenance\n(1 = pretrained only    \u2192    5 = comprehensive curated)", fontsize=11)
    ax.set_xlim(0.3, 5.7)
    ax.set_ylim(0.3, 5.7)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_title("Human Oversight vs. Knowledge Provenance", fontsize=14, fontweight="bold", pad=15)

    _add_classification_legend(ax, loc="lower left")

    plt.tight_layout()
    fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out_path}")


def plot_xz_oversight_vs_experience(data, out_path):
    """Plot 2: Human Oversight (X) vs Experience Accumulation (Z)."""
    fig, ax = plt.subplots(figsize=(11, 8))

    _scatter_points(ax, data, "X", "Z")

    offsets = {
        "DSM":              (0.18, 0.12),
        "autoresearch":     (-0.15, 0.15),
        "claude-sci-skills": (0.18, 0.12),
        "Cline / Roo Code": (0.18, -0.22),
        "Cursor":           (0.18, -0.25),
        "Devin":            (-0.6, 0.15),
        "Engage-META":      (0.18, 0.12),
        "GSD":              (0.18, -0.22),
        "Kilo Code":        (-1.1, 0.15),
        "Kiro":             (0.18, -0.25),
        "BMAD":             (-0.55, 0.15),
        "OpenHands":        (0.18, 0.12),
        "Paperclip":        (0.18, 0.12),
        "Picobot":          (0.18, 0.12),
        "SPARC":            (0.18, 0.12),
    }
    _smart_labels(ax, data, "X", "Z", offsets)

    ax.set_xlabel("Human Oversight Model\n(1 = per-turn gating    \u2192    5 = full autonomy)", fontsize=11)
    ax.set_ylabel("Experience Accumulation\n(0 = stateless    \u2192    5 = distributed evolution)", fontsize=11)
    ax.set_xlim(0.3, 5.7)
    ax.set_ylim(-0.7, 5.7)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([0, 1, 2, 3, 4, 5])
    ax.set_title("Human Oversight vs. Experience Accumulation", fontsize=14, fontweight="bold", pad=15)

    _add_classification_legend(ax, loc="upper right")

    plt.tight_layout()
    fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out_path}")


def plot_yz_provenance_vs_experience(data, out_path):
    """Plot 3: Knowledge Provenance (Y) vs Experience Accumulation (Z)."""
    fig, ax = plt.subplots(figsize=(11, 8))

    _scatter_points(ax, data, "Y", "Z")

    offsets = {
        "DSM":              (0.15, 0.12),
        "autoresearch":     (0.15, 0.12),
        "claude-sci-skills": (0.15, 0.12),
        "Cline / Roo Code": (-1.5, -0.22),
        "Cursor":           (0.15, -0.28),
        "Devin":            (0.15, 0.12),
        "Engage-META":      (0.15, 0.12),
        "GSD":              (0.15, -0.25),
        "Kilo Code":        (-1.1, 0.15),
        "Kiro":             (0.15, -0.28),
        "BMAD":             (-0.55, 0.15),
        "OpenHands":        (0.15, 0.12),
        "Paperclip":        (-1.1, -0.22),
        "Picobot":          (0.15, 0.12),
        "SPARC":            (-0.7, 0.15),
    }
    _smart_labels(ax, data, "Y", "Z", offsets)

    ax.set_xlabel("Knowledge Provenance\n(1 = pretrained only    \u2192    5 = comprehensive curated)", fontsize=11)
    ax.set_ylabel("Experience Accumulation\n(0 = stateless    \u2192    5 = distributed evolution)", fontsize=11)
    ax.set_xlim(0.3, 5.7)
    ax.set_ylim(-0.5, 5.7)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([0, 1, 2, 3, 4, 5])
    ax.set_title("Knowledge Provenance vs. Experience Accumulation", fontsize=14, fontweight="bold", pad=15)

    _add_classification_legend(ax, loc="lower right")

    plt.tight_layout()
    fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out_path}")


def plot_z_axis_bars(data, out_path):
    """Horizontal bar chart of Z (Experience Accumulation) scores, sorted."""
    fig, ax = plt.subplots(figsize=(10, 7))

    sorted_data = data.sort_values("Z", ascending=True)
    colors = [class_colors[c] for c in sorted_data["Class"]]

    bars = ax.barh(
        sorted_data["System"], sorted_data["Z"],
        color=colors, edgecolor="white", linewidth=0.8, height=0.7
    )

    # Highlight DSM bar
    for bar, system in zip(bars, sorted_data["System"]):
        if system == "DSM":
            bar.set_edgecolor("#E63946")
            bar.set_linewidth(2.5)

    ax.set_xlabel("Experience Accumulation Level", fontsize=11)
    ax.set_title("Experience Accumulation Depth by System", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlim(0, 5.5)
    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels([
        "0\nStateless", "1\nSession", "2\nProject",
        "3\nCross-project\n(agent)", "4\nCross-session\n(human)",
        "5\nDistributed\nevolution"
    ], fontsize=8)

    # Value labels on bars
    for bar, val in zip(bars, sorted_data["Z"]):
        ax.text(
            bar.get_width() + 0.08, bar.get_y() + bar.get_height() / 2,
            f"{val:g}", va="center", fontsize=9, color="#333"
        )

    plt.tight_layout()
    fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    # Three 2D scatter plots, one per dimension pair
    plot_xy_oversight_vs_provenance(data, OUT_DIR / "oversight-vs-provenance.png")
    plot_xz_oversight_vs_experience(data, OUT_DIR / "oversight-vs-experience.png")
    plot_yz_provenance_vs_experience(data, OUT_DIR / "provenance-vs-experience.png")
    # Bar chart for Z-axis
    plot_z_axis_bars(data, OUT_DIR / "experience-accumulation-bars.png")
    print(f"\nAll plots saved to {OUT_DIR}")
