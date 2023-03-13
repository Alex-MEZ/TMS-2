# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n) используя цикл while

n = int(input("Vvedi chislo: "))
result = 0
i = 1
while i <= n:
    result += i ** 3
    i += 1
print(result)

result_2 = sum([i ** 3 for i in range(1, n + 1)])
print(result_2)
