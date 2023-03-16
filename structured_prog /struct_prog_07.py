# Ввести строку.
# Вывести на экран букву, которая находится в середине этой строки.
# Также, если эта центральная буква равна первой букве в строке,
# то создать и вывести часть строки между первым и последним символами исходной строки.
# (подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам.
# Для создания результирующий строки используйте срез)

stroka = input("Vvedi stroka - ")
stroka_1 = len(stroka)
stroka_2 = stroka_1 // 2
if stroka_1 % 2 != 0:
    print(stroka[int(stroka_2)])
elif stroka_1 % 2 == 0:
    print(stroka[int(stroka_2) - 1:int(stroka_2)])
if stroka[int(stroka_2)] == stroka[0]:
    print(stroka[1:-1])
else:
    pass

    # for x in (len(stroka) / 2):
    #     print(x)
