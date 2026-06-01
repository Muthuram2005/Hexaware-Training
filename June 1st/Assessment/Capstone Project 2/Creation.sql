-- Database creation & using
create database hospital_management;
use hospital_management;

-- patients
create table patients (
    patient_id int primary key,
    patient_name varchar(100),
    gender varchar(10),
    age int,
    city varchar(50),
    phone varchar(15)
);

-- departments
create table departments (
    department_id int primary key,
    department_name varchar(100)
);

-- doctors
create table doctors (
    doctor_id int primary key,
    doctor_name varchar(100),
    specialization varchar(100),
    department_id int,
    consultation_fee decimal(10,2),
    foreign key (department_id)
    references departments(department_id)
);

-- appointments
create table appointments (
    appointment_id int primary key,
    patient_id int,
    doctor_id int,
    appointment_date date,
    appointment_status varchar(30),
    foreign key (patient_id)
    references patients(patient_id),
    foreign key (doctor_id)
    references doctors(doctor_id)
);

-- treatments
create table treatments (
    treatment_id int primary key,
    appointment_id int,
    treatment_name varchar(100),
    treatment_cost decimal(10,2),
    foreign key (appointment_id)
    references appointments(appointment_id)
);

-- bills
create table bills (
    bill_id int primary key,
    patient_id int,
    appointment_id int,
    bill_date date,
    total_amount decimal(10,2),
    bill_status varchar(30),
    foreign key (patient_id)
    references patients(patient_id),
    foreign key (appointment_id)
    references appointments(appointment_id)
);

-- payments 
create table payments (
    payment_id int primary key,
    bill_id int,
    payment_mode varchar(30),
    paid_amount decimal(10,2),
    payment_status varchar(30),
    foreign key (bill_id)
    references bills(bill_id)
);
