-- EXERCISE

CREATE TABLE students(
	id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20)
);

CREATE TABLE papers(
	title VARCHAR(30),
    grade INT,
    student_id INT,
    FOREIGN KEY(student_id) REFERENCES students(id)
);

INSERT INTO students (first_name) VALUES 
('Caleb'), ('Samantha'), ('Raj'), ('Carlos'), ('Lisa');
 
INSERT INTO papers (student_id, title, grade ) VALUES
(1, 'My First Book Report', 60),
(1, 'My Second Book Report', 75),
(2, 'Russian Lit Through The Ages', 94),
(2, 'De Montaigne and The Art', 98),
(4, 'Borges and Magical Realism', 89);

SELECT * FROM students;
SELECT * FROM papers;

-- 1) INNER JOIN
SELECT first_name,title,grade FROM students JOIN papers ON students.id = papers.student_id ORDER BY grade DESC;

-- 2) LEFT JOIN
SELECT first_name,title,grade FROM students LEFT JOIN papers ON students.id = papers.student_id;

SELECT first_name,IFNULL(title,'Missing'),IFNULL(grade,0) FROM students LEFT JOIN papers ON students.id = papers.student_id;

SELECT first_name,IFNULL(AVG(grade),0) FROM students LEFT JOIN papers ON students.id = papers.student_id 
	GROUP BY first_name ORDER BY AVG(grade) DESC;
    
-- PASS or FAIL
SELECT First_name,IFNULL(AVG(grade),0) AS 'Avg(grade)',
	CASE
    WHEN AVG(grade) > 75 THEN 'PASSED'
    ELSE 'FAILED'
    END AS Passing_status
    FROM students LEFT JOIN papers ON students.id = papers.student_id
	GROUP BY first_name ORDER BY AVG(grade) DESC;

