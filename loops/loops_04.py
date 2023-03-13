# Просуммировать неопределенное количество чисел, вводимых пользователем,
# суммировать до тех пор, пока пользователь не введёт слово «стоп». Не учитывать числа кратные 5

sum = 0
while True:
    num = input("Vvedi chislo (ili 'stop' dlya zaversheniya: ")
    if num == "stop":
        break
    num_1 = int(num)
    if num_1 % 5 == 0:
        continue
    sum += num_1
print(sum)
