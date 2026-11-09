"""SQL 파일 실행기. 사용: py run.py sql/q1.sql [에디션=291026]
- 파일 안에 쿼리가 여러 개면 ';'로 구분해 순서대로 실행, 마지막 결과만 출력.
- 결과는 markdown 표로 출력 → 노션·README에 바로 붙임.
"""
import sys, duckdb
stmts = [s for s in stmts if re.sub(r"--.*", "", s).strip()]
# drop chunks that are only comments / 주석만 남은 조각 제거
sql_path = sys.argv[1]
ed = sys.argv[2] if len(sys.argv) > 2 else "291026"
con = duckdb.connect(f"data/{ed}/ons_{ed}.duckdb")

# 00_long.sql(뷰 정의)은 매번 먼저 실행해 뷰 보장
try:
    con.execute(open("sql/00_long.sql", encoding="utf-8").read())
except FileNotFoundError:
    pass

stmts = [s.strip() for s in open(sql_path, encoding="utf-8").read().split(";") if s.strip()]
for s in stmts[:-1]:
    con.execute(s)
rel = con.sql(stmts[-1])
print(rel.df().to_markdown(index=False, floatfmt=".2f"))
