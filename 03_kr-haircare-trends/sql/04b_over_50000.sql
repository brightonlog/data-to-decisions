-- 4-1. 판매가 5만 원 이상인 제품은 무엇인가
SELECT rank, brand, cat_small, sale_price AS 판매가
FROM oy_rank
WHERE sale_price >= 50000
ORDER BY rank;
