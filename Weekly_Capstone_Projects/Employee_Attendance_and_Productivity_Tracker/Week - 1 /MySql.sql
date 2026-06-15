-- DATABASE
CREATE DATABASE EmployeeAttendanceDB;
USE EmployeeAttendanceDB;

-- Employees Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department VARCHAR(50),
    designation VARCHAR(50),
    joining_date DATE
);

-- Attendance Table
CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY,
    employee_id INT,
    attendance_date DATE,
    clock_in TIME,
    clock_out TIME,
    status VARCHAR(20),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Tasks Table
CREATE TABLE tasks (
    task_id INT PRIMARY KEY,
    employee_id INT,
    task_name VARCHAR(100),
    task_status VARCHAR(30),
    tasks_completed INT,
    task_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Insert Data
INSERT INTO employees VALUES
(101,'Rahul Sharma','IT','Software Engineer','2023-01-15'),
(102,'Priya Singh','HR','HR Executive','2022-06-10'),
(103,'Arjun Kumar','Finance','Accountant','2021-09-20');

INSERT INTO attendance VALUES
(1001,101,'2026-06-01','09:00:00','18:00:00','Present'),
(1002,102,'2026-06-01','09:15:00','18:10:00','Present'),
(1003,103,'2026-06-01','08:50:00','17:45:00','Present');

INSERT INTO tasks VALUES
(201,101,'Bug Fixing','Completed',8,'2026-06-01'),
(202,102,'Recruitment Drive','Completed',5,'2026-06-01'),
(203,103,'Financial Audit','Completed',4,'2026-06-01');

-- CRUD Operations
-- CREATE
-- 1
INSERT INTO employees
VALUES (104,'Sneha Patel','IT','QA Engineer','2024-02-10');
-- 2
INSERT INTO employees
VALUES (105,'Vikram Rao','Sales','Sales Executive','2023-08-15');
-- 3
INSERT INTO attendance
VALUES (1004,104,'2026-06-02','09:10:00','18:15:00','Present');
-- 4
INSERT INTO attendance
VALUES (1005,105,'2026-06-02','09:20:00','18:00:00','Present');
-- 5
INSERT INTO tasks
VALUES (204,104,'Test Case Execution','Completed',7,'2026-06-02');
-- 6
INSERT INTO tasks
VALUES (205,105,'Client Meeting','Completed',6,'2026-06-02');

-- READ
-- 1
SELECT * FROM employees;
-- 2
SELECT employee_id, employee_name, department FROM employees
WHERE department='IT';
-- 3
SELECT * FROM attendance
WHERE status='Present';
-- 4
SELECT employee_name, designation FROM employees
WHERE employee_id IN
(
    SELECT employee_id FROM attendance
);
-- 5
SELECT e.employee_name, SUM(t.tasks_completed) AS total_tasks FROM employees e
JOIN tasks t ON e.employee_id=t.employee_id
GROUP BY e.employee_name;
-- 6
SELECT e.employee_name, a.attendance_date, a.status, t.task_name, t.tasks_completed FROM employees e
JOIN attendance a ON e.employee_id=a.employee_id
JOIN tasks t ON e.employee_id=t.employee_id;

-- UPDATE
-- 1
UPDATE employees SET designation='Senior Software Engineer'
WHERE employee_id=101;
-- 2
UPDATE employees SET department='Operations'
WHERE employee_id=105;
-- 3
SET SQL_SAFE_UPDATES = 0;
UPDATE attendance SET status='Late'
WHERE clock_in > '09:15:00';
SET SQL_SAFE_UPDATES = 1;
-- 4
UPDATE attendance SET status='Absent'
WHERE clock_in IS NULL;
-- 5
UPDATE tasks SET tasks_completed=10
WHERE task_id=201;
-- 6
UPDATE tasks SET task_status='In Progress'
WHERE task_id=205;

-- DELETE
-- 1
DELETE FROM tasks
WHERE task_id=205;
-- 2
DELETE FROM attendance
WHERE attendance_id=1005;
-- 3
DELETE FROM employees
WHERE employee_id=105;
-- 4
DELETE FROM tasks
WHERE tasks_completed < 5;
-- 5
DELETE FROM attendance
WHERE status='Absent';
-- 6
DELETE FROM employees
WHERE employee_id NOT IN
(
    SELECT DISTINCT employee_id FROM attendance
);

-- Stored Procedure
-- 1
DELIMITER //
CREATE PROCEDURE GetWorkingHours(
    IN p_employee_id INT
)
BEGIN
    SELECT employee_id, attendance_date, TIMESTAMPDIFF( HOUR, CONCAT(attendance_date,' ',clock_in), CONCAT(attendance_date,' ',clock_out)) AS total_working_hours FROM attendance
    WHERE employee_id=p_employee_id;
END //
DELIMITER ;
-- Execution
CALL GetWorkingHours(101);

-- 2
DELIMITER //
CREATE PROCEDURE GetAttendanceReport(
    IN p_employee_id INT
)
BEGIN
    SELECT * FROM attendance
    WHERE employee_id=p_employee_id;
END //
DELIMITER ;
-- Execution
CALL GetAttendanceReport(101);

-- 3
DELIMITER //
CREATE PROCEDURE GetDepartmentWiseEmployees()
BEGIN
    SELECT department, COUNT(*) AS employee_count FROM employees
    GROUP BY department;
END //
DELIMITER ;
-- Execution
CALL GetDepartmentWiseEmployees();

-- 4
DELIMITER //
CREATE PROCEDURE GetEmployeeProductivity(
    IN p_employee_id INT
)
BEGIN
    SELECT e.employee_id, e.employee_name, SUM(t.tasks_completed) AS total_tasks_completed FROM employees e
    JOIN tasks t ON e.employee_id=t.employee_id
    WHERE e.employee_id=p_employee_id
    GROUP BY e.employee_id,e.employee_name;
END //
DELIMITER ;
-- Execution
CALL GetEmployeeProductivity(101);

-- 5
DELIMITER //
CREATE PROCEDURE GetTopPerformers()
BEGIN
    SELECT e.employee_id, e.employee_name, SUM(t.tasks_completed) AS total_tasks FROM employees e
    JOIN tasks t ON e.employee_id=t.employee_id
    GROUP BY e.employee_id,e.employee_name
    ORDER BY total_tasks DESC
    LIMIT 5;
END //
DELIMITER ;
-- Execution
CALL GetTopPerformers();

-- 6
DELIMITER //
CREATE PROCEDURE GetLowPerformers(
    IN p_min_tasks INT
)
BEGIN
    SELECT e.employee_id, e.employee_name, SUM(t.tasks_completed) AS total_tasks FROM employees e
    JOIN tasks t ON e.employee_id=t.employee_id
    GROUP BY e.employee_id,e.employee_name
    HAVING total_tasks < p_min_tasks;
END //
DELIMITER ;
-- Execution
CALL GetLowPerformers(10);

-- INDEXES
-- 1
CREATE INDEX idx_employee_id
ON attendance(employee_id);

SHOW INDEX FROM attendance
WHERE Key_name = 'idx_employee_id';

-- 2
CREATE INDEX idx_department
ON employees(department);

SHOW INDEX FROM employees
WHERE Key_name = 'idx_department';

-- 3
CREATE INDEX idx_task_employee
ON tasks(employee_id);

SHOW INDEX FROM tasks
WHERE Key_name = 'idx_task_employee';

-- 4
CREATE INDEX idx_attendance_date
ON attendance(attendance_date);

SHOW INDEX FROM attendance
WHERE Key_name = 'idx_attendance_date';

-- 5
CREATE INDEX idx_task_date
ON tasks(task_date);

SHOW INDEX FROM tasks
WHERE Key_name = 'idx_task_date';

-- 6
CREATE INDEX idx_employee_department
ON employees(employee_id, department);

SHOW INDEX FROM employees
WHERE Key_name = 'idx_employee_department';
