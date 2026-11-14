"""올리브영 랭킹 제품 100개에 검색어(B)와 같은 주제(topic)를 붙인다.
-> data/oy_rank_topic.csv (rank, topic, needs_check), table oy_rank_topic (oy_rank + topic, topic_check)

분류 규칙은 nv_keyword와 같다: 제품명에 고민이 드러나면 그 주제.
머리 빠짐·볼륨은 탈모, 비듬·지성·각질·진정은 두피케어, 트리트먼트·헤어팩은 손상·복구,
에센스·오일·식초는 윤기·오일, 고민 표시 없는 샴푸는 세정 일반.
열보호·노워시 트리트먼트는 손상·복구, '글로스·광채' 라인은 윤기·오일, 탈모 문구로 판매하는 두피 앰플은 탈모.
기기·브러쉬(6, 35, 82위)도 같은 규칙으로 주제를 붙이고, 기기 여부는 cat_mid로 구분한다.
사용자가 2026-11-13에 분류를 모두 확정했다. 순위 뒤에 '?'를 붙이면 확정 전으로 표시된다 (needs_check = 1).
"""
import sqlite3
from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent.parent
TOPICS = {
    "탈모": "2 4 5 13 14 21 22 77 96 28 36 63 86 10 52 76 39 51",
    "두피케어": "11 62 16 53 55 87 99 100 68 35 82",
    "손상·복구": "8 80 88 27 54 70 92 1 17 24 50 57 60 71 75 89 90 93 6 81 64 79 19 30 45 42",
    "윤기·오일": "15 25 33 56 72 84 3 9 18 49 74 94 95 47 29 91",
    "염색·컬러": "7 12 32 37 40 48 67 73",
    "스타일링": "20 43 66 85 44 58 59 97 26 31 46 83 23 78 34",
    "세정 일반": "41 38 65",
    "기타": "69 98 61",
}
rows = [(int(tok.rstrip("?")), topic, int(tok.endswith("?"))) for topic, s in TOPICS.items() for tok in s.split()]
t = pd.DataFrame(rows, columns=["rank", "topic", "needs_check"]).sort_values("rank")
assert sorted(t["rank"]) == list(range(1, 101)), "every rank 1..100 exactly once"
t.to_csv(root / "data" / "oy_rank_topic.csv", index=False, encoding="utf-8-sig")

with sqlite3.connect(root / "data" / "haircare.db") as con:
    oy = pd.read_sql_query("SELECT * FROM oy_rank", con)
    merged = oy.merge(t.rename(columns={"needs_check": "topic_check"}), on="rank", validate="one_to_one")
    merged.to_sql("oy_rank_topic", con, if_exists="replace", index=False)
print(t["topic"].value_counts().to_string())
print("needs_check:", int(t["needs_check"].sum()))
