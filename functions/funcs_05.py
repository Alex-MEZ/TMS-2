# Создать функцию, принимающая на вход неопределенное количество аргументом и возвращающая сумму args[i] * i
# Пример:  args = [4,3,2,1], 4 * 0 + 3 * 1 + 2 * 2 + 1 * 3 = 10
import calculate_sum
def sum(*args):
    print(args, type(args))
    result = 0
    for index, number in enumerate(args):
        result = index + number
    return result


def main():
    print(sum(1,2,3,4,5,6))


if __name__ == '__main__':
    main()
