# Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
import random
from random import randint

while  True :
    num = random.randint (1, 10)
    print(num)
    if num == 7:
        break
