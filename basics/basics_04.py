# Создать два списка a = [1,2,3,4] и b = [ ]
# Вывести на экран id a и b
# Присвоить b значение a (b=a)
# Вывести на экран id переменных
# Добавить элемент в список b
# Вывести на экран оба списка

from copy import copy, deepcopy


a = [1, 2, 3, 4, 5, ['as',101, [-1,-2,-3,]]]
b = []

print(f'first list id = {id(a)}, second list id = {id(b)}')
b = a
print(f'first list id = {id(a)}, second list id = {id(b)}')
print(b)
a.append(7)
print(a, b)
print(a is b)

b = deepcopy(a)
print(f'first list id = {id(a)}, second list id = {id(b)}')