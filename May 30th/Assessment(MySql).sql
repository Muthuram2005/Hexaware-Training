-- 1
select * from books;

-- 2
select book_title, category, price from books;

-- 3
select distinct category from books;

-- 4
select * from books where category = 'Programming';

-- 5
select * from books where price > 700;

-- 6
select * from books where stock < 15;

-- 7
select * from books where category in ('Programming','Database','AI');

-- 8
select * from books where price between 500 and 900;

-- 9
select * from books where book_title like '%SQL%';

-- 10
select * from books where book_title like 'Data%';

-- 11
select * from books order by price desc;

-- 12
select * from books order by category asc, price desc;

-- 13
select count(*) as total_books from books;

-- 14
select max(price) as highest_price from books;

-- 15
select min(price) as lowest_price from books;

-- 16
select avg(price) as average_price from books;

-- 17
select sum(stock) as total_stock from books;

-- 18
select category, count(*) as total_books from books
group by category;

-- 19
select category, avg(price) as avg_price from books
group by category;

-- 20
select category, sum(stock) as total_stock from books
group by category;

-- 21
select category, count(*) as total_books from books
group by category
having count(*) > 1;

-- 22
select category, avg(price) as avg_price from books
group by category
having avg(price) > 700;

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

-- 35
select * from customers_new where customer_id in
(
  select customer_id from payments where customer_id is not null
);

-- 36
select * from customers_new c where not exists
(
  select * from payments p where p.customer_id = c.customer_id
);

-- 37
select * from payments where amount > 
( 
  select avg(amount) from payments
);

-- 38
select * from customers_new where customer_id =
(
  select customer_id from payments where amount =
  (
    select max(amount) from payments
  )
);

-- 39
select * from customers_new where membership_type = 'Gold' and customer_id in
(
  select customer_id from payments
);

-- 40
select customer_id, sum(amount) as total_payment from payments
group by customer_id
having sum(amount) > 10000;

-- 41
select * from payments p where not exists
(
  select * from customers_new c where c.customer_id = p.customer_id
);

-- 42
select * from customers_new c where exists
(
  select * from payments p where p.customer_id = c.customer_id
);

-- 43
select * from customers_new c where not exists
(
  select * from payments p where p.customer_id = c.customer_id
);

-- 44
select * from payments where amount > all
(
  select amount from payments where customer_id = 2
);
