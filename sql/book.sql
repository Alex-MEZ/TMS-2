
CREATE TABLE IF NOT EXISTS book (id integer, title varchar,pages int, author varchar, price float);

ALTER TABLE book ALTER COLUMN release_year int;


CREATE TABLE IF NOT EXISTS book (id integer primary key autoincrement, title varchar,pages int, author varchar, price float);
ALTER TABLE book ADD COLUMN release_year int;
INSERT INTO book (title, pages , author , price , release_year )
VALUES ('master', 380, ' Bulgakov', 25, 1953),
('kot', 3880, ' Bugakov', 225, 153),
('psa', 30, ' Bulgakv', 255, 19153),
('mar', 80, ' Bulga', 250, 19553),
('maer', 800, ' Buakov', 215, 19253);


SELECT * FROM book
SELECT title, price, release_year FROM book WHERE release_year = 2001 AND author = 'kaverin'
UPDATE book SET price = 1000 WHERE  release_year = 153
DELETE FROM book WHERE release_year = 153