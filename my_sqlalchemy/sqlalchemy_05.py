from sqlalchemy import create_engine, Table, Metadata, \
    Column, Integer, VARCHAR, Float

e = create_engine('sqlite:///book.db', echo=True)

metadata = Metadata()
book_table = Table('Books', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('title', VARCHAR),
                   Column('pages', Integer),
                   Column('release_year', Integer),
                   Column('author', VARCHAR),
                   Column('price', Float),
                   )
metadata.create_all(e)
