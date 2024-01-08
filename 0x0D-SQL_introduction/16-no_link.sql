-- This script lists all records of the table second_table in the specified database
-- excluding rows without a name value. Results display the score and the name in that order,
-- and records are listed by descending score

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
