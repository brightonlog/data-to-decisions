"""Chart for Q7: analysis/07_topic_trend.csv -> analysis/07_topic_trend.png (세그먼트별 선 그래프 2칸)"""
import matplotlib.pyplot as plt
import pandas as pd
from chartstyle import GRAY, LIGHT_NAVY, NAVY, ROOT, finish, new_fig

df = pd.read_csv(ROOT / "analysis" / "07_topic_trend.csv")
STYLE = {  # 6번에서 차이가 컸던 두 주제만 색으로 강조
    "손상·복구": dict(color=NAVY, lw=1.8, ls="-"),
    "탈모": dict(color=LIGHT_NAVY, lw=1.8, ls="-"),
    "두피케어": dict(color="#8A8F98", lw=1.0, ls="--"),
    "윤기·오일": dict(color="#8A8F98", lw=1.0, ls=":"),
    "염색·컬러": dict(color=GRAY, lw=1.2, ls="-"),
}
PANELS = [("전체", "전체 (성별·연령 전체)"), ("2030여성", "2030 여성 (여성 19~39세)")]

fig, _ = new_fig()
plt.close(fig)
fig, axes = plt.subplots(1, 2, figsize=(8, 4.5), dpi=200, facecolor="white")
for ax, (seg, label) in zip(axes, PANELS):
    p = df[df["segment"] == seg].pivot(index="month", columns="topic", values="ratio")
    for topic, style in STYLE.items():
        ax.plot(range(len(p)), p[topic], label=topic, **style)
    ticks = list(range(0, len(p), 4))
    ax.set_xticks(ticks, [p.index[i][2:].replace("-", ".") for i in ticks])
    ax.set_ylim(0, p.max().max() * 1.15)
    ax.tick_params(labelsize=6)
    ax.set_ylabel("검색 지수 (월평균, 상댓값)", fontsize=6.5)
    ax.text(0.02, 0.97, label, transform=ax.transAxes, fontsize=7.5, va="top", weight="bold")
    ax.spines[["top", "right"]].set_visible(False)
axes[1].legend(fontsize=6, frameon=False, loc="lower left", ncol=2)
finish(fig, axes[0], "07_topic_trend",
       "최근 1년간 평균이 이전 1년보다 가장 많이 내려간 주제는 탈모 (전체, 2030 여성 약 30%씩 감소)",
       source="출처: 네이버 데이터랩 검색어트렌드 (통합검색, 일간 값을 월평균으로 변환, 2024.11~2026.10) · 수집 2026-11-13 · 두 칸은 따로 조회한 값이라 수치 크기를 서로 비교할 수 없음")
