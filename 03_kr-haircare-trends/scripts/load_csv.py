"""Load a CSV in data/ into data/haircare.db as a table (replaces the table).
Usage: python scripts/load_csv.py naver_shopping_keywords.csv nv_keyword
"""
import sqlite3, sys
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent.parent
csv_name, table = sys.argv[1], sys.argv[2]
df = pd.read_csv(root / "data" / csv_name, encoding="utf-8-sig")
with sqlite3.connect(root / "data" / "haircare.db") as con:
    df.to_sql(table, con, if_exists="replace", index=False)
    n = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
assert n == len(df)
print(f"{table}: {n} rows")
