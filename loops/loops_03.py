# Просуммировать неопределенное количество чисел, вводимых пользователем,
# суммировать до тех пор, пока пользователь не введёт слово «стоп»

arr = input("Vvedi chislo(pishi stop kogda zahochesh ostanovitsya): ")
i = int(arr)
print(arr.isdigit())
while arr.isdigit() == True:
    i += i
    print(i)
    break

# while i in arr != 'stop':
#     i += i
#     # i = int(input("Vvedi chislo(pishi stop kogda zahochesh ostanovitsya): "))
#     print(i)
