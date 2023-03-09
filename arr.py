# Есть список arr = [1,2,3,4,4,4,5,5,2]
# 1. Найти сумму всех числел
# 2. Найти среднее арифметическое
# 3. Найти среднее геометрическое
# 4. Найти массив квадратов
# 5*. Найти кумулятивную сумму
# 6*. Найти медиану
# 7*. Найти верхнюю и нижнюю квартиль
import statistics

import numpy

# 1
arr = [1, 2, 3, 4, 4, 4, 5, 5, 2]
print(sum(arr))

# 2
avg_arr = sum(arr) / len(arr)
print(avg_arr)

# 3
from scipy.stats import gmean

avg2_arr = arr
avg2_arr = gmean(avg2_arr)
print(avg2_arr)

# 4
print(sum(x ** 2 for x in arr))

# 5
from numpy import cumsum

massiv = numpy.cumsum(arr)
print(massiv[-1], massiv)
# or
# print(sum(arr))


#6
import statistics
print(statistics.median(arr))

#7 ???

