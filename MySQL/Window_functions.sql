CREATE DATABASE window_functions;

USE window_functions;

SELECT database();

CREATE TABLE employees (
    emp_no INT PRIMARY KEY AUTO_INCREMENT,
    department VARCHAR(20),
    salary INT
);

INSERT INTO employees (department, salary) VALUES
('engineering', 80000),
('engineering', 69000),
('engineering', 70000),
('engineering', 103000),
('engineering', 67000),
('engineering', 89000),
('engineering', 91000),
('sales', 59000),
('sales', 70000),
('sales', 159000),
('sales', 72000),
('sales', 60000),
('sales', 61000),
('sales', 61000),
('customer service', 38000),
('customer service', 45000),
('customer service', 61000),
('customer service', 40000),
('customer service', 31000),
('customer service', 56000),
('customer service', 55000);

SELECT * FROM employees;

-- OVER()
SELECT department,AVG(salary) FROM employees GROUP BY department;
SELECT AVG(salary) FROM employees;

SELECT AVG(salary) OVER() FROM employees;
SELECT department,salary,AVG(salary) OVER() FROM employees;

-- PARTITION BY
SELECT department,salary,AVG(salary) OVER(PARTITION BY department) FROM employees;

-- EACH DEPT PAY
SELECT department,salary,
	SUM(salary) OVER(PARTITION BY department) AS total_spent_by_dept,
    SUM(salary) OVER() AS total_pay
    FROM employees;
    
-- ORDER BY
SELECT department,AVG(salary) FROM employees GROUP BY department ORDER BY AVG(salary);

SELECT department,salary,
	AVG(salary) OVER(PARTITION BY department ORDER BY salary) AS avg_salary,
    SUM(salary) OVER(PARTITION BY department ORDER BY salary) AS sum
    -- AVG(salary) OVER(ORDER BY AVG(salary))
    FROM employees;
    
SELECT department,SUM(salary) FROM employees GROUP BY department;

-- RANK
SELECT department,salary,
	RANK() OVER(ORDER BY salary DESC)
    FROM employees;
    
SELECT department,salary,
	RANK() OVER(PARTITION BY department ORDER BY salary DESC) FROM employees;
    
SELECT department,salary,
	ROW_NUMBER() OVER(ORDER BY salary DESC),
	DENSE_RANK() OVER(ORDER BY salary DESC),
	RANK() OVER(ORDER BY salary DESC) FROM employees;
    
-- ROW_NUMBER and DENSE_RANK
SELECT department,salary,
	ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS row_num,
    DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS dense_num,
    RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS rank_num FROM employees;
    
SELECT department,salary,
	DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) FROM employees;
    
-- NTILE
SELECT department,salary,
	NTILE(5) OVER(ORDER BY salary DESC)
    FROM employees;


-- FIRST_VALUE
SELECT emp_no,department,salary,
	FIRST_VALUE(emp_no) OVER(ORDER BY salary DESC) AS high_paid
    FROM employees ORDER BY salary;
    
SELECT emp_no,department,salary,
	FIRST_VALUE(emp_no) OVER(PARTITION BY department ORDER BY salary DESC) AS high_paid_dept FROM employees ORDER BY emp_no;
    
-- LEAD and LAG
SELECT department,salary,
	LAG(salary) OVER(PARTITION BY department)
    FROM employees;
    
SELECT department,salary,
	LEAD(salary) OVER(PARTITION BY department)
    FROM employees;
