select 
    Department, Employee, Salary 
    from (select 
            dept.name Department, emp.name Employee, emp.salary Salary,
            Dense_rank() over (partition by dept.name order by emp.salary desc) rnk 
            from Employee emp join Department dept
            on emp.departmentId = dept.id) as a
    where rnk<=3
