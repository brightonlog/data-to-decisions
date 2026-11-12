SELECT cat_small,
    COUNT(*) AS 제품수
FROM oy_rank
GROUP BY cat_small
ORDER BY 제품수 DESC;