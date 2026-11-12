-- 5. 인기 검색어는 어떤 주제에 많은가
SELECT topic, 
    COUNT(*) AS 검색어수
FROM nv_keyword
WHERE segment = '전체'
GROUP BY topic
ORDER BY 검색어수 DESC;

