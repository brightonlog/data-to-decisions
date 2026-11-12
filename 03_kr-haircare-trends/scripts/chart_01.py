"""Chart for Q1: analysis/01_brand_share.csv -> analysis/01_brand_share.png"""
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

root = Path(__file__).resolve().parent.parent
df = pd.read_csv(root / "analysis" / "01_brand_share.csv")
df["순위"] = df["제품수"].rank(method="min", ascending=False).astype(int)

# 제품 3개 이상(공동 10위 제외) + 로레알 그룹 브랜드
LOREAL = {"케라스타즈": "#1F3A5F", "로레알 프로페셔널": "#1F3A5F", "로레알": "#7D93B2"}
show = df[(df["순위"] < 10) | df["brand"].isin(LOREAL)].copy()
dup = show["순위"].map(df["순위"].value_counts()) > 1
show["label"] = [f"{'공동 ' if d else ''}{r}위  {'로레알파리' if b == '로레알' else b}" for r, b, d in zip(show["순위"], show["brand"], dup)]
show = show.iloc[::-1]

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200, facecolor="white")
colors = [LOREAL.get(b, "#C9CED6") for b in show["brand"]]
bars = ax.barh(show["label"], show["제품수"], color=colors, height=0.6)
for bar, n, avg in zip(bars, show["제품수"], show["평균_등수"]):
    ax.text(bar.get_width() + 0.08, bar.get_y() + bar.get_height() / 2,
            f"{n}개 · 평균 {int(avg + 0.5)}위", va="center", fontsize=7)

ax.set_title("케라스타즈는 제품 수 1위(7개)지만 평균 등수는 70위",
             fontsize=11, loc="left", pad=10)
ax.set_xlabel("랭킹 100위 안 제품 수", fontsize=7)
ax.tick_params(axis="y", labelsize=7, length=0)
ax.tick_params(axis="x", labelsize=6)
ax.set_xlim(0, show["제품수"].max() + 1.6)
ax.spines[["top", "right"]].set_visible(False)
ax.margins(y=0.01)
fig.text(0.01, 0.01, "출처: 올리브영 온라인몰 헤어케어 판매랭킹 1~100위 · 수집 2026-11-12",
         fontsize=5, color="#666666")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(root / "analysis" / "01_brand_share.png", facecolor="white")
