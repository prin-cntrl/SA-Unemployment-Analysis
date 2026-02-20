-- 1. Average unemployment rate
SELECT AVG(Unemployment_Rate) 
FROM unemployment_sa;

-- 2. Year with highest unemployment
SELECT Year, Unemployment_Rate
FROM unemployment_sa
ORDER BY Unemployment_Rate DESC
LIMIT 1;

-- 3. Years with unemployment above 30%
SELECT Year, Unemployment_Rate
FROM unemployment_sa
WHERE Unemployment_Rate > 30;
