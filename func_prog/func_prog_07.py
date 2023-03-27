# Дан список чисел.
# Найти произведение всех чисел, которые кратны 3.
from functools import reduce

arr = [1, 2, 3, 4, 5, 6, 24, 33]

new_arr = list(filter(lambda x: x % 3 == 0, arr))
new_arr_2 = reduce(lambda a, x: a * x, new_arr)
print(new_arr)
print(new_arr_2)

# new_arr_3 = reduce(lambda a, x: a * x, filter(lambda x: x % 3 == 0, arr))
# print(new_arr_3)
