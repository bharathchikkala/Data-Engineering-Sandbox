-- VIEWS

CREATE VIEW full_reviews AS
SELECT title,rating,CONCAT(first_name,' ',last_name) AS reviewer FROM series JOIN reviews ON series.id = reviews.series_id
JOIN reviewers ON reviewers.id = reviews.reviewer_id ORDER BY title;

SELECT * FROM full_reviews;
SELECT reviewer,MAX(rating),MIN(rating),AVG(rating) FROM full_reviews GROUP BY reviewer;

SELECT title,AVG(rating) FROM full_reviews GROUP BY title HAVING COUNT(rating) > 2;

SELECT * FROM full_reviews;

SELECT title,AVG(rating) FROM full_reviews GROUP BY title HAVING AVG(rating) > 8;

-- ROLLUP
SELECT AVG(rating) FROM full_reviews;
SELECT title,AVG(rating) FROM full_reviews GROUP BY title WITH ROLLUP;
