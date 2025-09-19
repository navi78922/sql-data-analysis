Top 5 airlines with the most flights

SELECT airline, COUNT(*) AS total_flights
FROM airlines_flights_data
GROUP BY airline
ORDER BY total_flights DESC
LIMIT 5;

Average ticket price by class

SELECT class, AVG(price) AS avg_price
FROM airlines_flights_data
GROUP BY class;

Most popular source–destination route

SELECT source_city, destination_city, COUNT(*) AS total_flights
FROM airlines_flights_data
GROUP BY source_city, destination_city
ORDER BY total_flights DESC

4. Average flight price depending on days left

SELECT days_left, AVG(price) AS avg_price
FROM airlines_flights_data
GROUP BY days_left
ORDER BY days_left;
5. Average flight duration by airline

SELECT airline, AVG(duration) AS avg_duration
FROM airlines_flights_data
GROUP BY airline
ORDER BY avg_duration DESC;

LIMIT 5;
