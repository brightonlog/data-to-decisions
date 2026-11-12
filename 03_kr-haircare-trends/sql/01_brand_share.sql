SELECT brand,
	COUNT(*) AS 제품수,
	CAST(ROUND(AVG(rank)) AS INTEGER) AS 평균_등수
FROM oy_rank
GROUP BY brand
ORDER BY 제품수 DESC;