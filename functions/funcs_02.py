# Написать программу для работы с матрицами:
# Создание
# Вывод
# Сумма всех элементов
# Нахождение максимального элемента
# Нахождение минимального элемента.


from random import randint


# Создание матриц (диапазон, колличество)

def create_matrix(n):
    # matrix = [[randint(1, 10) for _ in range(n)] for _ in range(n)]
    matrix = []
    for _ range(n):
        arr_in = []
        for _ in range(n):
            arr_in.append(randint(0, 9))
        arr.append(arr_in)
    return matrix


def output_matrix(matrix):
    for row in matrix:
        print(row)


def sum_matrix(matrix: list) -> int:
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total


def max_matrix(matrix):
    # return max(max(row) for row in matrix)
    list_of_max_element = []
    for row in matrix:
        max_element_in_arr = max(row)
        list_of_max_element.append(max_element_in_arr)
    max_element = max(max_element_in_arr)
    return max_element


def min_matrix(matrix):
    # return min(min(row) for row in matrix)
    list_of_min_element = []
    for row in matrix:
        min_element_in_arr = min(row)
        list_of_min_element.append(min_element_in_arr)
    return min_element


print(output_matrix(matrix))
print(create_matrix(matrix))
print(min_matrix(matrix))
print(max_matrix(matrix))
print(sum_matrix(matrix))


def main():


if __name__ == '__main__':
    main()
