"""Chart for Q6: analysis/06_keyword_segment.csv -> analysis/06_keyword_segment.png"""
import numpy as np
import pandas as pd
from chartstyle import GRAY, NAVY, ROOT, finish, new_fig

df = pd.read_csv(ROOT / "analysis" / "06_keyword_segment.csv")
p = df.pivot(index="topic", columns="segment", values="검색어수").fillna(0).astype(int)
p["diff"] = p["2030여성"] - p["전체"]
p = p.sort_values(["diff", "전체"], ascending=[True, True])  # barh draws bottom-up
y = np.arange(len(p)); h = 0.38

fig, ax = new_fig()
ax.barh(y + h / 2, p["전체"], height=h, color=GRAY, label="전체")
ax.barh(y - h / 2, p["2030여성"], height=h, color=NAVY, label="2030 여성")
for yi, (a, w, d) in enumerate(zip(p["전체"], p["2030여성"], p["diff"])):
    ax.text(a + 0.2, yi + h / 2, f"{a}개", va="center", fontsize=6)
    ax.text(w + 0.2, yi - h / 2, f"{w}개" + (f" ({d:+d})" if d else ""), va="center", fontsize=6, color=NAVY)

ax.set_yticks(y, p.index)
ax.set_xlabel("인기검색어 100위 안 검색어 수", fontsize=7)
ax.tick_params(axis="y", labelsize=8, length=0)
ax.tick_params(axis="x", labelsize=6)
ax.set_xlim(0, 29)
ax.margins(y=0.02)
ax.legend(fontsize=6.5, frameon=False, loc="center right")
finish(fig, ax, "06_keyword_segment", "2030 여성은 손상·복구 검색어가 전체보다 8개 많고, 탈모 검색어는 10개 적음",
       source="출처: 네이버 데이터랩 쇼핑인사이트 헤어케어 인기검색어 1~100위 (전체 / 여성 20·30대, 최근 1년) · 수집 2026-11-12 · 주제는 분석자 분류")
