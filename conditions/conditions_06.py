# Ввести почтовый адрес.
# Проверить доменное имя.
# В случае если оно gmail.com, вывести на экран имя почтового ящика.
# Иначе вывести надпись “DOMAIN NAME is not supported’

my_mail = input("You email: ")
if "@gmail.com" in my_mail:
    print(my_mail)
else:
    print(f'DOMAIN NAME is not supported')