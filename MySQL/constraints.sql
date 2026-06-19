SELECT database();

use knowing_things;

-- UNIQUE CONSTRAINT
-- data which is inserting into the table should be unique


-- CHECK CONSTRAINT
CREATE TABLE palindromes(
	word VARCHAR(30) CHECK(REVERSE(word) = word)
    );
    
SELECT * FROM palindromes;

INSERT INTO palindromes(word) VALUES ('aaaa');
    
SELECT * FROM palindromes;

DESC palindromes;

ALTER TABLE palindromes
MODIFY word VARCHAR(20);

ALTER TABLE palindromes
CHANGE word word_in VARCHAR(70);
