"""Chart for Q5: analysis/05_keyword_topic.csv -> analysis/05_keyword_topic.png"""
import pandas as pd
from chartstyle import GRAY, ROOT, finish, new_fig

df = pd.read_csv(ROOT / "analysis" / "05_keyword_topic.csv").iloc[::-1]

fig, ax = new_fig()
bars = ax.barh(df["topic"], df["검색어수"], color=GRAY, height=0.65)
for bar, n in zip(bars, df["검색어수"]):
    ax.text(n + 0.25, bar.get_y() + bar.get_height() / 2, f"{n}개", va="center", fontsize=7)

ax.set_xlabel("인기검색어 100위 안 검색어 수", fontsize=7)
ax.tick_params(axis="y", labelsize=8, length=0)
ax.tick_params(axis="x", labelsize=6)
ax.set_xlim(0, df["검색어수"].max() + 3)
ax.margins(y=0.02)
finish(fig, ax, "05_keyword_topic", "검색어 100개 중 탈모 관련 검색어가 25개로 가장 많음",
       source="출처: 네이버 데이터랩 쇼핑인사이트 헤어케어 인기검색어 1~100위 (전체, 최근 1년) · 수집 2026-11-12 · 주제는 분석자 분류")
