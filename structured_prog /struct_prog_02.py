# Ввести строку с клавиатуры.
# Вернуть результат логического выражения: длина строки не меньше 8 или в строке есть “python”.

my_str = input("Vvedi stroku: ")
len_my_str = len(my_str)
result_bool = len_my_str >= 8 or "python" in my_str

print(f'длина строки не меньше 8 или в строке есть “python” == {result_bool}')

#print(len(my_str) > 8 or (my_str "python")


