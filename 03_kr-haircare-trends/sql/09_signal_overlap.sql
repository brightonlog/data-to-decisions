-- 9. 검색어, 랭킹, 업계 동향 세 데이터에 모두 나오는 주제는 무엇인가
WITH s AS (
    -- 2030 여성 인기 검색어를 주제별로 센 표
    SELECT topic, COUNT(*) AS search_cnt
    FROM nv_keyword
    WHERE segment = '2030여성'
    GROUP BY topic
),
r AS (
    -- 올리브영 랭킹 제품을 주제별로 센 표
    SELECT topic, COUNT(*) AS rank_cnt
    FROM oy_rank_topic
    GROUP BY topic
),
d AS (
    -- 업계 동향을 주제별로 센 표 (타깃, 기타는 헤어 고민 주제가 아니라서 제외)
    SELECT topic, COUNT(*) AS signal_cnt
    FROM industry_signal
    WHERE topic NOT IN ('타깃', '기타')
    GROUP BY topic
)
SELECT s.topic,
       s.search_cnt,
       COALESCE(r.rank_cnt, 0)   AS rank_cnt,
       COALESCE(d.signal_cnt, 0) AS signal_cnt,
       1 + (r.rank_cnt IS NOT NULL) + (d.signal_cnt IS NOT NULL) AS data_cnt
FROM s
LEFT JOIN r ON s.topic = r.topic
LEFT JOIN d ON s.topic = d.topic
ORDER BY data_cnt DESC, s.search_cnt DESC;
