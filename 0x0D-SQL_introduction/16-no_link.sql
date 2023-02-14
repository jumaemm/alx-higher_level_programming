-- List all records with non-null name
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC
