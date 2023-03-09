# Введите число. Если это число делиться на 1000 без остатка, то выведите на экран "millennium"

chislo = int(input("Vvedi chislo - "))

if chislo % 1000 == 0:
    print("millennium")
else:
    print("False")

if not chislo % 1000:
    print("millennium")
else:
    print("False")