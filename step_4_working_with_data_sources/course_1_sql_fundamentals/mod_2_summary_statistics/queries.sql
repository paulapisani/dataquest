-- select count of majors with majority men
SELECT COUNT(Major)
FROM recent_grads
WHERE ShareWomen < 0.5

-- select min of median for engineering majors
SELECT Major, Major_category, MIN(Median)
FROM recent_grads
WHERE Major_category = 'Engineering'

-- select total number of students
SELECT SUM(Total)
FROM recent_grads

-- select avg of total, min of men, and max of women
SELECT AVG(Total), MIN(Men), MAX(Women)
FROM recent_grads

-- select total rows and max employment rate
SELECT AVG(Total), MIN(Men), MAX(Women)
FROM recent_grads

-- select unique majors, major categories, and major codes
SELECT COUNT(DISTINCT Major) AS unique_majors,
    COUNT(DISTINCT Major_category) AS unique_major_categories,
    COUNT(DISTINCT Major_code) AS unique_major_codes
FROM recent_grads

-- select quartile spread from 75th percentile - 25th percentile 
SELECT Major, Major_category, P75th - P25th AS quartile_spread
FROM recent_grads
ORDER BY P75th - P25th
LIMIT 20
