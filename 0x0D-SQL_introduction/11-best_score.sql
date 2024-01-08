-- This script lists all records of the table second_table in the specified database
-- with a score greater than or equal to 10, displaying both the score and the name,


SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
