"""Chart for Q8: analysis/08_demand_vs_supply.csv -> analysis/08_demand_vs_supply.png"""
import numpy as np
import pandas as pd
from chartstyle import GRAY, NAVY, ROOT, finish, new_fig

p = pd.read_csv(ROOT / "analysis" / "08_demand_vs_supply.csv").sort_values("diff")  # barh draws bottom-up
y = np.arange(len(p)); h = 0.38

fig, ax = new_fig()
ax.barh(y + h / 2, p["search_cnt"], height=h, color=NAVY, label="2030 여성 인기 검색어 수")
ax.barh(y - h / 2, p["rank_cnt"], height=h, color=GRAY, label="올리브영 랭킹 제품 수")
for yi, (s, r, d) in enumerate(zip(p["search_cnt"], p["rank_cnt"], p["diff"])):
    ax.text(s + 0.2, yi + h / 2, f"{s}개 ({d:+d})", va="center", fontsize=6, color=NAVY)
    ax.text(r + 0.2, yi - h / 2, f"{r}개", va="center", fontsize=6)

ax.set_yticks(y, p["topic"])
ax.set_xlabel("100개 중 개수 (괄호는 검색어 수 - 제품 수)", fontsize=7)
ax.tick_params(axis="y", labelsize=8, length=0)
ax.tick_params(axis="x", labelsize=6)
ax.set_xlim(0, 31)
ax.margins(y=0.02)
ax.legend(fontsize=6.5, frameon=False, loc="lower right")
finish(fig, ax, "08_demand_vs_supply", "고민이 드러난 주제 중 검색어가 랭킹 제품보다 많은 것은 두피케어뿐 (검색어 15개, 제품 11개)",
       source="출처: 네이버 데이터랩 쇼핑인사이트 헤어케어 인기검색어 1~100위 (여성 20·30대, 최근 1년) · 올리브영 온라인몰 헤어케어 판매랭킹 1~100위 · 수집 2026-11-12 · 주제는 분석자 분류")
