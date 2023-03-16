# Дано число. Найти сумму и произведение его цифр.


# 1
number = 123456
result_sum = 0
result_m = 1
list_of_number = list(str(number))
for i in list_of_number:
    result_sum += int(i)
    result_m *= int(i)
print((result_sum), (result_m))

# 2
result_sum = 0
result_m = 1
while number:
    last_n = number % 10
    result_sum += last_n
    result_m *= last_n
    number //= 10
print((result_sum), (result_m))
