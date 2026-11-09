-- Q4: Segment size by age = households × weekly spend per household (£m/week)
-- Q4: 연령대별 세그먼트 크기 = 가구 수 × 가구당 주간 지출 (단위 £백만/주)
-- Source: ONS Family Spending FYE2023-25, Tables A12-A16 ("All households" column)

SELECT
  age_group,
  CAST(households_k AS INTEGER) AS households_k,
  weekly_gbp,
  CAST(ROUND(households_k * weekly_gbp / 1000, 0) AS INTEGER) AS weekly_total_gbp_m,
  ROUND(100 * households_k * weekly_gbp / SUM(households_k * weekly_gbp) OVER (), 1) AS share_pct
FROM v_ons_age
WHERE code = '1-13'
ORDER BY weekly_total_gbp_m DESC;