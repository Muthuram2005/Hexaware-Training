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
