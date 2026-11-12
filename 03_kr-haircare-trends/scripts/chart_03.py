"""Chart for Q3: analysis/03_set_vs_single.csv -> analysis/03_set_vs_single.png"""
import pandas as pd
from chartstyle import GRAY, ROOT, finish, new_fig

df = pd.read_csv(ROOT / "analysis" / "03_set_vs_single.csv").sort_values("is_set")
labels = df["is_set"].map({1: "세트", 0: "단품"})

fig, ax = new_fig()
bars = ax.barh(labels, df["제품수"], color=GRAY, height=0.5)
for bar, n, avg in zip(bars, df["제품수"], df["평균_등수"]):
    ax.text(n + 1, bar.get_y() + bar.get_height() / 2, f"{n}개 · 평균 {avg}위", va="center", fontsize=8)

ax.set_xlabel("랭킹 100위 안 제품 수", fontsize=7)
ax.tick_params(axis="y", labelsize=9, length=0)
ax.tick_params(axis="x", labelsize=6)
ax.set_xlim(0, 85)
ax.margins(y=0.25)
finish(fig, ax, "03_set_vs_single", "100개 중 67개가 세트이고, 세트의 평균 등수가 단품보다 13위 앞",
       source="출처: 올리브영 온라인몰 헤어케어 판매랭킹 1~100위 · 수집 2026-11-12 · 세트 여부는 제품명 기준 추정")
