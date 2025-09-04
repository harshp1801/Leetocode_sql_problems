select 
    Department,Employee,Salary 
    from (select 
            dept.name Department,emp.name Employee, Salary, 
            Dense_rank() over (partition by departmentId order by salary desc) rnk
            from Employee emp join Department dept
            on emp.departmentId = dept.id) as a
    where rnk = 1
