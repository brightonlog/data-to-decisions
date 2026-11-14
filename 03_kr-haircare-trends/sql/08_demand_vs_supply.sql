-- 8. 2030 여성이 찾는 주제와 랭킹에 있는 제품의 주제는 어떻게 다른가
WITH s AS (
    -- 2030 여성 인기 검색어 100개를 주제별로 센 표
    SELECT topic, COUNT(*) AS search_cnt
    FROM nv_keyword
    WHERE segment = '2030여성'
    GROUP BY topic
),
r AS (
    -- 올리브영 랭킹 제품 100개를 주제별로 센 표
    SELECT topic, COUNT(*) AS rank_cnt
    FROM oy_rank_topic
    GROUP BY topic
)
SELECT s.topic,
       s.search_cnt,
       COALESCE(r.rank_cnt, 0) AS rank_cnt,
       s.search_cnt - COALESCE(r.rank_cnt, 0) AS diff
FROM s
LEFT JOIN r ON s.topic = r.topic
ORDER BY diff DESC;
