n = int(input("Введи число для нахождения факторила: "))

def my_func(n):
    result =1
    for i in range(1, n+1):
        result *= i
    return result
print(my_func(n))