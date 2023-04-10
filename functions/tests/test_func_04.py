from functions.funcs_04 import my_matrix, my_matrix_2


def test_my_matrix(self):
    n = 3
    random_from = 0
    random_to = 4
    matrix = my_matrix(n, random_from, random_to)
    self.assertEqual(len(matrix), n)
    for row in matrix:
        self.assertEqual(len(row), n)
        for element in row:
            self.assertTrue(random_from <= element <= random_to)


def test_my_matrix_2(self):
    n = 5
    random_from = -10
    random_to = 10
    matrix = my_matrix_2(n, random_from, random_to)
    self.assertEqual(len(matrix), n)
    for row in matrix:
        self.assertEqual(len(row), n)
        for element in row:
            self.assertTrue(random_from <= element <= random_to)
