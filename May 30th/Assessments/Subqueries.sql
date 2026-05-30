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
