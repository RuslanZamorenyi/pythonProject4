CREATE TABLE table_list (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    date_of_purchase INTEGER IS NOT NULL,
    cost iNTEGER IS NOT NULL,
    appointment TEXT IS ON NULL );

ALTER TABLE table_list
ADD COLUMN salary INTEGER

INSERT INTO table_list (date_of_purchase, cost, appointment, salary)
VALUE (20, 1200, "Draw", 100000000)

SELECT *
FROM table_list;





