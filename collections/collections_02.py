# Создать список произвольного содержания.
# После каждой операции выводить список на экран

my_list = [10, 20, 33, 45, 46, 234, 23433, 5235]
print(my_list)

my_list.append('Hello')
print(my_list)

my_list.remove(10)
print(my_list)

my_list.pop(1)
print(my_list)

my_list[2] = 'World'
print(my_list)

my_list.pop(2)
print(my_list)

print(my_list[::-1])