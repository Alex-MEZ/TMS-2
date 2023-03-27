# Дан словарь, создать новый словарь, поменяв местам ключ и значение

my_dict ={'key_1': 'value_1'}
new_my_dict = {value: key for key, value in my_dict.items()}

print(new_my_dict)

new_my_dict_2={}
for key, value in my_dict.items():
    new_my_dict_2[value] = key
print(new_my_dict_2)