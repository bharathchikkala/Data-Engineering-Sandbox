#creating database

CREATE DATABASE MILK_SHOP;
CREATE DATABASE dogs;

#delete database

DELETE DATABASE dogs;

#for knowing which database exits

show databases;

#creating tables

CREATE DATABASE pet_shop;
SLEECT pet_shop;

CREATE TABLE dogs(
  name VARCHAR(20),
  breed VARCHAR(20),
  age INT
);
CREATE TABLE pastries(
	name VARCHAR(10),
    quantity INT
);

DESC pastries;

DROP TABLE pastries;


SELECT database();

use pet_shop;

CREATE TABLE cats3(
	name VARCHAR(20) DEFAULT "unnamed",
    age INT DEFAULT 99
    );
    
INSERT INTO cats3 (name) VALUES ("lilly");

SELECT * FROM cats3;

SHOW TABLES;

CREATE TABLE unique_cats(
	cat_id INT NOT NULL PRIMARY KEY,
	name VARCHAR(20),
    age int
);

INSERT INTO unique_cats(cat_id,name,age) VALUES (1,"abc",7);

SELECT * FROM unique_cats;

INSERT INTO unique_cats(cat_id,name,age) VALUES (2,"bcd",3),(3,"hgh",3);

DESC unique_cats;

select database();

-- learning auto_increment with PRIMARY KEY

CREATE TABLE unique_cats2(
	cat_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    age int
);

INSERT INTO unique_cats2 (name,age) VALUES ("lilly",2),("bob",3),("tiger",7);

SELECT * FROM unique_cats2;

DESC unique_cats2;

