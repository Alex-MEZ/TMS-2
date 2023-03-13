# Просуммировать неопределенное количество чисел, вводимых пользователем,
# суммировать до тех пор, пока пользователь не введёт слово «стоп»

sum =0
while True:
    num = input("Vvedi chislo (ili 'стоп' dlya zaversheniya: ")
    if num == "стоп":
        break
    sum += float(num)

print(sum)
# arr = input("Vvedi chislo(pishi stop kogda zahochesh ostanovitsya): ")
# i = int(arr)
# print(arr.isdigit())
# while arr.isdigit() == True:
#     i += i
#     print(i)
#     break

# while i in arr != 'stop':
#     i += i
#     # i = int(input("Vvedi chislo(pishi stop kogda zahochesh ostanovitsya): "))
#     print(i)
