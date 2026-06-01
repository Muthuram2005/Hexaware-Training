-- Basic Queries -- 
-- 1
select * from patients;
-- 2
select * from doctors;
-- 3
select * from patients where city = 'Hyderabad';
-- 4
select d.* from doctors d
join departments dp on d.department_id = dp.department_id where dp.department_name = 'Cardiology';
-- 5
select * from appointments where appointment_date > '2026-01-01';
-- 6
select * from appointments where appointment_status = 'Cancelled';
-- 7
select * from bills where total_amount > 5000;
-- 8
select * from payments where payment_mode = 'UPI';
-- 9
select * from patients where age between 30 and 50;
-- 10
select * from doctors where consultation_fee > 800;

-- Aggregate Queries --
-- 11
select count(*) as total_patients from patients;
-- 12
select count(*) as total_doctors from doctors;
-- 13
select count(*) as total_appointments from appointments;
-- 14
select avg(consultation_fee) as average_fee from doctors;
-- 15
select max(treatment_cost) as highest_treatment_cost from treatments;
-- 16
select sum(total_amount) as total_billing from bills;
-- 17
select sum(paid_amount) as total_paid_amount from payments;
-- 18
select city, count(*) as patient_count from patients group by city;
-- 19
select specialization, count(*) as doctor_count from doctors group by specialization;
-- 20
select appointment_status, count(*) as total_appointments from appointments group by appointment_status;

-- Joins --
-- 21
select p.patient_name, a.appointment_date, a.appointment_status from patients p
join appointments a on p.patient_id = a.patient_id;
-- 22
select d.doctor_name, dp.department_name from doctors d
join departments dp on d.department_id = dp.department_id;
-- 23
select p.patient_name, d.doctor_name, a.appointment_date from appointments a
join patients p on a.patient_id = p.patient_id
join doctors d on a.doctor_id = d.doctor_id;
-- 24
select a.appointment_id, t.treatment_name, t.treatment_cost from appointments a
join treatments t on a.appointment_id = t.appointment_id;
-- 25
select b.bill_id, p.patient_name, b.total_amount from bills b
join patients p on b.patient_id = p.patient_id;
-- 26
select b.bill_id, p.payment_mode, p.paid_amount, p.payment_status from bills b
join payments p on b.bill_id = p.bill_id;
-- 27
select p.patient_name, d.doctor_name, dp.department_name, a.appointment_date, a.appointment_status, t.treatment_name, t.treatment_cost, b.total_amount, py.payment_status from appointments a
join patients p on a.patient_id = p.patient_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id
left join treatments t on a.appointment_id = t.appointment_id
left join bills b on a.appointment_id = b.appointment_id
left join payments py on b.bill_id = py.bill_id;

-- GROUP BY and HAVING --
-- 28
select doctor_id, count(*) as appointment_count from appointments group by doctor_id;
-- 29
select dp.department_name, count(*) as appointment_count from appointments a
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id group by dp.department_name;
-- 30
select dp.department_name, sum(b.total_amount) as total_revenue from bills b
join appointments a on b.appointment_id = a.appointment_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id group by dp.department_name;
-- 31
select treatment_name, sum(treatment_cost) as total_treatment_cost from treatments group by treatment_name;
-- 32
select p.city, sum(b.total_amount) as total_billing from patients p
join bills b on p.patient_id = b.patient_id group by p.city;
-- 33
select doctor_id, count(*) as appointment_count from appointments
group by doctor_id having appointment_count > 2;
-- 34
select dp.department_name, sum(b.total_amount) as total_revenue from bills b
join appointments a on b.appointment_id = a.appointment_id
join doctors d on a.doctor_id = d.doctor_id
join departments dp on d.department_id = dp.department_id group by dp.department_name having total_revenue > 20000;
-- 35
select city, count(*) as patient_count from patients group by city having patient_count > 2;

-- Subqueries --
-- 36
select * from patients where patient_id in
( select patient_id from appointments );
-- 37
select * from patients where patient_id not in
( select patient_id from appointments );
-- 38
select * from doctors where doctor_id not in
( select doctor_id from appointments );
-- 39
select * from bills where total_amount >
( select avg(total_amount) from bills );
-- 40
select * from patients where patient_id =
( select patient_id from bills order by total_amount desc limit 1 );
-- 41
select * from doctors where consultation_fee >
( select avg(consultation_fee) from doctors );
-- 42
select * from patients where patient_id in
( select a.patient_id from appointments a
  join doctors d on a.doctor_id = d.doctor_id
  join departments dp on d.department_id = dp.department_id where dp.department_name = 'Cardiology' );
-- 43
select * from bills where bill_status = 'Unpaid';
-- 44
select * from appointments where appointment_id in
( select appointment_id from treatments );
-- 45
select patient_id, sum(total_amount) as total_bill from bills group by patient_id having total_bill >
( select avg(patient_total) from
  ( select sum(total_amount) as patient_total from bills group by patient_id ) x
);

-- Data Quality Checks -- 
-- 46
select * from appointments where appointment_id not in
( select appointment_id from treatments );
-- 47
select * from bills where bill_id not in
( select bill_id from payments );
-- 48
select * from payments where paid_amount is null or paid_amount = 0;
-- 49
select * from appointments a
join bills b on a.appointment_id = b.appointment_id where a.appointment_status = 'Cancelled';
-- 50
select b.bill_id, b.total_amount, p.paid_amount from bills b
join payments p on b.bill_id = p.bill_id where p.payment_status = 'Paid' and p.paid_amount < b.total_amount;
-- 51
select * from doctors d
left join departments dp on d.department_id = dp.department_id where dp.department_id is null;
-- 52
select * from appointments a
left join patients p on a.patient_id = p.patient_id
left join doctors d on a.doctor_id = d.doctor_id where p.patient_id is null or d.doctor_id is null;

-- Final Reports --
-- Report 1
select p.patient_name, p.city, count(distinct a.appointment_id) as total_appointments,
    coalesce(sum(b.total_amount),0) as total_bill_amount,
    coalesce(sum(py.paid_amount),0) as total_paid_amount,
    coalesce(sum(b.total_amount),0) -
    coalesce(sum(py.paid_amount),0) as pending_amount
from patients p
left join appointments a on p.patient_id = a.patient_id
left join bills b on p.patient_id = b.patient_id
left join payments py on b.bill_id = py.bill_id
group by p.patient_id, p.patient_name, p.city;
