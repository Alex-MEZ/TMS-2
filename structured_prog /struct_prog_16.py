# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.
import random

n = int(random.randint(1, 900))
result_sum = 0
for i in range(1, n + 1):
    result_sum += 1 / i
print(result_sum)


