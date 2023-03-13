# Просуммировать неопределенное количество чисел, вводимых пользователем,
# суммировать до тех пор, пока пользователь не введёт слово «стоп»

sum = 0
while True:
    i = input("Vvedi chislo (ili 'stop' dlya zaversheniya: ")
    if i == "stop":
        break
    sum += float(i)

print(int(sum))

# result_sum = 0
# while True:
#     number = input("Vvedi chislo (ili 'stop' dlya zaversheniya: ")
#     if i == "stop":
#         print('The end')
#         break
#     result_sum += int(number)
#     print(f'result_sum = {result_sum}')


# arr = input("Vvedi chislo(pishi stop kogda zahochesh ostanovitsya): ")
# i = int(arr)
# print(arr.isdigit())
# while arr.isdigit() == True:
#     i += i
#     print(i)
#     break
#
# while i in arr != 'stop':
#     i += i
#     # i = int(input("Vvedi chislo(pishi stop kogda zahochesh ostanovitsya): "))
#     print(i)
