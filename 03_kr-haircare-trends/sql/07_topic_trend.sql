-- 7. 주제별 검색 관심은 2년 동안 어떻게 변했는가 
SELECT month, segment, topic, ratio
FROM nv_trend
ORDER BY segment, topic, month;