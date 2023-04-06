#1
with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_2.txt', 'w') as file:
    for _ in range(3):
        s = input("Vvedi stroku")
        file.write(f'{s}\n')
#2
with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_2.txt', 'w') as file:
    s = []
    for _ in range(3):
        text = input("Vvedi stroku")
        s.append(f'{text}\n')
    file.writelines(f'{s}\n')
