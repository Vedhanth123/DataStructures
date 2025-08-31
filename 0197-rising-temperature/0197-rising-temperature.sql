# Write your MySQL query statement below

WITH WeatherWithLag AS (
    -- Step 1: Create a CTE with current temp and previous day's temp/date
    SELECT
        id,
        recordDate,
        temperature,
        LAG(temperature, 1) OVER (ORDER BY recordDate) AS previous_temp,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) AS previous_date
    FROM
        Weather
)
-- Step 2: Select from the CTE where the conditions are met
SELECT
    id
FROM
    WeatherWithLag
WHERE
    temperature > previous_temp
    AND DATEDIFF(recordDate, previous_date) = 1;