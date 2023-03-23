# Написать программу для работы с матрицами:
# Создание
# Вывод
# Сумма всех элементов
# Нахождение максимального элемента
# Нахождение минимального элемента.

from random import randint
# Создание матриц (диапазон, колличество)
matrix = []
def create_matrix(matrix):
    matrix = [[randint(1, 10) for _ in range(4)] for _ in range(4)]
    return matrix

def output_matrix(matrix):
    for row in matrix:
        print(row)

def sum_matrix(matrix):
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total

def max_matrix(matrix):
    return max(max(row) for row in matrix)

def min_matrix(matrix):
    return  min(min(row) for row in matrix)

print(output_matrix(matrix))
print(create_matrix(matrix))
print(min_matrix(matrix))
print(max_matrix(matrix))
print(sum_matrix(matrix))

# def my_func("create", 'vyvod', 'summa', 'max_number', 'min_nimber'):
#     print()


# def main():
#     my_func(name)
#
#
# if __name__ == '__main__':
#     main()
