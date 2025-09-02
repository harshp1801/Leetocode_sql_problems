select email from 
    (select email,count(*) cnt from person
    group by email) as a
where cnt>1