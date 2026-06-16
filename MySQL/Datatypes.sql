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


-- TIME FUNCTIONS
SELECT 
    birthdt,
    YEAR(birthdate),
    MONTH(birthdt),
    MONTHNAME(birthdate),
    DAY(birthdate),
    HOUR(birthdt),
    SECOND(birthtime),
    MICROSECOND(birthdt)
FROM
    people;
    
-- Formatting Dates

SELECT birthdate, DATE_FORMAT(birthdate, '%a %b %D') FROM people;
 
SELECT birthdt, DATE_FORMAT(birthdt, '%H:%i') FROM people;
 
SELECT birthdt, DATE_FORMAT(birthdt, 'BORN ON: %r') FROM people;

-- DATE MATH
SELECT birthdate FROM people;

SELECT DATEDIFF(birthdate,CURDATE()) FROM people;

SELECT birthdate FROM people WHERE name = 'bharath';

SELECT 'Ganga Garu was older by:' AS what,DATEDIFF(
	(SELECT birthdate FROM people WHERE name = 'bharath'),
    (SELECT birthdate FROM people WHERE name = 'ganga')) AS diff_between_us;
    
SELECT TIMEDIFF(CURTIME(),'07:00:00');

SELECT name,birthdate,birthdate + INTERVAL 21 YEAR FROM people;

SELECT name,birthdate,
	DATEDIFF(CURDATE(), birthdate + INTERVAL 21 year) AS over_days
    FROM people;
