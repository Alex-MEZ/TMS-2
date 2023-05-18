CREATE TABLE user (
   id integer primary key autoincrement,
   firstname varchar(255),
   lastname varchar(255),
   age integer
);

INSERT INTO user values ('max', 'ivanov', 25),
('aaax', 'iva', 25),
('madsx', 'ianov', 27),
('marx', 'ivanv', 15),
('mrax', 'inov', 9);

SELECT * FROM user WHERE <=25;
SELECT * FROM user WHERE age>15 and age <=18;



