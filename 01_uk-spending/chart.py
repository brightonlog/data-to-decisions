"""SQL 결과 → PNG 차트. 사용:
  py chart.py sql/q1.sql --kind barh --x sector --y change_pct --baseline 18.2 --title "..." --out charts/q1.png
  py chart.py sql/q3.sql --kind line --x month --y a18_34,a35_54,a55plus --title "..." --out charts/q3.png
옵션: --baseline (기준선 값) --unit (축 단위 라벨) --highlight (강조할 x값, 쉼표 구분)
"""
import argparse, pathlib, duckdb
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ACCENT, MUTED, INK, GRID = "#2F5BEA", "#B8BFCC", "#1F2430", "#E6E9EF"
SERIES = ["#2F5BEA", "#E8702A", "#1FA67A", "#8B5CF6"]  # 고정 순서, 최대 4

p = argparse.ArgumentParser()
p.add_argument("sql"); p.add_argument("--kind", choices=["barh", "line"], required=True)
p.add_argument("--x", required=True); p.add_argument("--y", required=True)
p.add_argument("--title", default=""); p.add_argument("--unit", default="")
p.add_argument("--baseline", type=float); p.add_argument("--highlight", default="")
p.add_argument("--edition", default="291026"); p.add_argument("--out")
a = p.parse_args()

con = duckdb.connect(f"data/{a.edition}/ons_{a.edition}.duckdb", read_only=True)
try: con.execute(open("sql/00_long.sql", encoding="utf-8").read())
except Exception: pass
stmts = [s.strip() for s in open(a.sql, encoding="utf-8").read().split(";") if s.strip()]
for s in stmts[:-1]: con.execute(s)
df = con.sql(stmts[-1]).df()

ys = a.y.split(","); hl = set(a.highlight.split(",")) if a.highlight else set()
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=160)
ax.set_facecolor("white"); fig.patch.set_facecolor("white")
for sp in ["top", "right"]: ax.spines[sp].set_visible(False)
ax.spines["left"].set_color(GRID); ax.spines["bottom"].set_color(GRID)
ax.tick_params(colors=INK, labelsize=9)

if a.kind == "barh":
    d = df.sort_values(ys[0])
    colors = [ACCENT if (str(v) in hl or not hl) else MUTED for v in d[a.x]]
    if hl: colors = [ACCENT if str(v) in hl else MUTED for v in d[a.x]]
    ax.barh(d[a.x].astype(str), d[ys[0]], color=colors, height=0.62)
    for i, v in enumerate(d[ys[0]]):
        ax.text(v + (abs(d[ys[0]]).max() * 0.01), i, f"{v:.1f}{a.unit}", va="center", fontsize=9, color=INK)
    if a.baseline is not None:
        ax.axvline(a.baseline, color=INK, lw=1, ls="--")
        ax.text(a.baseline, len(d) - 0.4, f" total {a.baseline:g}{a.unit}", fontsize=8, color=INK, va="bottom")
    ax.xaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.set_xlabel(a.unit, color=INK, fontsize=9)
else:
    for i, y in enumerate(ys):
        ax.plot(df[a.x], df[y], color=SERIES[i], lw=2)
        ax.text(df[a.x].iloc[-1], df[y].iloc[-1], f" {y}", fontsize=9, color=SERIES[i], va="center")
    if a.baseline is not None:
        ax.axhline(a.baseline, color=INK, lw=1, ls="--")
    ax.yaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
    ax.set_ylabel(a.unit, color=INK, fontsize=9)
    fig.autofmt_xdate()

ax.set_title(a.title, loc="left", fontsize=11, color=INK, pad=12)
fig.text(0.01, 0.01, "Source: ONS, Revolut spending on debit cards (index, 2023 = 100, per account)", fontsize=7, color="#6B7280")
out = a.out or f"charts/{pathlib.Path(a.sql).stem}.png"
pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(out); print("saved", out)
