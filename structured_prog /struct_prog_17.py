# В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.

from random import randint

arr = [randint(1, 20) for _ in range(19)]
max_number = max(arr)
min_number = min(arr)

# Поиск максимального числа
# max_number_oun_solution = arr[0]
# for i in arr:
#     if i > max_number_oun_solution:
#         max_number_oun_solution = i

for index, number in enumerate(arr):
    if number % 2 == 0:
        arr[index] = max_number

print(arr, max_number)
