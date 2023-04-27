# Создать скрипт, который принимает имя фамилию и возраст и дописывает их в файл

import sys
import argparse

print(sys.argv)

parser = argparse.ArgumentParser()
parser.add_argument('-fn', ' --last_name', required=True)
parser.add_argument('-ln', 'first_name', required=True)
parser.add_argument('-a', type=int, required=True)

args = parser.parse_args()
with open("namefile.txt", 'a') as file:
    file.write(f"")
