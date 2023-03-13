# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы, которые кратны 3.

from random import randint

n = int(input("chislo ="))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(0, 9))
    # print(arr_1)
    arr.append(arr_1)
print(arr)

# result = 0
# for arr_i in arr:
#     print(arr_i)
#     for i in arr_i:
#         result += i
# print(result)

result = 0
for arr_i in arr:
    print(arr_i)
    for i in arr_i:
        if i % 3 == 0:
            result += i
print(result)