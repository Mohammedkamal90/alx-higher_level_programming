-- list all cities of California that can be found in database hbtn_0d_usa
-- list all rows of column in database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
