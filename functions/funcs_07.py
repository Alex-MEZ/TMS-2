# Создать функцию, которая принимает на вход неопределенное количество
# именованных аргументов и выводит на экран те из них, длина ключа которых четна.

def chet_args(**kwargs):
    for key, value in kwargs.items():
        if len(key) % 2 == 0:
           print(key,value)



def main():
    chet_args(a=2,bb=24,cccc=222)


if __name__ == '__main__':
    main()
