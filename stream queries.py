# SELECT * FROM filtered_population ORDER BY updated_datetime DESC LIMIT 10;
#SELECT SUM(current_population) AS total_population FROM filtered_population;

# SELECT
#     YEAR(updated_datetime) AS year,
#     MONTH(updated_datetime) AS month,
#     SUM(current_population) AS total_population
# FROM
#     filtered_population
# GROUP BY
#     YEAR(updated_datetime), MONTH(updated_datetime)
# ORDER BY
#     year DESC, month DESC;

# Population growth rate over time query.
# SELECT
#     updated_datetime,
#     current_population,
#     LAG(current_population) OVER (ORDER BY updated_datetime) AS previous_population,
#     ((current_population - LAG(current_population) OVER (ORDER BY updated_datetime)) / LAG(current_population) OVER (ORDER BY updated_datetime)) * 100 AS growth_rate
# FROM
#     filtered_population;

'''
SELECT
    country,
    MAX(current_population) - MIN(current_population) AS population_change
FROM
    filtered_population
WHERE
    updated_datetime BETWEEN 'start_date' AND 'end_date'
GROUP BY
    country
ORDER BY
    population_change DESC
LIMIT 10;

,,,


''
#SELECT
    DAYOFWEEK(updated_datetime) AS day_of_week,
    AVG(current_population) AS average_population
FROM
    filtered_population
GROUP BY
    day_of_week
ORDER BY
    day_of_week;

'''