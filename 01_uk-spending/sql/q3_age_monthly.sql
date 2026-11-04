SELECT
    date_trunc('month', date) AS month,
    ROUND(AVG(age_18_34), 1) AS a18_34,
    ROUND(AVG(age_35_54), 1) AS a35_54,
    ROUND(AVG(age_55plus), 1) AS a55plus
FROM daily_age
GROUP BY month
ORDER BY month DESC
