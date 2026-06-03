
-- Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- Total Transactions
SELECT COUNT(*) AS total_transactions
FROM fact_transactions;

-- Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- SIP Transactions Count
SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type = 'SIP';

-- 6. Average Expense Ratio
SELECT AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;

-- 7. Top 5 Funds by 1 Year Return
SELECT scheme_name, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 8. Redemption Transactions Count
SELECT COUNT(*) AS redemption_count
FROM fact_transactions
WHERE transaction_type = 'REDEMPTION';

-- 9. Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 10. Average AUM
SELECT AVG(aum_crore) AS avg_aum
FROM fact_performance;