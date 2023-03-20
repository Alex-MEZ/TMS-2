# Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия.
# Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
# Примечание: данное задание подразумевает самостоятельное изучение принципов работы со временем в Python(библиотека datetime)
from datetime import datetime, timedelta

arr = [
    {'number': 1,
     'start': 'Minsk',
     'start_time': datetime(2023, 3, 20, 12, 30),
     'finish': 'Brest',
     'end_time': datetime(2023, 3, 20, 4, 30)
     },
    {'number': 2,
     'start': 'Grodno',
     'start_time': datetime(2023, 3, 20, 8, 30),
     'finish': 'Brest',
     'end_time': datetime(2023, 3, 20, 10, 30)
     },
    {'number': 3,
     'start': 'Gomel',
     'start_time': datetime(2023, 3, 20, 20, 30),
     'finish': 'Brest',
     'end_time': datetime(2023, 3, 20, 4, 30)
     }
]

timedata_train = timedelta(hours=7, minutes=20)

for dict in arr:
    time_in_road = dict["start_time"] - dict["end_time"]
    if time_in_road > timedata_train:
        print(dict)