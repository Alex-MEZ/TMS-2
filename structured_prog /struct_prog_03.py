# Получить на ввод количество рублей и копеек и вывести в правильной форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки

rub = int(input("Vvedi rubli - "))
kop = int(input("Vvedi kopeiki - "))

if (rub != 0) and (kop != 0):
    print(f"{rub} rub,{kop} kop")
elif (rub != 0) and (kop == 0):
    print(f"{rub} rub")
else:
    print(f"{kop} kop")

if rub and kop:
    print(f"{rub} rub,{kop} kop")
elif rub and not kop:
    print(f"{rub} rub")
else:
    print(f"{kop} kop")