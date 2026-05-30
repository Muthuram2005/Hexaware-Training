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
