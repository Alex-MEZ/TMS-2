# Ввести число с клавиатуры. Вернуть результат логического выражения: число больше 15 и число кратно 5.

arr = input("Число: ")

arr = int(arr)
#result = (arr > 15) and (arr % 5) == 0
print((arr > 15) and not (arr % 5))

#если введенное число > 5 -> True,
if arr > 15:
    print(True)
else:
    print(False)

# if arr > 15:
#     print(arr)
# else arr % 5:
#     print(arr)
# elif:
#    pass
