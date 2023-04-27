# Написать скрипт - таймер.
# Программа при запуске принимает имя, фамилию, часы, минуты и секунды.
# После программа начинает обратный отсчет выводя оставшееся время.
# Программа должна хранить файл логирования с информацией о том кто запускал программу и когда.
import csv
import time
from argparse import ArgumentParser
import os
from datetime import timedelta

parser = ArgumentParser()
parser.add_argument('-ln', '--dir_name', required=True)
parser.add_argument('-fn', '--file_name', required=True)
parser.add_argument('-hs ', '--hours', default=0, type=int)
parser.add_argument('-m', '--minutes', default=0, type=int)
parser.add_argument('-s', '--seconds', default=10, type=int)
args = parser.parse_args()
print(type(args), args)
with open('log_times.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    if not os.path, exists('log_timer.csv'):
        fields = ['file name', ' last name', 'time stars']
        csvwriter.writerow(fields)
    csvwriter.writerow([args.first_name, args.last_name, time.time()])
my_timedelta = timedelta(houts=args.hours, minutes=args.minutes, seconds=args.seconds)
while my_timedelta:
    print(my_timedelta)
    my_timedelta -= timedelta(seconds=1)
    time.sleep(1)

# filepath = os.path.join(os.path.realpath(args.dir_name), args.file_name)
# last_str = args.file_name.split('.')[-1]
