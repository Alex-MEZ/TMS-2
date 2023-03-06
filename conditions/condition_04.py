# Ввести строку с клавиатуры
# Если длина строки больше 5 - вывести значение на экран
# Если длина строки меньше 5 - вывести строку “Need more!”
# Если длина строки равна 5 - вывести строку “len str == 5”

my_str = input("Введи предложение: ")
len_my_str = len(my_str)

if len_my_str > 5:
    print(len_my_str)
elif len_my_str < 5:
    print("Need more!")
else:
    print("len str == 5")