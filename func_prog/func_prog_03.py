# Дан список словарей.
# Каждый словарь описывает машину(серийный номер и год выпуска).
# Создать новый список со всеми машинами, год выпуска которых больше n


my_list = [
    {'number': 1, 'yers': 1999},
    {'number': 2, 'yers': 2000},
    {'number': 3, 'yers': 2001},
    {'number': 4, 'yers': 2002},
]
n = 2000
new_my_list = [dict_element for dict_element in my_list if dict_element['yers'] > n]

print(new_my_list)

new_list_2 = []
for element in my_list:
    if element['yers'] > n:
        new_list_2.append(element)
    print(new_list_2)
