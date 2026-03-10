/*create database sql_practice;*/
drop table if exists departments cascade;
create table departments(dept_id serial primary key, dept_name varchar(50) not null, location varchar(100), budget decimal(12,2));
drop table if exists employees cascade;
create table employees(emp_id serial primary key, firstname varchar(50) not null, lastname varchar(50) not null, email varchar(100) unique, hiredate date default current_date, salary decimal(10,2), dept_id integer references departments(dept_id));
drop table if exists projects cascade;
create table projects(project_id serial primary key, projectname varchar(100) not null, startdate date, enddate date, budget decimal(12,2), dept_id integer references departments(dept_id));

INSERT INTO departments (dept_name, location, budget) VALUES
('Engineering', 'Building A', 500000),
('Sales', 'Building B', 300000),
('Marketing', 'Building C', 200000),
('HR', 'Building D', 150000);

INSERT INTO employees (firstname, lastname, email, hiredate, salary, dept_id) VALUES
('Alice', 'Johnson', 'alice@company.com', '2020-03-15', 85000, 1),
('Bob', 'Smith', 'bob@company.com', '2019-07-01', 72000, 1),
('Carol', 'Williams', 'carol@company.com', '2021-01-10', 65000, 2),
('David', 'Brown', 'david@company.com', '2018-11-20', 90000, 1),
('Eve', 'Davis', 'eve@company.com', '2022-05-01', 55000, 3),
('Frank', 'Miller', 'frank@company.com', '2020-09-15', 78000, 2),
('Grace', 'Wilson', 'grace@company.com', '2021-06-01', 62000, 4),
('Henry', 'Taylor', 'henry@company.com', '2019-03-01', 95000, 1);

INSERT INTO projects (projectname, startdate, enddate, budget, dept_id) VALUES
('Website Redesign', '2024-01-01', '2024-06-30', 50000, 3),
('Mobile App', '2024-02-15', '2024-12-31', 150000, 1),
('Sales Portal', '2024-03-01', '2024-09-30', 75000, 2),
('HR System', '2024-04-01', '2024-08-31', 40000, 4);

SELECT * FROM departments;
SELECT * FROM employees;
SELECT * FROM projects;

alter table employees add column phone varchar(20);
alter table departments alter column budget type decimal(15,2);
drop table if exists training_courses CASCADE;
create table training_courses(course_id serial primary key, coursename varchar(100) not null, durationhours integer, instructor varchar(100));
insert into employees(firstname, lastname, email, salary, dept_id) VALUES
('Grace', 'Lee', 'grace.lee@company.com', 58000, 4),
('Ivan', 'Chen', 'ivan@company.com', 61000, 4),
('Julia', 'Kim', 'julia@company.com', 55000, 4);

update employees set salary = salary * 1.1 where employees.dept_id = (select departments.dept_id from departments where dept_name = 'Engineering');
update employees set email = 'bob.smith@company.com' where firstname = 'Bob' and lastname = 'Smith'; 
delete * from projects where enddate < current_date;
/*delete * from employees where dept_id = null*/
select * from employees order by salary desc;
select * from employees where employees.dept_id = (select departments.dept_id from departments where dept_name = 'Engineering');
select * from employees where hiredate.year >= 2021;
select * from employees where salary >= 60000 and salary <= 80000;
/* or the one above could be:*/
/*select * from employees where salary between 60000 and 80000;*/
select * from employees where email like '%company%';
select * from departments where location in ('Building A', 'Building B');
select dept_name, sum(salary) as salary_expense from employees join departments on employees.dept_id = departments.dept_id group by dept_name;
select round(avg(salary),2) as average_salary, min(salary) as minimum_salary, max(salary) as maximum_salary from employees;
select * from employees where dept_id in (select dept_id as numEmployees from employees GROUP BY dept_id HAVING count(dept_id) >= 2);
select concat(firstname, ' ', lastname) as full_name, dept_name as department, concat('$', to_char(salary, 'FM999,999,999,999,999.00')) as salary_formatted from employees join departments on employees.dept_id = departments.dept_id;
select concat(firstname, ' ', lastname) as full_name, concat('$', to_char(salary, 'FM999,999,999,999,999.00')) from employees where salary > (select avg(salary) from employees);
select distinct dept_name as department from projects join departments on projects.dept_id = departments.dept_id;
