-- join facts and cities tables using inner join
SELECT *
FROM facts 
INNER JOIN cities 
ON facts.id = cities.facts_id
LIMIT 10

-- update previous query with aliases for tables and filtered columns
SELECT c.*, f.name AS country_name
FROM facts f 
INNER JOIN cities c 
ON f.id = c.facts_id 
LIMIT 5

-- add filter to only show capital cities for each country
SELECT f.name AS country, c.name AS capital_city
FROM facts f
INNER JOIN cities c 
ON f.id = c.facts_id 
WHERE c.capital = 1
LIMIT 5

-- find countries that doen't exist in cities table with left join (right and full outer not supported in sqlite)
SELECT f.name AS country, 
    f.population
FROM facts f 
LEFT JOIN cities c 
ON f.id = c.facts_id 
WHERE c.facts_id IS NULL

-- find 10 capital cities with highest poulation from biggest to smallest (using ORDER BY shortcut)
SELECT c.name AS capital_city,
	f.name AS country,
	c.population
FROM cities c 
LEFT JOIN facts f 
ON c.facts_id = f.id 
WHERE c.capital = 1 
ORDER BY 3 DESC
LIMIT 10

-- find capital cities with population > 10MM using subquery
SELECT c.name AS capital_city,
    f.name AS country,
    c.population
FROM facts f 
INNER JOIN 
    (
    SELECT * 
    FROM cities
    WHERE capital = 1 
    AND population > 10000000
    ) c 
ON f.id = c.facts_id
ORDER BY 3 DESC

-- find countries with percent urban pop > 0.50 using more complex query
SELECT f.name AS country
    , sum(c.population) AS urban_pop
    , f.population AS total_pop
    , sum(c.population) / CAST(f.population AS Float) AS urban_pct
FROM facts f 
LEFT JOIN cities c 
ON f.id = c.facts_id 
GROUP BY f.name, f.population
HAVING sum(c.population) / CAST(f.population AS Float) > 0.5
ORDER BY 4 ASC
