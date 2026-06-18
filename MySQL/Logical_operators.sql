-- LOGICAL OPERATORS
SELECT database();

CREATE DATABASE books_log_oper;
USE books_log_oper;

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

INSERT INTO books
    (title, author_fname, author_lname, released_year, stock_quantity, pages)
    VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
           ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
           ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);

SELECT * FROM books;

-- NOT EQUAL
SELECT title,released_year FROM books WHERE released_year != 2017;

-- NOT LIKE
SELECT title FROM books WHERE title LIKE '% %';
SELECT title FROM books WHERE title NOT LIKE '% %';

-- GREATER THAN
SELECT title FROM books WHERE CHAR_LENGTH(title) > 20;
SELECT title,released_year FROM books WHERE released_year >= 2000 ORDER BY released_year;

-- LOGICAL AND
SELECT title,CONCAT(author_fname,' ',author_lname) AS author,released_year FROM books
	WHERE CONCAT(author_fname,' ',author_lname) = 'Dave eggers' AND released_year > 2010;
    
SELECT * FROM books WHERE CHAR_LENGTH(title) > 20 AND pages > 300 ORDER BY released_year,pages;

-- LOGICAL OR
SELECT * FROM books WHERE released_year > 2010 OR stock_quantity > 120;

-- BETWEEN
SELECT * FROM books WHERE released_year BETWEEN 2010 AND 2017 ORDER BY released_year;

-- IN OPERATOR
SELECT * FROM books WHERE author_lname IN ('lahiri','smith');

SELECT * FROM books WHERE released_year IN (2015,'2016',2004,2010);

SELECT * FROM books WHERE released_year % 2 != 0;

SELECT * FROM books WHERE released_year % 2 != 0 AND pages > 200 OR stock_quantity > 100;

-- CASE STATEMENTS
SELECT title,released_year,
	CASE 
    WHEN released_year >= 2000 THEN 'Modern book'
	ELSE '20th Century one'
    END AS GENRE
    FROM books;
    
SELECT title,stock_quantity,
	CASE 
    WHEN stock_quantity < 50 THEN '*'
	WHEN stock_quantity BETWEEN 50 AND 100 THEN '**'
    ELSE '***'
    END AS stocks
    FROM books;

