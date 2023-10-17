-- Lists all records of table second_table having a name value in my MySQL
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
