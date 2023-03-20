# В заданной строке расположить в обратном порядке все слова.
# Разделителями слов считаются пробелы.

stroka = input("Введи фразу из нескольких слов: ")
slova = stroka.split()
obratka_stroka = slova[::-1]
result = " ".join(obratka_stroka)
print(result)

# # Похожее задание
#
# slova = stroka.split(";")
# obratka_stroka = ""
#
# for i in slova:
#     obratka_stroka = slova[::-1]
# print(obratka_stroka)
