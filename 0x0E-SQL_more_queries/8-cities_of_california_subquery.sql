-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Find the state_id for California
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- List all cities of California
SELECT * FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;
