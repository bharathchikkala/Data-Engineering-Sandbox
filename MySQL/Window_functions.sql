CREATE DATABASE window_functions;

USE window_functions;

SELECT database();

CREATE TABLE employees (
    emp_no INT PRIMARY KEY AUTO_INCREMENT,
    department VARCHAR(20),
    salary INT
);
