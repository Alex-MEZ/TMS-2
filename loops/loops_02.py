# Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.

from random import randint

lst = [randint(1, 20) for i in range(5)]
print(lst)

print(sum([i for i in lst if i > 10]))
