-- Database creation & using
create database retail_capstone_db;
use retail_capstone_db;

-- customers
create table customers (
    customer_id int primary key,
    customer_name varchar(100),
    city varchar(50),
    state varchar(50),
    gender varchar(10),
    membership_type varchar(30)
);

-- products
create table products (
    product_id int primary key,
    product_name varchar(100),
    category varchar(50),
    price decimal(10,2)
);

-- orders
create table orders (
    order_id int primary key,
    customer_id int,
    order_date date,
    order_status varchar(30),
    foreign key (customer_id)
    references customers(customer_id)
);

-- order_items
create table order_items (
    item_id int primary key,
    order_id int,
    product_id int,
    quantity int,
    foreign key (order_id)
    references orders(order_id),
    foreign key (product_id)
    references products(product_id)
);

-- payments
create table payments (
    payment_id int primary key,
    order_id int,
    payment_mode varchar(30),
    payment_status varchar(30),
    amount decimal(10,2),
    foreign key (order_id)
    references orders(order_id)
);

-- deliveries
create table deliveries (
    delivery_id int primary key,
    order_id int,
    delivery_partner varchar(50),
    delivery_status varchar(30),
    delivery_city varchar(50),
    foreign key (order_id)
    references orders(order_id)
);
