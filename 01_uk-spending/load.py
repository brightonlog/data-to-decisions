"""ONS 'Revolut spending on debit cards' xlsx -> CSV + DuckDB. 에디션별 분리 저장."""
import sys, re, pathlib
import openpyxl, duckdb



SRC = pathlib.Path(sys.argv[1])            # xlsx 경로
ED  = re.search(r"(\d{6})\.xlsx$", SRC.name).group(1)  # 예: 291026 -> 2026-10-29 릴리스
OUT = pathlib.Path(__file__).parent / "data" / ED
OUT.mkdir(parents=True, exist_ok=True)

SHEET_MAP = {  # 시트명 -> 테이블명 (두 세대 포맷 모두 지원)
    "Table 1": "daily_total", "Table 2": "daily_age", "Table 3": "daily_online", "Table 4": "monthly_total",
    "1.Spending by Sector NSA": "daily_sector", "2.Spending by Age NSA": "daily_age",
    "3.Spending Online NSA": "daily_online", "4.Monthly by Sector NSA": "monthly_sector_nsa",
    "5.Monthly by Sector SA": "monthly_sector_sa", "6.Monthly Trend": "monthly_trend",
}

def norm(c):  # 컬럼명 표준화: '18-34' -> age_18_34, 'Total' -> total
    c = str(c).strip().lower().replace("+", "plus").replace("-", "_").replace(" ", "_")
    return f"age_{c}" if c[0].isdigit() else c



wb = openpyxl.load_workbook(SRC, read_only=True, data_only=True) 
con = duckdb.connect(str(OUT / f"ons_{ED}.duckdb"))
for ws in wb.worksheets:
    tbl = SHEET_MAP.get(ws.title)
    if not tbl:
        continue
    rows = list(ws.iter_rows(values_only=True))
    hdr_i = next(i for i, r in enumerate(rows) if r and r[0] == "Date")
    cols = [norm(c) for c in rows[hdr_i] if c is not None]
    body = [r[: len(cols)] for r in rows[hdr_i + 1 :] if r and r[0] is not None]
    csv = OUT / f"{tbl}.csv"
    with open(csv, "w") as f:
        f.write(",".join(cols) + "\n")
        for r in body:
            f.write(",".join("" if v in (None, "[x]") else str(v) for v in r) + "\n")
    fmt = "%d %b %Y" if tbl.startswith("daily") else "%b %Y"
    con.execute(f"""
        CREATE OR REPLACE TABLE {tbl} AS
        SELECT strptime(date, '{fmt}')::DATE AS date,
               * EXCLUDE (date)
        FROM read_csv('{csv}', header=true, nullstr='')
    """)
    n = con.execute(f"SELECT count(*), min(date), max(date) FROM {tbl}").fetchone()
    print(f"{ED} {tbl:20s} rows={n[0]:5d}  {n[1]} ~ {n[2]}")
con.close()
