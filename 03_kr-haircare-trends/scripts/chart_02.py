"""Chart for Q2: analysis/02_category.csv -> analysis/02_category.png
Dark segment = 프로페셔널 사업부 브랜드 제품 수 (from analysis/01b_pro_products.csv)."""
import pandas as pd
from chartstyle import GRAY, NAVY, ROOT, finish, new_fig

df = pd.read_csv(ROOT / "analysis" / "02_category.csv").iloc[::-1]
pro = pd.read_csv(ROOT / "analysis" / "01b_pro_products.csv")["cat_small"].value_counts()
df["pro"] = df["cat_small"].map(pro).fillna(0).astype(int)

fig, ax = new_fig()
ax.barh(df["cat_small"], df["제품수"], color=GRAY, height=0.65, label="그 외 브랜드")
ax.barh(df["cat_small"], df["pro"], color=NAVY, height=0.65, label="프로페셔널 사업부 브랜드 (케라스타즈·로레알 프로페셔널)")
for y, (n, p) in enumerate(zip(df["제품수"], df["pro"])):
    ax.text(n + 0.25, y, f"{n}개" + (f" (프로페셔널 {p}개)" if p else ""), va="center", fontsize=6.5)

ax.set_xlabel("랭킹 100위 안 제품 수", fontsize=7)
ax.tick_params(axis="y", labelsize=7, length=0)
ax.tick_params(axis="x", labelsize=6)
ax.set_xlim(0, df["제품수"].max() + 5)
ax.margins(y=0.01)
ax.legend(fontsize=6, frameon=False, loc="lower right")
finish(fig, ax, "02_category", "샴푸·헤어트리트먼트·헤어에센스 세 종류가 100개 중 53개")
