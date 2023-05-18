import sqlite3 as sq

connection = sq.connect('test.db')
cur = connection.cursor()

# cur.execute("""CREATE TABLE user (
#     id integer primary key autoincrement,
#     firstname varchar(255),
#     lastname varchar(255),
#     age integer
# );""")
#
# cur.execute("""INSERT INTO user (lastname, firstname, age)
# values ('max', 'ivanov', 25),
# ('aaax', 'iva', 25),
# ('madsx', 'ianov', 27),
# ('marx', 'ivanv', 15),
# ('mrax', 'inov', 9);""")

# connection.execute("""INSERT INTO user (lastname, firstname, age)
# values ('maas', 'ivanossv', 225),
# ('aaasdx', 'ivta', 13),
# ('madssdx', 'ianggov', 270),
# ('marddx', 'ivadnv', 11),
# ('mwrax', 'inotgv', 19);""")

connection.commit()

data = cur.execute("SELECT *FROM user WHERE firstname = 'iva';")
for i in data:
    print(i)

data = cur.execute("SELECT *FROM user WHERE age<25;")
for i in data:
    print(i)

connection.close()