"""Chart for Q4: analysis/04_pro_position.csv -> analysis/04_pro_position.png (가격 × 순위 산점도)"""
import pandas as pd
from chartstyle import GRAY, LIGHT_NAVY, NAVY, ROOT, finish, new_fig

df = pd.read_csv(ROOT / "analysis" / "04_pro_position.csv")
df["만원"] = df["판매가"] / 10000
pro = df["브랜드"].isin(["케라스타즈", "로레알 프로페셔널"])
paris = df["브랜드"] == "로레알"

fig, ax = new_fig()
ax.scatter(df.loc[~pro & ~paris, "만원"], df.loc[~pro & ~paris, "순위"], s=22, color=GRAY, label="그 외 브랜드")
ax.scatter(df.loc[paris, "만원"], df.loc[paris, "순위"], s=26, color=LIGHT_NAVY, label="로레알파리 (참고)")
ax.scatter(df.loc[pro, "만원"], df.loc[pro, "순위"], s=34, color=NAVY, label="프로페셔널 사업부 브랜드")
for r in df[pro].itertuples():
    name = "로레알 프로페셔널" if r.브랜드 == "로레알 프로페셔널" else "케라스타즈"
    ax.annotate(f"{name} {r.순위}위", (r.만원, r.순위), xytext=(5, 0 if r.순위 != 91 else -7),
                textcoords="offset points", fontsize=5.5, color=NAVY, va="center")

median = df["만원"].median()
ax.axvline(median, color="#999999", lw=0.6, ls="--")
ax.text(median - 0.1, -4, f"중앙값 {median * 10000:,.0f}원", fontsize=5.5, color="#666666", va="center", ha="right")

ax.set_ylim(104, -7)
ax.set_yticks([1, 20, 40, 60, 80, 100])
ax.set_xlabel("판매가 (만 원)", fontsize=7)
ax.set_ylabel("판매 순위 (위쪽이 높은 순위)", fontsize=7)
ax.tick_params(labelsize=6)
ax.legend(fontsize=6, frameon=False, loc="lower right")
finish(fig, ax, "04_pro_position", "케라스타즈 상품 7개는 모두 5만 원 이상, 로레알 프로페셔널은 1만 원대, 100개 중 70개는 1만~2만 원대")
