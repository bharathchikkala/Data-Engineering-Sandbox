CREATE DATABASE Knowing_CRUD;

SELECT DATABASE();

USE Knowing_CRUD;

CREATE TABLE cats (
    cat_id INT AUTO_INCREMENT,
    name VARCHAR(100),
    breed VARCHAR(100),
    age INT,
    PRIMARY KEY (cat_id)
); 


INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);
       
       
SELECT * FROM cats;
SELECT name FROM cats;

SELECT * FROM cats WHERE age = 4;

SELECT * FROM cats WHERE name ='Egg';


SELECT cat_id FROM cats;

SELECT name, breed FROM cats;

SELECT name, age FROM cats WHERE breed='Tabby';

SELECT cat_id, age FROM cats WHERE cat_id=age;

SELECT * FROM cats WHERE cat_id=age;

-- Knowing Update in CRUD

use office;

SELECT * FROM employees;

UPDATE employees SET Middle_name = "Ganga" WHERE First_name = "Satya";


SELECT database();

use Knowing_crud;

show tables;

SELECT * FROM cats;

-- UPDATE Challenge
-- 1)
UPDATE cats SET name = "Jack" WHERE cat_id = 7;

-- 2)
UPDATE cats SET breed = 'British Shorthair' WHERE cat_id = 1;

-- 3)
UPDATE cats SET age = 12 WHERE cat_id IN (2,3);

-- Understanding DELETE

SELECT * FROM cats;
-- 1)

DELETE FROM cats WHERE cat_id IN (1,4);

-- 2)
DELETE FROM cats WHERE cat_id = 7;

-- 3)
DELETE FROM cats;


