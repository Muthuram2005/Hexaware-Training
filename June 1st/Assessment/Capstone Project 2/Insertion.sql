-- patients
insert into patients values
(101,'Rahul Sharma','Male',35,'Hyderabad','9876543210'),
(102,'Priya Reddy','Female',29,'Bangalore','9876543211'),
(103,'Arjun Kumar','Male',42,'Chennai','9876543212'),
(104,'Sneha Patel','Female',31,'Hyderabad','9876543213'),
(105,'Vikram Singh','Male',50,'Mumbai','9876543214'),
(106,'Anjali Verma','Female',27,'Delhi','9876543215'),
(107,'Rohit Gupta','Male',39,'Pune','9876543216'),
(108,'Kavya Nair','Female',45,'Hyderabad','9876543217'),
(109,'Manoj Das','Male',33,'Chennai','9876543218'),
(110,'Deepika Rao','Female',37,'Bangalore','9876543219'),
(111,'Suresh Iyer','Male',48,'Mumbai','9876543220'),
(112,'Neha Jain','Female',30,'Hyderabad','9876543221');

-- departments
insert into departments values
(1,'Cardiology'),
(2,'Neurology'),
(3,'Orthopedics'),
(4,'Pediatrics'),
(5,'Dermatology');

-- doctors
insert into doctors values
(201,'Dr. Amit','Cardiologist',1,1000),
(202,'Dr. Kiran','Neurologist',2,1200),
(203,'Dr. Meena','Orthopedic',3,900),
(204,'Dr. Raj','Pediatrician',4,700),
(205,'Dr. Priya','Dermatologist',5,800),
(206,'Dr. Arvind','Cardiologist',1,1100),
(207,'Dr. Swathi','Neurologist',2,1300),
(208,'Dr. Nitin','Orthopedic',3,950);

-- appointments
insert into appointments values
(301,101,201,'2026-01-05','Completed'),
(302,102,202,'2026-01-07','Completed'),
(303,103,203,'2026-01-10','Cancelled'),
(304,104,204,'2026-01-11','Completed'),
(305,105,205,'2026-01-12','Completed'),
(306,106,206,'2026-01-13','Completed'),
(307,107,207,'2026-01-14','Pending'),
(308,108,208,'2026-01-15','Completed'),
(309,109,201,'2026-01-16','Completed'),
(310,110,202,'2026-01-17','Completed'),
(311,111,203,'2026-01-18','Completed'),
(312,112,204,'2026-01-19','Cancelled'),
(313,101,205,'2026-01-20','Completed'),
(314,102,206,'2026-01-21','Completed'),
(315,103,207,'2026-01-22','Completed'),
(316,104,208,'2026-01-23','Pending'),
(317,105,201,'2026-01-24','Completed'),
(318,106,202,'2026-01-25','Completed'),
(319,107,203,'2026-01-26','Completed'),
(320,108,204,'2026-01-27','Completed');

-- treatments
insert into treatments values
(401,301,'ECG',1500),
(402,302,'Brain Scan',4000),
(403,304,'Vaccination',1200),
(404,305,'Skin Treatment',2500),
(405,306,'Heart Checkup',3000),
(406,308,'Bone X-Ray',1800),
(407,309,'ECG',1500),
(408,310,'MRI Scan',4500),
(409,311,'Fracture Treatment',5000),
(410,313,'Skin Allergy Treatment',2200),
(411,314,'Heart Surgery Consultation',6000),
(412,315,'Neuro Therapy',5500),
(413,317,'ECG',1500),
(414,318,'Brain Scan',4000),
(415,319,'Joint Treatment',3500);

-- bills
insert into bills values
(501,101,301,'2026-01-05',2500,'Paid'),
(502,102,302,'2026-01-07',5500,'Paid'),
(503,104,304,'2026-01-11',2000,'Paid'),
(504,105,305,'2026-01-12',3500,'Paid'),
(505,106,306,'2026-01-13',4500,'Paid'),
(506,108,308,'2026-01-15',2800,'Paid'),
(507,109,309,'2026-01-16',2500,'Paid'),
(508,110,310,'2026-01-17',6500,'Paid'),
(509,111,311,'2026-01-18',7000,'Unpaid'),
(510,101,313,'2026-01-20',3200,'Paid'),
(511,102,314,'2026-01-21',8000,'Paid'),
(512,103,315,'2026-01-22',7500,'Unpaid'),
(513,105,317,'2026-01-24',2500,'Paid'),
(514,106,318,'2026-01-25',5500,'Paid'),
(515,107,319,'2026-01-26',4800,'Pending');

-- payments
insert into payments values
(601,501,'UPI',2500,'Paid'),
(602,502,'Credit Card',5500,'Paid'),
(603,503,'Cash',2000,'Paid'),
(604,504,'UPI',3500,'Paid'),
(605,505,'Debit Card',4500,'Paid'),
(606,506,'UPI',2800,'Paid'),
(607,507,'Cash',2500,'Paid'),
(608,508,'Credit Card',6500,'Paid'),
(609,509,'UPI',0,'Pending'),
(610,510,'Cash',3200,'Paid'),
(611,511,'UPI',8000,'Paid'),
(612,512,'Credit Card',0,'Pending'),
(613,513,'Debit Card',2500,'Paid'),
(614,514,'UPI',5500,'Paid'),
(615,515,'Cash',3000,'Partial');
