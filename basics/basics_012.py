# Запросить у пользователя два целых числа.
# Вывести строку вида “2 плюс 3 равно 5”
# Примечание: после ввода переменных преобразовать переменные к типу int
# >> first_number = int(first_number)

number_1 = input("Первое число:")
number_2 = input("Второе число:")
number_1 = int(number_1)
number_2 = int(number_2)
number_3 = number_1 + number_2
print(number_1, "+", number_2, "=", number_3)
