# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.

# my_file = open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1.txt')
# read_all = my_file.read()
# # print(read_all,type(read_all))
# print(read_all)
# my_file.close()
# my_file_2 = open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1.txt')
# while line := my_file_2.readline():
#     print(line.strip())
# my_file_2.close()

file = open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1.txt')
# file_read = file.read()
# file_read_list = file_read.split()
# print(file_read_list[0])
# print(file_read_list[4])
# print(file_read_list[:5])
# print(file_read_list[:2])
# print(file_read_list)
# file.close()
count = 0
while line := file.readline():
    if count > 5:
        break
    print(line.strip())