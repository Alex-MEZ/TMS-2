# Имеется текстовый файл. Переписать в другой файл все его строки с заменой в них символа 0 на символ 1 и наоборот.

with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_3.txt', 'r') as file, \
        open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_3_new.txt', 'w') as file_new:
    fileread = file.read()
    for i in fileread:
        if i == '0':
            i = '1'
        elif i == '1':
            i = '0'
        file_new.write(i)
