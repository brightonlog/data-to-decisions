SELECT
    CASE
        WHEN sector IN ('entertainment','utilities','transport','health','services','groceries') THEN 'recurring'
        ELSE 'discretionary'
    END AS spend_type,
    COUNT (DISTINCT sector) AS n_sectors,
    ROUND(AVG(CASE WHEN date = '2024-09-01' THEN idx END), 1) AS idx_2024,
    ROUND(AVG(CASE WHEN date = '2026-09-01' THEN idx END), 1) AS idx_2026,
    ROUND(((idx_2026 - idx_2024)) / idx_2024 * 100) AS change_pct
FROM v_monthly_long
WHERE date IN ('2024-09-01', '2026-09-01')
GROUP BY spend_type
ORDER BY change_pct DESC;