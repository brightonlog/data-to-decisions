SELECT is_set,
    COUNT(*) AS 제품수,
    CAST(ROUND(AVG(rank)) AS INTEGER) AS 평균_등수
FROM oy_rank
GROUP BY is_set
ORDER BY is_set DESC;