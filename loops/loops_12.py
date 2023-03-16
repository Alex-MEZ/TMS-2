# for i, n in enumerate(range(10, 15)):
#     print(f'i = {i}, n = {n}')

# Дана целочисленная матрица А[n,m].
# Посчитать количество элементов матрицы,
# превосходящих среднее арифметическое значение элементов матрицы и сумма индексов которых четна.

n = int(input("chislo n = "))
m = int(input("chislo m = "))
from random import randint

arr = [[randint(1, 9) for _ in range(m)] for _ in range(n)]
count = 0
result_sum = 0
for arr_i in arr:
    for i in arr_i:
        result_sum += i
        count += 1
print(arr)
result_avg = result_sum / count
print(result_avg)
count = 0
for i, arr in enumerate(arr):
    for r, number in enumerate(arr_i):
        if number > result_avg and (i + r) % 2 == 0:
            count += 1
print(count)
