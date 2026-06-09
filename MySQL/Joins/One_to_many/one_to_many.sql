CREATE DATABASE relation_ships;

USE relation_ships;

CREATE TABLE customers(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    e_mail VARCHAR(20)
);

CREATE TABLE orders(
	id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATE,
    price DECIMAL(7,2),
	customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);

SELECT * FROM customers;

SELECT * FROM orders;

INSERT INTO customers (first_name, last_name, e_mail) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');
       
       
INSERT INTO orders (order_date, price, customer_id)
VALUES ('2016-02-10', 99.99, 1),
       ('2017-11-11', 35.50, 1),
       ('2014-12-12', 800.67, 2),
       ('2015-01-03', 12.50, 2),
       ('1999-04-11', 450.25, 5);
       
INSERT INTO orders (order_date,price,customer_id) VALUES ('2026-06-07',1500,3);


SELECT id FROM customers WHERE first_name = 'boy';

SELECT * FROM orders WHERE customer_id = 1;

-- INNER JOIN
SELECT * FROM customers
JOIN orders ON orders.customer_id = customers.id;

-- GROUP BY
SELECT first_name,last_name,SUM(price) FROM customers
JOIN orders on customers.id = orders.customer_id
GROUP BY first_name,last_name;

-- LEFT JOIN
SELECT first_name,last_name,order_date,price FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;

-- LEFT JOIN WITH GROUP BY
SELECT first_name,last_name,IFNULL(SUM(price),0) FROM customers LEFT JOIN orders ON
customers.id = orders.customer_id GROUP BY first_name,last_name;

-- RIGHT JOIN
SELECT * FROM customers RIGHT JOIN orders ON 
customers.id = orders.customer_id; 
