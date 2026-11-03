SELECT
  sector,
  MAX(CASE WHEN date = '2024-09-01' THEN idx END) AS idx_2024,
  MAX(CASE WHEN date = '2026-09-01' THEN idx END) AS idx_2026,
  ROUND(
    ( MAX(CASE WHEN date = '2026-09-01' THEN idx END)
    - MAX(CASE WHEN date = '2024-09-01' THEN idx END) )
    / MAX(CASE WHEN date = '2024-09-01' THEN idx END) * 100
  , 1) AS change_pct
FROM v_monthly_long
WHERE date IN ('2024-09-01', '2026-09-01')
GROUP BY sector
ORDER BY change_pct DESC