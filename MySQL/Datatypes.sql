SELECT database();

CREATE DATABASE knowing_things;

USE knowing_things;

-- WORKING WITH DATES AND TIME
CREATE TABLE people(
	name VARCHAR(20),
    birthdate DATE,
    birthtime TIME,
    birthdt DATETIME
);

DESC people;

INSERT INTO people (name,birthdate,birthtime,birthdt) VALUES 
	('bharath','2004-12-02','07:20:20','2004-12-02 07:20:20'),
    ('akka','2000-12-01','10:30:20','2000-12-01 10:30:20'),
    ('raja','1996-11-06','08:45:20','1996-11-06 08:45:20'),
    ('ganga','2004-10-23','12:30:20','2004-10-23 12:30:20')
    ;


TRUNCATE people;

SELECT * FROM people;
SELECT CURTIME();
SELECT CURDATE();
SELECT NOW();

-- CREATE TABLE right_now(
-- 	now_time TIME CURTIME(),
--     now_date DATE CURDATE()
-- );

INSERT INTO people (name,birthdate,birthtime,birthdt) VALUES ('vyshu',CURDATE(),CURTIME(),NOW());

SELECT DAYNAME('2004-12-02');
SELECT DAYNAME('2004-10-23');

SELECT name,birthdate,DAYNAME(birthdate),DAYOFYEAR(birthdate),WEEK(birthdate) AS day FROM people;
