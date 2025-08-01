-- 101. Average temperature (Fahrenheit) by city, ordered descending

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
