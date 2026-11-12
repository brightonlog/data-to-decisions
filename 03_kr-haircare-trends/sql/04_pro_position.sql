SELECT rank AS 순위,
    brand AS 브랜드,
    product_name AS 제품명,
    cat_small AS 제품종류,
    sale_price AS 판매가,
    list_price AS 정가,
    is_set AS 세트여부
FROM oy_rank
ORDER BY rank;
