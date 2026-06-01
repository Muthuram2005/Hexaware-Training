-- Basic Queries --
-- 1
select * from customers;
-- 2 
select customer_name, city, membership_type from customers;
-- 3 
select * from products order by price desc;
-- 4 
select * from customers where city = 'Hyderabad';
-- 5 
select * from customers where membership_type = 'Gold';
-- 6
select * from products where price between 500 and 5000;
-- 7
select * from products where category in ('Electronics', 'Fashion');
-- 8
select * from orders where order_date > '2026-01-01';
-- 9 
select * from payments where payment_mode = 'UPI';
-- 10 
select * from deliveries where delivery_status = 'Pending';

-- Aggregate Queries --
-- 11
select count(*) as total_customers from customers;
-- 12
select count(*) as total_orders from orders;
-- 13
select count(*) as total_products from products;
-- 14
select sum(amount) as total_revenue from payments where payment_status = 'Success';
-- 15
select avg(amount) as average_payment from payments;
-- 16 
select max(amount) as highest_payment from payments;
-- 17
select min(amount) as lowest_payment from payments;
-- 18
select city, count(*) as total_customers from customers group by city;
-- 19
select category, count(*) as total_products from products group by category;
-- 20
select order_status, count(*) as total_orders from orders group by order_status;

-- Joins --
-- 21
select c.customer_name, o.order_id, o.order_date from customers c 
join orders o on c.customer_id = o.customer_id;
-- 22 
select o.order_id, p.product_name, o.quantity, p.price from order_items o
join products p on o.product_id = p.product_id;
-- 23
select c.customer_name, p.product_name, o1.quantity, o.order_date from customers c 
join orders o on c.customer_id = o.customer_id
join order_items o1 on o.order_id = o1.order_id
join products p on o1.product_id = p.product_id; 
-- 24
select o.order_id, p.payment_mode, p.payment_status, p.amount from orders o
join payments p on o.order_id = p.order_id;
-- 25
select o.order_id, d.delivery_partner, d.delivery_status from orders o 
join deliveries d on o.order_id = d.order_id;
-- 26
select c.customer_name, c.city, o.order_id, o.order_date, p.product_name, p.category, o1.quantity, p.price, p1.payment_status, d.delivery_status from customers c 
join orders o on c.customer_id = o.customer_id
join order_items o1 on o.order_id = o1.order_id
join products p on o1.product_id = p.product_id
join payments p1 on o.order_id = p1.order_id
join deliveries d on o.order_id = d.order_id;

-- GROUP BY and HAVING -- 
-- 27
select c.city, sum(p.amount) as total_revenue from customers c
join orders o on c.customer_id = o.customer_id
join payments p on o.order_id = p.order_id
where p.payment_status = 'Success' group by c.city;
-- 28
select c.customer_name, sum(p.amount) as total_revenue from customers c
join orders o on c.customer_id = o.customer_id
join payments p on o.order_id = p.order_id
where p.payment_status = 'Success' group by c.customer_name;
-- 29
select p.product_name, sum(o.quantity) as total_quantity from products p
join order_items o on p.product_id = o.product_id group by p.product_name;
-- 30
select p.category, sum(o.quantity * p.price) as revenue from products p 
join order_items o on p.product_id = o.product_id group by p.category;
-- 31
select c.customer_name, count(o.order_id) as total_orders from customers c 
join orders o on c.customer_id = o.customer_id group by c.customer_name;
-- 32
select c.customer_name, count(o.order_id) as total_orders from customers c 
join orders o on c.customer_id = o.customer_id group by c.customer_name having total_orders > 1;
-- 33
select p.category, sum(o.quantity * p.price) as revenue from products p 
join order_items o on p.product_id = o.product_id group by p.category having revenue > 10000;
-- 34
select city, count(*) as total_customers from customers group by city having total_customers > 2;
-- 35
select p.product_name, sum(o.quantity) as total_sold from products p 
join order_items o on p.product_id = o.product_id group by p.product_name having total_sold > 3;

-- Subqueries -- 
-- 36
select * from customers where customer_id in 
( select customer_id from orders );
-- 37 
select * from customers where customer_id not in 
( select customer_id from orders );
-- 38
select * from products where product_id not in 
( select product_id from order_items );
-- 39
select o.* from orders o 
join payments p on o.order_id = p.order_id where p.amount > 
( select avg(amount) from payments );
-- 40 
select c.customer_name, p.amount from customers c 
join orders o on c.customer_id = o.customer_id
join payments p on o.order_id = p.order_id where p.amount = 
( select max(amount) from payments );
-- 41
select * from products where price >
( select avg(price) from products );
-- 42
select distinct c.customer_name from customers c 
join orders o on c.customer_id = o.customer_id 
join order_items o1 on o.order_id = o1.order_id 
where o1.product_id in ( select product_id from products where category = 'Electronics' );
-- 43
select * from orders where order_id in
( select order_id from payments where payment_status = 'Success' );
-- 44
select * from orders where order_id not in 
( select order_id from deliveries where delivery_status = 'Delivered' );
-- 45
select customer_name from
( select c.customer_id, c.customer_name, sum(p.amount) as total_spending from customers c
  join orders o on c.customer_id = o.customer_id
  join payments p on o.order_id = p.order_id
  where p.payment_status = 'Success'
  group by c.customer_id, c.customer_name
) t where total_spending >
( select avg(total_spending) from
    ( select sum(p.amount) as total_spending from customers c
	  join orders o on c.customer_id = o.customer_id
	  join payments p on o.order_id = p.order_id
	  where p.payment_status = 'Success' group by c.customer_id
    ) x
);

-- Data Quality Checks --
-- 46
select o.* from orders o 
left join payments p on o.order_id = p.order_id where p.order_id is null;
-- 47
select o.* from orders o 
left join deliveries d on o.order_id = d.order_id where d.order_id is null;
-- 48
select * from payments where amount is null or amount = 0;
-- 49
select o.order_id, o.order_status, p.payment_status from orders o 
join payments p on o.order_id = p.order_id where o.order_status = 'Cancelled' and p.payment_status = 'Success';
-- 50
select o.order_id, d.delivery_status, p.payment_status from orders o 
join deliveries d on o.order_id = d.order_id
join payments p on o.order_id = p.order_id where d.delivery_status = 'Delivered' and p.payment_status = 'Failed';
-- 51
select o.* from order_items o 
left join products p on o.product_id = p.product_id where p.product_id is null; 
-- 52
select o.* from orders o 
left join customers c on o.customer_id = c.customer_id where c.customer_id is null; 
