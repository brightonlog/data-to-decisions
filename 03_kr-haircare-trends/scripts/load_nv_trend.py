"""Load 네이버 데이터랩 검색어트렌드 엑셀(일간) -> 월평균 -> data/naver_search_trend_monthly.csv, table nv_trend.

원본: data/naver_search_trend_all.xlsx (전체), data/naver_search_trend_2030f.xlsx (여성 19~39세)
- 엑셀 1~6행은 조회 조건, 7행이 머리글, 8행부터 일간 값이다.
- 수집일(2026-11-12)은 값이 0으로 들어와 있고 2026-11은 한 달이 차지 않아서 2026-10까지만 쓴다.
- ratio는 일간 상댓값의 월평균이다. 두 파일은 따로 조회한 값이라 세그먼트끼리 크기를 비교할 수 없다.
"""
import sqlite3
import warnings
from pathlib import Path
import pandas as pd

warnings.filterwarnings("ignore", message="Workbook contains no default style")
root = Path(__file__).resolve().parent.parent
FILES = {"전체": "naver_search_trend_all.xlsx", "2030여성": "naver_search_trend_2030f.xlsx"}
TOPIC = {"탈모": "탈모", "두피케어": "두피케어", "손상복구": "손상·복구", "윤기오일": "윤기·오일", "염색컬러": "염색·컬러"}

parts = []
for segment, name in FILES.items():
    raw = pd.read_excel(root / "data" / name, header=None)
    head, body = raw.iloc[6], raw.iloc[7:]
    for col in range(1, raw.shape[1], 2):  # (날짜, 값) 쌍이 주제마다 반복된다
        parts.append(pd.DataFrame({
            "date": pd.to_datetime(body[col - 1]),
            "segment": segment,
            "topic": TOPIC[str(head[col]).strip()],
            "ratio": body[col].astype(float),
        }))
daily = pd.concat(parts)
daily = daily[daily["date"] < "2026-11-01"]
assert (daily["ratio"] > 0).all()
daily["month"] = daily["date"].dt.strftime("%Y-%m")
monthly = (daily.groupby(["month", "segment", "topic"], as_index=False)["ratio"].mean().round({"ratio": 2}))
assert len(monthly) == 24 * 2 * 5, len(monthly)

monthly.to_csv(root / "data" / "naver_search_trend_monthly.csv", index=False, encoding="utf-8-sig")
with sqlite3.connect(root / "data" / "haircare.db") as con:
    monthly.to_sql("nv_trend", con, if_exists="replace", index=False)
print(f"nv_trend: {len(monthly)} rows")
