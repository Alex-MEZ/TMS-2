# Написать игру. Пользователь должен угадать число.
# Сперва вводится диапазон угадывания.
# После колличество попыток. В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или меньше искомое число).
# Если за указанное количество попыток число не угадано - выводить: You are the loser и правильное число.

print("Игра Угадай число!")

first_number = int(input("Введи начальное число: "))
end_number = int(input("Введи конечное число: "))
import random

number = random.randint(first_number, end_number)
#print(number)
print("У тебя есть 3 попытки угадать число!")
max_popytki = 3
popytki = 0
while popytki < max_popytki:
    user = int(input("Угадай число: "))
    popytki += 1
    if user == number:
        print(" You are the winner")
        break
    elif user < number:
        print("Введенное число меньше загаданного. Попробуй еще!")
    elif user > number:
        print("Введенное число больше загаданного. Попробуй еще!")
if user != number:
    print("You are the loser")
