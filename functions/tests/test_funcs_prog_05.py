
import unittest
from functions.funcs_05 import calculate_sum


class TestCalculateSum(unittest.TestCase):
    def test_calculate_sum(self):
        args = [4, 3, 2, 1]
        expected_result = 10
        result = calculate_sum(*args)
        self.assertEqual(result, expected_result)


if name == 'main':
    unittest.main()