a = 5
b = '0'

try:
    result = a / b
    print(f'a/b = {a / b}')
except ZeroDivisionError:
    print(f'a/b = infinity')
except TypeError:
    print(f'a/b = {int(a)} / {int(b)}')

