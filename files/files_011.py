# Создать csv файл с данными о ежедневной погоде.
# Структура:  Дата, Место, Градусы, Скорость ветра.
# Найти среднюю погоду(скорость ветра и градусы) для Минск за последние 7 дней.
# Создать csv файл с данными о ежедневной погоде.
# Структура:  Дата, Место, Градусы, Скорость ветра.
# Найти среднюю погоду(скорость ветра и градусы) для Минск за последние 7 дней.
import csv
import datetime

arr = [["date", "place", "temp", "speed"],
       ["06-04-2023", "minsk", 26, 30],
       ["05-04-2023", "minsk", 11, 4],
       ["04-04-2023", "minsk", 6, 12],
       ["03-04-2023", "minsk", 24, 34],
       ["02-04-2023", "minsk", 16, 212],
       ["01-04-2023", "minsk", 19, 2],
       ["31-03-2023", "minsk", 54, 1]
       ]

delta_finish = datetime.datetime.now()
delta = datetime.timedelta(7)
delta_start = delta_finish - delta
print(delta_start, delta_finish, int(delta.days))

with open("test_temp.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(arr)
with open("test_temp.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    rows = [row for row in csvreader]
    for row in rows[1:]:
        row[0] = datetime.datetime.strptime(row[0], '%d-%m-%Y')
        row[2] = int(row[2])
        row[3] = int(row[3])
    total_degress = 0
    total_wind = 0
    for row in rows[1:]:
        if delta_start <= row[0] < delta_finish and row[1] == 'minsk':
            total_degress += row[2]
            total_wind += row[3]
        delta = int(delta.days)
        avg_degress = total_degress / delta
        avg_wind = total_wind / delta
        print(f'avg_degress: {avg_degress},avg_wind: {avg_wind}')
