# Написать декоратор, который будет выводить время выполнения функции

from datetime import datetime
from functools import wraps


def my_decorator(my_func):
    @wraps(my_func)
    def ineer(*args, **kwargs):
        start_time = datetime.now()
        result = my_func(*args, **kwargs)
        end_time = datetime.now()
        delta = end_time - start_time
        print(delta)
        return result

    return ineer()


@my_decorator
def very_iomportent_func():
    from time import sleep
    sleep(0)
    print("very importent func")


# def main():
#     arr = [i for i range(100)]
#     very_iomportent_func(arr)

