"""Shared chart format (see CLAUDE.md '차트 형식'). Used from chart_02 onward."""
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
GRAY, NAVY, LIGHT_NAVY = "#C9CED6", "#1F3A5F", "#7D93B2"
SOURCE_OY = "출처: 올리브영 온라인몰 헤어케어 판매랭킹 1~100위 · 수집 2026-11-12"


def new_fig():
    plt.rcParams["font.family"] = "Malgun Gothic"
    plt.rcParams["axes.unicode_minus"] = False
    return plt.subplots(figsize=(8, 4.5), dpi=200, facecolor="white")


def finish(fig, ax, name, title, source=SOURCE_OY):
    ax.set_title(title, fontsize=11, loc="left", pad=10)
    ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.01, 0.01, source, fontsize=5, color="#666666")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(ROOT / "analysis" / f"{name}.png", facecolor="white")
