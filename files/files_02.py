# Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.

with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_2.txt','w') as file:
    for _ in range(6):
        text = input('Enter text: ')
        file.write(text)
        file.write('\n')

print('-----------')
with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_2.txt') as file:
    print(file.read())