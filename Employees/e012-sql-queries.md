# Exercise: SQL Query Practice Lab

## Overview

In this exercise, you will practice DDL, DML, and DQL operations using a provided database schema. This is an **Implementation** exercise focusing on writing and executing SQL statements.

**Estimated Time:** 2-3 hours

---

## Setup

### Step 1: Create the Database

Connect to PostgreSQL and run the following setup script:

```sql
-- Create database
CREATE DATABASE sql_practice;
\c sql_practice

-- Create tables
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    budget DECIMAL(12, 2)
);

CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE DEFAULT CURRENT_DATE,
    salary DECIMAL(10, 2),
    dept_id INTEGER REFERENCES departments(dept_id)
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2),
    dept_id INTEGER REFERENCES departments(dept_id)
);

-- Insert sample data
INSERT INTO departments (dept_name, location, budget) VALUES
('Engineering', 'Building A', 500000),
('Sales', 'Building B', 300000),
('Marketing', 'Building C', 200000),
('HR', 'Building D', 150000);

INSERT INTO employees (first_name, last_name, email, hire_date, salary, dept_id) VALUES
('Alice', 'Johnson', 'alice@company.com', '2020-03-15', 85000, 1),
('Bob', 'Smith', 'bob@company.com', '2019-07-01', 72000, 1),
('Carol', 'Williams', 'carol@company.com', '2021-01-10', 65000, 2),
('David', 'Brown', 'david@company.com', '2018-11-20', 90000, 1),
('Eve', 'Davis', 'eve@company.com', '2022-05-01', 55000, 3),
('Frank', 'Miller', 'frank@company.com', '2020-09-15', 78000, 2),
('Grace', 'Wilson', 'grace@company.com', '2021-06-01', 62000, 4),
('Henry', 'Taylor', 'henry@company.com', '2019-03-01', 95000, 1);

INSERT INTO projects (project_name, start_date, end_date, budget, dept_id) VALUES
('Website Redesign', '2024-01-01', '2024-06-30', 50000, 3),
('Mobile App', '2024-02-15', '2024-12-31', 150000, 1),
('Sales Portal', '2024-03-01', '2024-09-30', 75000, 2),
('HR System', '2024-04-01', '2024-08-31', 40000, 4);
```

### Step 2: Verify Setup

```sql
SELECT * FROM departments;
SELECT * FROM employees;
SELECT * FROM projects;
```

---

## Part 1: DDL Practice (20 minutes)

Complete the following DDL operations:

### Task 1.1: Add a Column

Add a `phone` column (VARCHAR(20)) to the employees table.

```sql
alter table employees add column phone varchar(20);
```

### Task 1.2: Modify a Column

Change the `budget` column in departments to allow larger values (DECIMAL(15, 2)).

```sql
alter table departments alter column budget type decimal(15,2);
```

### Task 1.3: Create a New Table

Create a table called `training_courses` with:

- course_id (auto-incrementing primary key)
- course_name (required, VARCHAR(100))
- duration_hours (INTEGER)
- instructor (VARCHAR(100))

```sql
create table training_courses(course_id serial primary key, coursename varchar(100) not null, durationhours integer, instructor varchar(100));
```

---

## Part 2: DML Practice (30 minutes)

### Task 2.1: INSERT Operations

Add 3 new employees to the HR department:

- Grace Lee, <grace.lee@company.com>, salary 58000
- Ivan Chen, <ivan@company.com>, salary 61000
- Julia Kim, <julia@company.com>, salary 55000

```sql
insert into employees(firstname, lastname, email, salary, dept_id) VALUES
('Grace', 'Lee', 'grace.lee@company.com', 58000, 4),
('Ivan', 'Chen', 'ivan@company.com', 61000, 4),
('Julia', 'Kim', 'julia@company.com', 55000, 4);
```

### Task 2.2: UPDATE Operations

A) Give all Engineering department employees a 10% raise:

