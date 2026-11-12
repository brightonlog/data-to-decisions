-- 6. 전체와 2030 여성은 검색어 주제가 어떻게 다른가 
SELECT segment, topic, COUNT(*) AS 검색어수
FROM nv_keyword
GROUP BY segment, topic
ORDER BY topic, segment DESC;