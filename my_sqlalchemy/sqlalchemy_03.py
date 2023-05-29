# Создать файл sqlalchemy_03.py.
# Написать программу: пользователь вводит год.
# Отобразить на экране те книги, год которых меньше введенного пользователем года.
# Если таких книг нет - вывести сообщение: Not found.

from sqlalchemy import create_engine, text


def find_books_by_year():
    engine = create_engine('sqlite3:///sa_test.db')
    with engine.connect() as connection:
        year = int(input('enter year - '))
        select_query_text = f""" SELECT *FROM Book WHERE release_year < {year}"""
        query = text(select_query_text)
        data = list(connection.execute(query))
        if len(data):
            for book in data:
                print(book)
            else:
                print("not found")


def main():
    find_books_by_year()

if __name__=__main__