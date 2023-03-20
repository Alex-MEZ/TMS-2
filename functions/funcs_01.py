# Написать функцию, которая получает на вход имя и выводит строку вида: “Hello, {name}”.
# Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.

def my_func(name):
    print(f"Hello, {name}")


def main():
    arr = ["Boris", "Tony", "Al", "Somy", "Boss"]
    for name in arr:
        my_func(name)


if __name__ == '__main__':
    main()
