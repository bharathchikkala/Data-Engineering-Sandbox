-- EXERCISE
-- 1) current time
SELECT CURTIME();

-- 2) current date
SELECT CURDATE();

-- 3) current day of week
SELECT DAYNAME(CURDATE());
SELECT DAYOFWEEK(CURDATE());
SELECT DAYOFYEAR(CURDATE());

-- 4) day and time USE DATEFORMAT()
SELECT DATE_FORMAT(NOW(), '%d-%m-%Y %H:%i:%s') AS current_datetime;

SELECT DATE_FORMAT(NOW(), '%M %D at %l:%i') AS current_datetime;

-- Create tweet table
CREATE TABLE tweets(
	Tweet_content VARCHAR(200),
    Username VARCHAR(20),
    Created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- NOW() also we can use in current_timestamp
);

INSERT INTO tweets (tweet_content,username) VALUES ('recently surya kumar yadav was out of form so BCCI selector thought sack him and appoint
			iyer as captain of T20 matches','Cricket_with_bharath');
            
SELECT * FROM tweets;

INSERT INTO tweets(tweet_content,username) VALUES ('SRHvsRCB tickets available DM for information','bharath_chikkala');
