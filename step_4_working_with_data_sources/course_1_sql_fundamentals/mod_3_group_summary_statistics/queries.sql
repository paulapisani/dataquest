-- select all columns with five row sample
SELECT *
FROM recent_grads
LIMIT 5

-- select major category and avg share of women
SELECT Major_category, AVG(ShareWomen)
FROM recent_grads
GROUP BY Major_category

-- select major category and avg percent employed
SELECT Major_category, AVG(Employed) / AVG(Total) AS share_employed
FROM recent_grads
GROUP BY Major_category

-- select major categories where share of low wage jobs > 10%
SELECT Major_category, AVG(Low_wage_jobs) / AVG(Total) as share_low_wage
FROM recent_grads
GROUP BY Major_category
Having share_low_wage > 0.1

-- select rounded version of share women metric
SELECT ROUND(ShareWomen, 4), Major_category
FROM recent_grads
LIMIT 10

-- select rounded version of share of degrees  
SELECT Major_category, 
    ROUND(AVG(College_jobs) / AVG(Total), 3) AS share_degree_jobs
FROM recent_grads
GROUP BY Major_category
HAVING share_degree_jobs < 0.3

-- select major category and share of women as float
SELECT Major_category, 
    SUM(Women) / CAST(SUM(Total) AS Float) AS SW
FROM recent_grads
GROUP BY Major_category
ORDER BY SW

