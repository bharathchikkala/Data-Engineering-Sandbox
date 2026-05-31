-- EXERCISE
-- 1) title which has stories
SELECT title FROM books WHERE title LIKE '%stories%';

-- 2) get longest book
SELECT title,pages FROM books ORDER BY pages DESC LIMIT 1;

-- 3) get 3 recent books under summary with title and year
SELECT CONCAT(title,' - ',released_year) AS summary FROM books ORDER BY released_year DESC LIMIT 3;

-- 4) get author_lname whic has space between
SELECT title,author_lname FROM books WHERE author_lname LIKE '% %';

-- 5) 3 books with lowest stock
SELECT title,released_year,stock_quantity FROM books ORDER BY stock_quantity LIMIT 3;

-- 6) title,author_lname first sort author and then title
SELECT title,author_lname FROM books ORDER BY author_lname,title;

-- 7)
SELECT 
    CONCAT('MY FAVOURITE AUTHOR IS ',
            UPPER(author_fname),
            ' ',
            UPPER(author_lname),
            '!') AS yelll
FROM
    books
ORDER BY author_lname;

SELECT title FROM books WHERE title LIKE '%stories%';
