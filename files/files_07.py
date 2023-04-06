# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл

import json

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/json_1.json', 'w') as file:
    data = json.dumps(matrix)
    print(type(data), data)
    file.write(data)

with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/json_1.json', 'r') as file, \
        open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/json_2.json', 'w') as file_2:
    data = json.load(file)
    for index_row, row in enumerate(data):
        for index_number, number in enumerate(row):
            if number % 2 == 0:
                data[index_row][index_number] = 0
    print(type(data), data)
    json.dump(data, file_2)
