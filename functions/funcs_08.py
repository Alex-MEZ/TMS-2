# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций.

from functools import reduce


def my_func_1(*args):
    return sum(args) / len(args)


def my_func_2(*args):
    return reduce(lambda x, y: x * y, args) ** (1 / len(args))


def result_my_func(*args,mean_type):
    if mean_type == 1:
        return my_func_1(*args)
    elif mean_type == 0:
        return my_func_2(*args)
def main():
    print(f'result_my_func - {result_my_func(3,3,3,mean_type=1)}')
    print(f'srednee - {result_my_func(3,3,3,mean_type=0)}')



if __name__ == '__main__':
    main()
