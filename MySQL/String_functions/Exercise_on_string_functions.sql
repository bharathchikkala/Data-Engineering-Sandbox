-- EXERCISE OF STRING FUNCTIONS
-- 1)
SELECT UPPER(REVERSE('where is my dog')) AS rev_up;

-- 2)REPLACE all spaces with arrow in title from books
SELECT REPLACE(title,' ','->') AS arrow_title FROM books;

-- 3) about last name
SELECT author_lname AS Forwards,REVERSE(author_lname) AS Backwards FROM books;

-- 4) author full name Upper
SELECT UPPER(CONCAT(author_fname,' ',author_lname)) AS full_name_in_caps FROM books;

-- 5) combine with released year
SELECT CONCAT(title,' was released in ',released_year) AS blurb FROM books;

-- 6) print book title and length of each title
SELECT title,CHAR_LENGTH(title) AS character_count FROM books;

-- 7) final one
SELECT 
    CONCAT(LEFT(title, 10), '...') AS short_title,
    CONCAT(author_fname, ',', author_lname) AS author,
    CONCAT(stock_quantity, ' in stock') AS quantity
FROM
    books;
