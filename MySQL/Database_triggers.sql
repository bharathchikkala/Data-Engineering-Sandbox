CREATE DATABASE trigger_s;

USE trigger_s;

CREATE TABLE users(
username VARCHAR(100),
age INT
);

INSERT INTO users(username,age) VALUES ('bharath',21);

SELECT * FROM users;

DELIMITER $$

CREATE TRIGGER must_be_adult
     BEFORE INSERT ON users FOR EACH ROW
     BEGIN
          IF NEW.age < 18
          THEN
              SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Must be an adult!';
          END IF;
     END;
$$
DELIMITER ;

INSERT INTO users(username,age) VALUES ('raja',25),('sravani',25);

SELECT * FROM users;
