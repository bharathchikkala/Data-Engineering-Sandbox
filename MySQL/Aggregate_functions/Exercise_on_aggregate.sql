-- EXERCISE
-- 1) number of books in database
SELECT SUM(title) AS all_books FROM books;
SELECT COUNT(*) FROM books;

-- 2) books released in each year
SELECT released_year,COUNT(*) FROM books GROUP BY released_year;

-- 3) total stock quantity
SELECT SUM(stock_quantity) AS total_quantity FROM books;

-- 4) avg year for each author
SELECT CONCAT(author_fname,' ',author_lname) AS author,AVG(released_year) FROM books GROUP BY author;
SELECT AVG(released_year) FROM books GROUP BY author_fname,author_lname;

-- 5) name of author who wrote long book
SELECT CONCAT(author_fname,' ',author_lname) AS author_name,pages FROM books WHERE pages = (SELECT MAX(pages) FROM books);
SELECT author_lname FROM books WHERE pages = 634;
SELECT * FROM books;
-- 6)
SELECT released_year,COUNT(*),AVG(pages) AS avg_pages FROM books GROUP BY released_year ORDER BY released_year;

SELECT released_year,COUNT(*) FROM books GROUP BY released_year;

SELECT released_year,COUNT(*),AVG(pages) FROM books GROUP BY released_year ORDER by released_year;
