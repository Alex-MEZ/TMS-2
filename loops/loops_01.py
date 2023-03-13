# Выведите на экран n раз фразу "I am a programmer".
# Число n вводит пользователь.

# n_raz = int(input("Сколько раз хочешь вывести фразу на экран? - "))
#
# my_list = (f'I am a programmer')
# for i in range(n_raz):
#     print(my_list)


# n = int(input("Сколько раз хочешь вывести фразу на экран? - "))
# while n> 0:
#     print("I am a programmer")
#     n -=1

n = int(input("Сколько раз хочешь вывести фразу на экран? - "))
while True:
    print("I am a programmer")
    n -= 1
    if n == 0:
        break
