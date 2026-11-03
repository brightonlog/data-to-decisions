FROM v_monthly_long
SELECT sector,
  idx,
  total,
  ROUND(idx / total, 2) AS rel_idx
WHERE date = '2026-09-01'
ORDER BY rel_idx DESC