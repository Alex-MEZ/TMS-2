# Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.

# for i in range(5, 8):
#     for j in range(3):
#          print(f"i = {i}, j = {j}")

from random import randint

n = int(input("chislo ="))
arr = []
for i in range(n):
    arr_1 = []
    for j in range(n):
        arr_1.append(randint(1, 9))
    print(arr_1)
    arr.append(arr_1)
print(arr)

arr_3 = [[randint(1, 9)] for _ in range(n) for _ in range(n)]

print(arr_3)
