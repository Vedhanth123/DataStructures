# Write your MySQL query statement below
with Prevday as (

    select id,
    recordDate,
    temperature,
    lag(recordDate, 1) over (order by recordDate) as prev_date,
    lag(temperature, 1) over (order by recordDate) as prev_temp
    from Weather
)


select id
from Prevday
where temperature > prev_temp and
datediff(recordDate, prev_date) = 1