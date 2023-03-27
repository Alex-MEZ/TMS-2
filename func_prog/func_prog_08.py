# Написать декоратор, который будет выводить время выполнения функции

from datetime import datetime
from functools import wraps

time_start = datetime.now()
def my_decorator(my_func):
    def inner():
        result = my_func
    return inner
time_end = datetime.now()

def my_func():
    time_out = time_end - time_start
    print(time_out)
print(my_func())
print(time_start,time_end)