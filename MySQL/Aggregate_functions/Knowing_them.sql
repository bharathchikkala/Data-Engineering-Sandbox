-- AGGREGATE FUNCTIONS
CREATE DATABASE books_shop2;

select database();

use books_shop2;

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

-- COUNT
SELECT COUNT(*) AS count FROM books;
SELECT COUNT(DISTINCT(CONCAT(author_fname,' ',author_lname))) AS who_there FROM books;
SELECT COUNT(DISTINCT(released_year)) AS year FROM books;

-- how many titles contain 'the'
SELECT COUNT(title) FROM books WHERE title LIKE '%the%';

-- GROUP BY
SELECT author_lname,COUNT(*) FROM books GROUP BY author_lname ORDER BY COUNT(*) DESC;

SELECT released_year,COUNT(title) FROM books GROUP BY released_year;
SELECT author_lname,COUNT(*) FROM books GROUP BY author_lname;


--  MIN & MAX
SELECT MIN(released_year) AS oldest_book FROM books;
SELECT MAX(pages) AS most_pages FROM books;

-- SELECT MAX(pages),title FROM books; wrong
SELECT title,pages FROM books ORDER BY pages DESC LIMIT 1;
SELECT * FROM books WHERE released_year = 2001;

-- Subqueries
SELECT title,pages FROM books WHERE pages = (SELECT MAX(pages) FROM books);
SELECT title,released_year FROM books ORDER BY released_year LIMIT 2;
select title,min(released_year) from books;
SELECT title,released_year FROM books WHERE released_year = (SELECT MIN(released_year) FROM books);

-- GROUP BY with multiple coloumns
SELECT author_lname FROM books GROUP BY author_lname,author_fname;
SELECT author_lname,COUNT(*) FROM books GROUP BY author_lname,author_fname;
SELECT CONCAT(author_fname,' ',author_lname) AS author,COUNT(*) AS written FROM books GROUP BY author;


-- MIN/MAX with GROUP BY
SELECT DISTINCT(CONCAT(author_fname,' ',author_lname)) AS author,MIN(released_year) FROM books GROUP BY author;

SELECT
    CONCAT(author_fname, ' ', author_lname) AS author,
    COUNT(*) AS books_written,
    MIN(released_year),
    MAX(released_year),
    MAX(pages),MIN(pages)
FROM
    books
GROUP BY author;

SELECT MAX(pages) FROM books GROUP BY author_fname;

-- SUM
SELECT SUM(pages) FROM books;

SELECT CONCAT(author_fname,' ',author_lname) AS author,SUM(pages) FROM books GROUP BY author_fname,author_lname ORDER BY SUM(pages) DESC;

-- AVG
SELECT AVG(released_year) FROM books;

SELECT released_year,AVG(stock_quantity) FROM books GROUP BY released_year ORDER BY released_year;
SELECT 
    released_year, 
    AVG(stock_quantity), 
    COUNT(*) FROM books
GROUP BY released_year;
SELECT released_year,stock_quantity FROM books;
