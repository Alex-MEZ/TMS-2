# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки.
# Если нет, то получить номер первой строки, в которой эти файлы отличаются друг от друга.

# Variant 1
# with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1.txt', 'r') as file, \
#         open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1_0.txt', 'r') as file_1:
# count = 0
# while line_1 := file.readline():
#     line_2 = file_1.readline()
#     if line_1 != line_2:
#         print(f'difference in {count} line')
#         break
#     count += 1

# Variant2
with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1.txt', 'r') as file, \
        open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1_0.txt', 'r') as file_1:
    for index, (line_1, line_2) in enumerate(zip(file, file_1)):
        if line_1 != line_2:
            print(f"differences in {index + 1} line")
            break
# arr = [1, 2, 3, 4, 5]
# arr_2 = [11, 21, 12, 13]
# arr_3 = [11, 21]
# for element_1, element_2,element_3 in zip(arr, arr_2,arr_3):
#     print(element_1, element_2,element_3)
