# Пользователь вводит три числа.
# Увеличьте первое число в два раза, второе числа уменьшите на 3,
# третье число возведите в квадрат и затем найдите сумму новых трех чисел.

print("Привет, друг! Введи три любых числа.")

number_1 = input("Первое число:")
number_2 = input("Второе число:")
number_3 = input("Третье число:")

number_1 = int(number_1)
number_2 = int(number_2)
number_3 = int(number_3)

new_number_01 = number_1 * 2
new_number_02 = number_2 - 3
new_number_03 = number_3 ** 2

print(new_number_01 + new_number_02 + new_number_03)
