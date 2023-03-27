# Дан список чисел. Вернуть список, где каждое число переведено в строку
# [5, 3] -> [‘5’, ‘3’]
#
arr = [1, 2, 3, 4, 5, 6, 7]
#
# def my_func(n):
#     return n * 2
#
# arr_2 = list(map(my_func, arr))
# print(arr_2)
#
# arr_3 = list(map(lambda x: x * 2, arr))
# print(arr_3)

my_list = list(map(str, arr))
print(my_list)
