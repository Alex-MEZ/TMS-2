with open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1.txt', 'r') as file, \
        open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1_1.txt', 'w') as file_5_1, \
        open('/home/alex/PycharmProjects/pythonProject TMS/files/test_files/test_file_1_1.txt', 'w') as file_5_2:
    data = file.readline()
    # data_for_5_1 = data[::2]
    # data_for_5_2 = data[1::2]
    # file_5_1.writelines(data_for_5_1)
    # file_5_2.writelines(data_for_5_2)

    for index, i in enumerate(data):
        if index % 2:
            file_5_1.write(i)
        else:
            file_5_2.write(i)
