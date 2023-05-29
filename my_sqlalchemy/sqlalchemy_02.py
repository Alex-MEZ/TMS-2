# Создать файл sqlalchemy_02.py.
# Создать соединение к базе sa_test.db.
# Создать 5 книг с помощью sqlalchemy.

from sqlalchemy import create_engine, text

engine = create_engine('sqlite3:///sa_test.db')
with engine.connect() as connection:
    insert_query = """
                INSERT INTO Book (title, pages, author, price, release_year)
            values ('Kok', 25,'Bul','1430',2300),
            ('Kak', 225,'Bal','12430',230),
            ('Kosk', 2225,'Ful','430',800),
            ('Kdok', 4325,'Badl','143',6300),
            ('Kfok', 2525,'Basl','13430',3300
            );
            """
    connection.commit()
    query = text(insert_query)
    connection.execute(query)
