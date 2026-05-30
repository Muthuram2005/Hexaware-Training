create database retail_db;
use retail_db;
create table customers (customer_id int, customer_name varchar(30), city varchar(50));
insert into customers(customer_id, customer_name, city) values(1,'Rahul','Chennai'),(2,'Bala','Mumbai'),(3,'Raja','Bangalore');
select * from customers;

use retail_db;
create table products(product_id int primary key, product_name varchar(100), category varchar(50), price decimal(10,2),
stock_quantity int, supplier_city varchar(50));
drop table products;
insert into products(product_id, product_name, category, price, stock_quantity, supplier_city) values
(1,'Laptop','Electronics',54999.50,80,'Chennai'),
(2,'Chair','Furniture',4999.50,60,'Mumbai'),
(3,'Bottle','Kitchen',499.50,150,'Bangalore');
select * from products;

-- distinct
select distinct(city) from customers;
-- in
select * from customers where city in ('chennai', 'mumbai');
-- not in
select * from customers where city not in ('chennai', 'mumbai');
-- between
select * from products where price between 500 and 10000;
-- not between
select * from products where price not between 500 and 10000;
-- like 
select * from products where product_name like 'l%';
select * from products where product_name like '%r';
select * from products where product_name like '%top%';
select * from products where product_name like 'l_';
select * from products where product_name like '_r';
select * from products where product_name like '_top_';
-- order by 
select * from products order by price asc;
select * from products order by price desc;
-- count
select count(*) as total_products from products;
-- sum
select sum(stock_quantity) as total_stock from products;
-- avg
select avg(price) as average_price from products;
-- max
select max(price) as highest_price from products;
-- min
select min(price) as lowest_price from products;
-- group by
select category, count(*) as total_products from products
group by category;
-- having
select category, count(*) as total_products from products
group by category
having count(*) > 0;
