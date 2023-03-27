# Дан список имен, отфильтровать все имена, где есть буква o

str = ['Kate', 'Boris', 'Roma', 'Vova']

new_str = list(filter(lambda x: "o" in x, str))
print(new_str)
