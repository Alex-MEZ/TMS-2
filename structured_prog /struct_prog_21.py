# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105

x = int(input("От числа -"))
y = int(input("До числа -"))

# a = int(input("Первый делитель -"))
# b = int(input("Второй делитель -"))
# x = 100
# y = 105

# Основное задание
for i in range(x, y + 1):
    print("Делитель числа", i, "кроме 1 и самого числа: ", end='')
    for j in range(2, i):
        if i % j == 0:
            print(j, end=' ')
    print()

# # Похожий пример #1
# for i in range(x, y + 1):
#     if i % a == 0 and i % b == 0:
#         print(i)


# # Еще одна #2
# for i in range(2, x):
#     if x % i == 0:
#         print(i, end=' ')


# # Задание аналог №3
# for i in range(x, y + 1):
#     count = 0
#     for j in range(2, i):
#         if i % j == 0:
#             count += 1
#             if count == 2:
#                 print(i, end=" ")
#                 break
#