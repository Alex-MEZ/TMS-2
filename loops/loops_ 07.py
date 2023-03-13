# Получить сумму кубов натуральных чисел от n до m, используя цикл for
n = int(input("Vvedi n - "))
m = int(input("Vvedi m - "))

result = 0
for i in range(n, m + 1):
    result += i ** 3
print(result)

# while n <= m:
#     result += n ** 3
#     n += 1
# print(result)
