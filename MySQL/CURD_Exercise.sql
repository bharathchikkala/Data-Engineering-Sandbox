-- Create database shirts_db

CREATE DATABASE shirts_db;

-- Knowing which db we are currently working on!
SELECT DATABASE();
USE shirts_db;

-- Creating the table
CREATE TABLE Shirts(
	Shirt_id INT PRIMARY KEY AUTO_INCREMENT,
    Article VARCHAR(20),
    Color VARCHAR(10),
    Shirt_Size VARCHAR(5),
    Last_Worn int
);

DESC Shirts;

SHOW TABLES;
SHOW DATABASES;

-- CREATING PART OF CRUD
-- Inserting DATA into the Shirts table,
INSERT INTO Shirts(Article,color,shirt_size,last_worn) 
	VALUES
	('t-shirt', 'white', 'S', 10),
	('t-shirt', 'green', 'S', 200),
	('polo shirt', 'black', 'M', 10),
	('tank top', 'blue', 'S', 50),
	('t-shirt', 'pink', 'S', 0),
	('polo shirt', 'red', 'M', 5),
	('tank top', 'white', 'S', 200),
	('tank top', 'blue', 'M', 15);
    
SELECT * FROM shirts;

-- Inserting another shirt
INSERT INTO shirts(article, color, shirt_size, last_worn) VALUES ('polo shirt','purple','M',50);


-- READING PART OF CRUD
SELECT article,color FROM shirts;

SELECT article,color,shirt_size,last_worn FROM shirts WHERE shirt_size = 'M';

-- UPDATING PART OF CRUD
-- 1) update all polo shirts change size to L
SELECT * FROM shirts WHERE article = 'polo shirt';

UPDATE shirts SET shirt_size = 'L' WHERE shirt_id IN (3,6,9); 
-- Here we r using SAFE UPDATE MODE so used primary key for updating else it would be WHERE article = 'polo shirt';

-- 2) update shirt last worn 15 days ago to 0
SELECT * FROM shirts WHERE last_worn = 15;

UPDATE shirts SET last_worn = 0 WHERE shirt_id = 8;

SELECT * FROM shirts;

-- 3) update all white shirts size to XS and color to off white
SELECT * FROM shirts WHERE color = 'white';

UPDATE shirts SET shirt_size = 'XS',color = 'off white' WHERE shirt_id IN (1,7);

SELECT * FROM shirts WHERE color = 'off white';

SELECT * FROM shirts;

-- DELETING PART OF CRUD

-- 1) delete all old shirts last worn 200 days ago
DELETE FROM shirts WHERE shirt_id IN (2,7);
SELECT * FROM shirts;

-- 2) delete all tank tops
DELETE FROM shirts WHERE shirt_id IN (4,8);
SELECT * FROM shirts;

-- 3) delete all shirts but keep table
DELETE FROM shirts WHERE shirt_id IN (1,3,5,6,9);
SELECT * FROM shirts;
