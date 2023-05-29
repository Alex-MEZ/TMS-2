# Создать пакет school. Создать файл models.py.
# Создать базу school в postgre. Создать таблицу
# Учебной группы(Group) с помощью sqlalchemy в
# декларативном стиле. Группа характеризуется названием(name).

# Создать таблицу Студент(Student) с помощью sqlalchemy в файле models.py.
# Студент характеризуется именем(firstname) и фамилией(lastname)
# и группой к которой он приурочен.
#
# Создать файл sqlalchemy_11.py. Создать две группы. Добавить в каждую
# по три студента.


from sqlalchemy import create_engine, \
    ForeignKey, Float, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base, \
    relationship, sessionmaker, backref
from sqlalchemy_utils import create_database, database_exists

DB_USER = 'postgres'
DB_PWD = 'postgres'
DB_HOST = 'localhost'
DB_NAME = 'school'

e = create_engine(f'postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}', echo=True)
e = create_engine(f'postgresql://postgres:postgres@localhost/school', echo=True)

if not database_exists((e.url)):
    create_database(e.url)

Base = declarative_base()


for student in students_all:
    print(students.firstname,student)

for group in 'groups':
    students_of_one_group = group.students
    print(students_of_one_group)
    print([st.books for st in students_of_one_group])

for book in 'books':
    students_for_book = book.students
    print([st.firstname for st in students_for_book])
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(Integer,
                      ForeignKey('group.id'),
                      nullable=False)
    group = relationship('Group',
                         foreign_keys='Student.group_id',
                         backref='students')

    def __init__(self, firstname, lastname, group):
        self.firstname = firstname
        self.lastname = lastname
        self.group = group


#
class Diary(Base):
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    avg_score = Column(Float)
    student_id = Column(Integer,
                        ForeignKey('student.id'),
                        nullable=False)
    student = relationship('Student',
                           foreign_keys='Diary.student_id',
                           backref=backref('students', uselist=False)
                           )

    def __init__(self, avg_score, student):
        self.avg_score = avg_score
        self.student = student


class Assotiation(Base):
    __tablename__ = 'assotiation', Base.metadata
    id = Column('id', Integer, primary_key=True),
    student_id = Column(Integer, ForeignKey('student_id')),
    book_id = Column(Integer, ForeignKey('book_id'))


assotiation_table = Table(
    'assotiation', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('student_id', Integer, ForeignKey('student.id')),
    Column('book_id', Integer, ForeignKey('book.id'))
)


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pages = Column(Integer)
    students = relationship('Student',
                            secondary=assotiation_table,
                            backref='books')

    def __init__(self, name, pages):
        self.name = name
        self.pages = pages


Base.metadata.create_all(e)
session = sessionmaker(bind=e)()
