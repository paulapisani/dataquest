-- check first ten lines 
SELECT *
FROM recent_grads
LIMIT 10;

-- select majors where women are in minority
SELECT Major, ShareWomen
FROM recent_grads
WHERE ShareWomen < 0.5;

-- select majors with majority women and median salary > 50000
SELECT Major, Major_category, Median, ShareWomen
FROM recent_grads
WHERE ShareWomen > 0.50
AND Median > 50000;

-- select top 20 majors that have median salary above 10000 or less than / equal to  1000 unemployed
SELECT Major, Median, Unemployed
FROM recent_grads
WHERE Median >= 10000
OR Unemployed <= 1000
LIMIT 20;

-- select majors that are Engineering and had either mostly women graduates or unemployment rate below 5.1%
SELECT Major, Major_category, ShareWomen, Unemployment_rate
FROM recent_grads
WHERE Major_category = 'Engineering' 
AND (ShareWomen > 0.5 OR Unemployment_rate < 0.051); 

-- select majors with share of women > 30% and unemployment rate of < 10%, and order by share of women desc
SELECT Major, ShareWomen, Unemployment_rate
FROM recent_grads
WHERE ShareWomen > 0.3
AND Unemployment_rate < 0.1
ORDER BY  ShareWomen DESC

-- select majors in engineering or physical sciences
SELECT Major_category, Major, Unemployment_rate
FROM recent_grads
WHERE Major_category = 'Engineering'
OR Major_category = 'Physical Sciences'
ORDER BY Unemployment_rate

