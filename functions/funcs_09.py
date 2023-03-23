# Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать функцию.
from random import randint


def schet(arr: list) -> dict:
    dict = {}
    for i in set(arr):
        dict[i] = arr.count(i)
    return dict


def schet_2(arr: list) -> dict:
    dict = {}
    for i in arr:
        if dict.get(i):
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict

def main():
    arr = [randint(0, 9) for _ in range(15)]
    print(arr)
    print(schet(arr))
    print(schet_2(arr))



if __name__ == '__main__':
    main()