```sql
update employees set salary = salary * 1.1 where employees.dept_id = (select departments.dept_id from departments where dept_name = 'Engineering');
```

B) Update Bob Smith's email to <bob.smith@company.com>:

```sql
update employees set email = 'bob.smith@company.com' where firstname = 'Bob' and lastname = 'Smith'; 
```

### Task 2.3: DELETE Operations

A) Delete all projects that have already ended (end_date before today):

```sql
delete * from projects where enddate < current_date;
```

B) **CAREFUL!** Write (but don't run) a DELETE that would remove all employees without a department. What makes this dangerous?

```sql
/*delete * from employees where dept_id = null*/
-- Explain why this could be dangerous: I don't think that this is dangerous because the employees table is the child table. It is most dangerous when an entry from the parent table is being deleted because it could have a reference to it in the child table which is why delete on cascade exists to try to avoid orphaned records.
```

---

## Part 3: DQL Practice (60 minutes)

Write SELECT queries for each requirement:

### Basic Queries

**Query 3.1:** List all employees ordered by salary (highest first)

```sql
select * from employees order by salary desc;
```

**Query 3.2:** Find all employees in the Engineering department

```sql
select * from employees where employees.dept_id = (select departments.dept_id from departments where dept_name = 'Engineering');
```

**Query 3.3:** List employees hired in 2021 or later

```sql
select * from employees where hiredate.year >= 2021;
```

### Filtering and Operators

**Query 3.4:** Find employees with salary between 60000 and 80000

```sql
select * from employees where salary >= 60000 and salary <= 80000;
/* or this could also work*/
/*select * from employees where salary between 60000 and 80000;*/
```

**Query 3.5:** Find employees whose email contains 'company'

```sql
select * from employees where email like '%company%';
```

**Query 3.6:** List departments in Buildings A or B

```sql
select * from departments where location in ('Building A', 'Building B');
```

### Aggregate Functions

**Query 3.7:** Calculate the total salary expense per department

```sql
select dept_name, sum(salary) as salary_expense from employees join departments on employees.dept_id = departments.dept_id group by dept_name;
```

**Query 3.8:** Find the average, minimum, and maximum salary

```sql
select round(avg(salary),2) as average_salary, min(salary) as minimum_salary, max(salary) as maximum_salary from employees;
```

**Query 3.9:** Count employees in each department, only show departments with 2+ employees

```sql
select * from employees where dept_id in (select dept_id as numEmployees from employees GROUP BY dept_id HAVING count(dept_id) >= 2);
```

### Aliases and Formatting

**Query 3.10:** Create a report showing full name (first + last), department name, and formatted salary

```sql
select concat(firstname, ' ', lastname) as full_name, dept_name as department, concat('$', to_char(salary, 'FM999,999,999,999,999.00')) as salary_formatted from employees join departments on employees.dept_id = departments.dept_id;
-- Expected output columns: full_name, department, salary_formatted
```

---

## Part 4: Challenge Queries (30 minutes)

### Challenge 4.1

Find employees who earn more than the average salary.
```sql
select concat(firstname, ' ', lastname) as full_name, concat('$', to_char(salary, 'FM999,999,999,999,999.00')) from employees where salary > (select avg(salary) from employees);
```

### Challenge 4.2

List departments that have at least one project.
```sql
select distinct dept_name as department from projects join departments on projects.dept_id = departments.dept_id;
```

### Challenge 4.3

Find the employee with the highest salary in each department.

### Challenge 4.4

Calculate how long each employee has been with the company (in years and months).

---

## Submission Checklist

- [ ] All DDL tasks completed
- [ ] All INSERT, UPDATE, DELETE operations executed
- [ ] All SELECT queries written and tested
- [ ] At least 2 challenge queries attempted
- [ ] Saved your SQL file with all queries

---

## Evaluation Criteria

| Section | Points |
|---------|--------|
| DDL Operations | 20 |
| DML Operations | 25 |
| Basic DQL Queries | 30 |
| Challenge Queries | 25 |
| **Total** | **100** |
