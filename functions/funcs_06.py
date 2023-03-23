# Создать функцию, которая принимает на вход неопределенное количество
# аргументов и возвращает их сумму и максимальное из них.

def sum_args(*args):
    # result = 0
    # for index, number in enumerate(args):
    #     result = index + number
    # return result
    return sum(args), max(args)


# def max_number(args):
#     # max_element = max(max(arr) for arr in args)
#     # return max_element
#     list_of_max_element = []
#     for arr in args:
#         max_element_in_arr = max(arr)
#         list_of_max_element.append(max_element_in_arr)
#     max_element = max(max_element_in_arr)
#     return max_element


def main():
    print(sum_args(1, 2, 3))


if __name__ == '__main__':
    main()
