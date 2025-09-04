delete from Person
where id in 
        (select id 
            from (select 
            id,email,
            row_number() over (partition by email order by id) rnk 
            from Person) as a
        where rnk <> 1)
