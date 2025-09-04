select id
from (select 
    id,recordDate,temperature,
    lag(recordDate) over (order by recordDate) as nxt_dt,
    lag(temperature) over (order by recordDate) as nxt_temp
    from Weather) as a
where temperature>nxt_temp and datediff(recordDate,nxt_dt) = 1
