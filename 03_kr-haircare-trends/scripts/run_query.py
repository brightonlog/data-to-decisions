"""Run sql/<name>.sql against data/haircare.db and save analysis/<name>.csv.
Usage: python scripts/run_query.py 01_brand_share
"""
import sqlite3, sys
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent.parent
name = sys.argv[1]
sql = (root / "sql" / f"{name}.sql").read_text(encoding="utf-8")
with sqlite3.connect(root / "data" / "haircare.db") as con:
    df = pd.read_sql_query(sql, con)
df.to_csv(root / "analysis" / f"{name}.csv", index=False, encoding="utf-8-sig")
print(df.to_string(index=False))
