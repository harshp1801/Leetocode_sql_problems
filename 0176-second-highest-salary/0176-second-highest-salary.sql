# Write your MySQL query statement below
with Employee_salary as 
    (
    select 
        salary,
        dense_rank() over (order by salary desc) as rnk 
        from Employee
    )
select max(salary) SecondHighestSalary from 
    (select salary from Employee_salary
        where rnk = 2
    union
    select null) as a