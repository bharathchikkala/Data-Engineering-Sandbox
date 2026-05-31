SELECT database();

-- CREATE DATABASE book_shop;

USE book_shop;

CREATE TABLE books 
	(
		book_id INT AUTO_INCREMENT,
		title VARCHAR(100),
		author_fname VARCHAR(100),
		author_lname VARCHAR(100),
		released_year INT,
		stock_quantity INT,
		pages INT,
		PRIMARY KEY(book_id)
	);
 
INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);

SELECT * FROM books;
DESC books;

-- CONCAT
SELECT CONCAT(author_fname,' ',author_lname) AS name from books;

-- CONCAT_WS
SELECT CONCAT_WS('!','bharath','akka','raja') AS cousins;

-- SUBSTRING
SELECT SUBSTRING('hello flokes',1,10) AS substring;
SELECT SUBSTRING('hello flokes',-6,4);
SELECT SUBSTRING(title,1,15) AS title FROM books;

-- SELECT SUBSTRING(title,1,10) AS short_title, CONCAT('...') FROM books;
SELECT CONCAT(SUBSTRING(title,1,10),'...') AS short_title FROM books;

SELECT CONCAT(SUBSTRING(author_fname,1,1),'.',SUBSTRING(author_lname,1,1),'.') AS author_initials FROM books;


-- REPLACE
SELECT REPLACE('hello world','hel','@*$&') AS changed;

SELECT REPLACE(title,' ','-') AS dash_title FROM books;

-- REVERSE
SELECT REVERSE('ganga');
SELECT REVERSE(author_fname) FROM books; 

-- CHAR LENGTH
SELECT CHAR_LENGTH('bharath') AS length;
SELECT CHAR_LENGTH(title) FROM books;
SELECT LENGTH(title) FROM books; #return value in bytes
SELECT CONCAT(author_lname, ' is ', CHAR_LENGTH(author_lname), ' characters long') AS name_length FROM books;

-- UPPER and LOWER
SELECT CONCAT('title upper case like ',UPPER(title)) AS upper_case FROM books;

-- INSERT
SELECT UPPER(INSERT('hi bharath',3,0,' ganga')) AS inserting;

-- LEFT
SELECT UPPER(LEFT('bharath chikkala',7)) AS name;

-- RIGHT
SELECT UPPER(RIGHT('bharath chikkala',9)) AS surname;

-- REPEAT
SELECT REPEAT('bharath ',2) AS name;

-- TRIM
SELECT TRIM('   bharath   ');
SELECT TRIM(LEADING 'a' FROM 'aaabharathaaaaaaaaaaaaaaa');
SELECT TRIM(TRAILING 'a' FROM 'aaabharathaaaaaaaaaaaaaaa');
SELECT TRIM(BOTH 'u' FROM 'uuuuuuuuuuuuuuuuuuubharathuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu') AS calling;


