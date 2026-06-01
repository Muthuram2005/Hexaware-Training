-- customers
insert into customers values
(1,'Rahul Sharma','Hyderabad','Telangana','Male','Gold'),
(2,'Priya Reddy','Hyderabad','Telangana','Female','Silver'),
(3,'Amit Kumar','Bangalore','Karnataka','Male','Gold'),
(4,'Sneha Rao','Mumbai','Maharashtra','Female','Platinum'),
(5,'Vikram Singh','Delhi','Delhi','Male','Silver'),
(6,'Anjali Verma','Chennai','Tamil Nadu','Female','Gold'),
(7,'Rohit Jain','Pune','Maharashtra','Male','Silver'),
(8,'Kiran Patel','Ahmedabad','Gujarat','Female','Gold'),
(9,'Arjun Das','Kolkata','West Bengal','Male','Silver'),
(10,'Meera Nair','Kochi','Kerala','Female','Platinum');

-- products
insert into products values
(101,'Laptop','Electronics',55000),
(102,'Smartphone','Electronics',25000),
(103,'Headphones','Electronics',2000),
(104,'T-Shirt','Fashion',800),
(105,'Jeans','Fashion',1800),
(106,'Shoes','Fashion',3000),
(107,'Mixer','Home Appliances',4000),
(108,'Watch','Accessories',5000),
(109,'Backpack','Accessories',1200),
(110,'Tablet','Electronics',18000);

-- orders
insert into orders VALUES
(1001,1,'2026-01-05','Completed'),
(1002,2,'2026-01-10','Completed'),
(1003,3,'2026-01-15','Cancelled'),
(1004,4,'2026-01-20','Completed'),
(1005,5,'2026-01-25','Pending'),
(1006,1,'2026-02-01','Completed'),
(1007,6,'2026-02-03','Completed'),
(1008,7,'2026-02-05','Completed'),
(1009,8,'2026-02-08','Cancelled'),
(1010,9,'2026-02-10','Completed'),
(1011,10,'2026-02-12','Completed'),
(1012,2,'2026-02-15','Pending'),
(1013,3,'2026-02-18','Completed'),
(1014,4,'2026-02-20','Completed'),
(1015,5,'2026-02-22','Completed');

-- order_items
insert into order_items values
(1,1001,101,1),
(2,1001,103,2),
(3,1002,104,3),
(4,1002,105,1),
(5,1003,102,1),
(6,1004,110,1),
(7,1005,107,1),
(8,1006,108,2),
(9,1006,109,1),
(10,1007,101,1),
(11,1008,106,2),
(12,1009,102,1),
(13,1010,103,3),
(14,1011,104,2),
(15,1012,105,2),
(16,1013,110,1),
(17,1014,101,1),
(18,1014,108,1),
(19,1015,107,2),
(20,1015,109,2);

-- payments
insert into payments values
(1,1001,'UPI','Success',59000),
(2,1002,'Card','Success',4200),
(3,1003,'UPI','Failed',25000),
(4,1004,'Net Banking','Success',18000),
(5,1005,'UPI','Pending',4000),
(6,1006,'Card','Success',11200),
(7,1007,'UPI','Success',55000),
(8,1008,'Card','Success',6000),
(9,1009,'UPI','Failed',25000),
(10,1010,'Net Banking','Success',6000),
(11,1011,'UPI','Success',1600),
(12,1012,'Card','Pending',3600),
(13,1013,'UPI','Success',18000),
(14,1014,'Card','Success',60000),
(15,1015,'UPI','Success',10400);

-- deliveries
insert into deliveries values
(1,1001,'Delhivery','Delivered','Hyderabad'),
(2,1002,'BlueDart','Delivered','Hyderabad'),
(3,1003,'Delhivery','Cancelled','Bangalore'),
(4,1004,'Ecom Express','Delivered','Mumbai'),
(5,1005,'BlueDart','Pending','Delhi'),
(6,1006,'Delhivery','Delivered','Hyderabad'),
(7,1007,'Ecom Express','Delivered','Chennai'),
(8,1008,'BlueDart','Delivered','Pune'),
(9,1009,'Delhivery','Cancelled','Ahmedabad'),
(10,1010,'BlueDart','Delivered','Kolkata'),
(11,1011,'Ecom Express','Delivered','Kochi'),
(12,1012,'Delhivery','Pending','Hyderabad'),
(13,1013,'BlueDart','Delivered','Bangalore'),
(14,1014,'Ecom Express','Delivered','Mumbai'),
(15,1015,'Delhivery','Delivered','Delhi');
