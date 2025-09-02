select distinct ConsecutiveNums 
    from(
        select 
            case 
                when num = l1 and l1 = l2 then num end as ConsecutiveNums
        from  
            (select 
                id,num,
                lead(num,1) over (order by id) l1,
                lead(num,2) over (order by id) l2
                from logs
                ) as a) as b
    where ConsecutiveNums is not null