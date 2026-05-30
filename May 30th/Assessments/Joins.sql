-- 23
select e.employee_name, e.salary, d.department_name, d.location from employees e
inner join departments d
on e.department_id = d.department_id;

-- 24
select * from employees e
left join departments d
on e.department_id = d.department_id;

-- 25
select e.employee_name from employees e
left join departments d
on e.department_id = d.department_id
where d.department_id is null;

-- 26
select * from employees e
right join departments d
on e.department_id = d.department_id;

-- 27
select d.department_name from departments d
left join employees e
on d.department_id = e.department_id
where e.employee_id is null;

-- 28
select * from employees where salary is null;

-- 29
select * from employees where city is null;

-- 30
select * from departments where location is null;

-- 31
select d.department_name, count(e.employee_id) as employee_count from departments d
left join employees e
on d.department_id = e.department_id
group by d.department_name;

-- 32
select d.department_name, avg(e.salary) as avg_salary from departments d
left join employees e
on d.department_id = e.department_id
group by d.department_name;

-- 33
select d.department_name, count(e.employee_id) as employee_count from departments d
left join employees e
on d.department_id = e.department_id
group by d.department_name
having count(e.employee_id) > 2;

-- 34
select d.department_name, max(e.salary) as highest_salary from departments d
left join employees e
on d.department_id = e.department_id
group by d.department_name;
