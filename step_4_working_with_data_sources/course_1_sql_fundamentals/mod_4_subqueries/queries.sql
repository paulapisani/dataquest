-- select majors with unemploment rate lower than avg
SELECT Major, Unemployment_rate
FROM recent_grads
WHERE Unemployment_rate < (SELECT AVG(Unemployment_rate) FROM recent_grads)
ORDER BY Unemployment_rate

-- select proportion of jobs with above avg share of women
SELECT COUNT(*) / CAST((SELECT COUNT(*) FROM recent_grads) AS Float) AS proportion_abv_avg
FROM recent_grads
WHERE ShareWomen > (SELECT AVG(ShareWomen) FROM recent_grads)

-- select where major category is one of five highest group levels for Total
SELECT Major, Major_category
FROM recent_grads
WHERE Major_category IN 
    (SELECT Major_category
     FROM recent_grads
     GROUP BY Major_category
     ORDER BY SUM(Total) DESC
     LIMIT 5)

-- select avg ratio of sample size to total for all majors
SELECT AVG(CAST(Sample_size AS Float) / CAST(Total AS Float)) AS avg_ratio
FROM recent_grads

-- select majors where ratio is above average 
SELECT Major, Major_category, CAST(Sample_size AS Float) / CAST(Total AS Float) AS ratio
FROM recent_grads
WHERE CAST(Sample_size AS Float) / CAST(Total AS Float) > 
    (SELECT AVG(CAST(Sample_size AS Float) / CAST(Total AS Float)) AS avg_ratio
    FROM recent_grads)
