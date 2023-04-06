# Написать функции по работе с csv файлами в файле csv_utils.py.
# Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление записи(по позиции, по-умолчанию последнюю).
# В файле files_08 импортировать функции.
# С помощью функций создать файл с информацией о товарах(Имя товара, цена, количество, комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.


import csv


def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def add_csv_record(filename, record, position=-1):
    with open(filename, 'r+', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        if position == -1:
            data.append(record)
        else:
            data.insert(position, record)
        file.seek(0)
        writer = csv.writer(file)
        writer.writerows(data)


def delete_csv_record(filename, position=-1):
    with open(filename, 'r+', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
        if position == -1:
            data.pop()
        else:
            data.pop(position)
        file.seek(0)
        writer = csv.writer(file)
        writer.writerows(data)


from csv_utils import read_csv, write_csv, add_csv_record, delete_csv_record

data = [
    ['Ноутбук', '50000', '3', ''],
    ['Монитор', '15000', '5', 'IPS-матрица'],
    ['Клавиатура', '3000', '10', 'мембранные клавиши']
]
write_csv('products.csv', data)

data = read_csv('products.csv')
print('До добавления и удаления:')
for row in data:
    print(row)

add_csv_record('products.csv', ['Мышь', '1000', '20', 'оптическая'])

delete_csv_record('products.csv', 2)

data = read_csv('products.csv')
print('После добавления и удаления:')
for row in data:
    print(row)

from csv_utils import read_csv, write_csv, add_csv_record, delete_csv_record

data = [
    ['Ноутбук', '50000', '3', ''],
    ['Монитор', '15000', '5', 'IPS-матрица'],
    ['Клавиатура', '3000', '10', 'мембранные клавиши']
]
write_csv('products.csv', data)

data = read_csv('products.csv')
print('До добавления и удаления:')
for row in data:
    print(row)

add_csv_record('products.csv', ['Мышь', '1000', '20', 'оптическая'])

delete_csv_record('products.csv', 2)

data = read_csv('products.csv')
print('После добавления и удаления:')
for row in data:
    print(row)
