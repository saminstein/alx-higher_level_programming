-- script that lists all record of the table 'second_table' in the database 'hbtn_0c_0' in your MySQL server
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)

SELECT score, name FROM second_table ORDER BY score DESC;