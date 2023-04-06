# решение через декоратор


limit = 10 ** 5


def function_coll(limit=10 * 5):
    max_digit = 0
    max_steps = 0
    for digit in range(1, limit):
        corrent_steps = 0
        origin_digit = digit
        while digit != 1:
            if digit % 2 == 0:
                digit /= 2
            else:
                digit = digit * 3 + 1
