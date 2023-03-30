# Создать декоратор для функции,которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных
# - удалять все четные элементы из списка.
def my_decorator(func):
    # @wraps
    def inner(arr):
        arr = [i for i in arr if i % 2 != 0]
        result = func(arr)
        return result

    return inner


@my_decorator
def func(arr):
    print(arr)
    return arr, len(arr)


arr = [i for i in range(1, 20)]
print(func(arr))
