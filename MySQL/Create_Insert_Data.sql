CREATE DATABASE office;

select database();

use office;

CREATE TABLE Employees(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Last_name VARCHAR(20) NOT NULL,
    First_name VARCHAR(20) NOT NULL,
    Middle_name VARCHAR(20),
    Age INT NOT NULL,
    Current_status VARCHAR(10) DEFAULT 'Employeed'
);

INSERT INTO Employees(Last_name,First_name,Middle_name,Age) VALUES ("Chikkala","Bharath",NULL,21),("Chikkala","Sravani","Durga",26),("Tadala",
"Vijaya","Raju",28);

DESC Employees;

SELECT * FROM Employees;

INSERT INTO Employees(Last_name,First_name,Middle_name,Age) VALUES ("Valavala","Satya",NULL,21);
