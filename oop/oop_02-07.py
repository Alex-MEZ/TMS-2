# # Создать два объекта класса Dog. Вывести их на экран
#
# class Dog():
#     def __init__(self, name):
#         self.name = name
#
#     def jump(self):
#         print('Jump!')
#
#     def run(self):
#         print('Run!')
#
#
# dog_1 = Dog("Bob")
# dog_2 = Dog("Sharik")
#
#
# # print(dog_1.name, dog_2.name)

class Dog():
    def __init__(self, height, weight, name, age, master,adres = 'Minsk'):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master
        self.__adres = adres


    def get_adres(self):
        return self.__adres

    def set_adres(self):
        return self.__adres

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print('Bark!')

    def change_name(self, new_name):
        self.name = new_name


dog_1 = Dog(name='Billy', age=1, height=22, weight=3, master='Timmy')
print(dog_1.__dict__)

dog_1 = Dog('a',1,2,3,'g')
print(dog_1.__dict__)
print(dog_1.get_adres())
dog_1.set_adres("Gomel")
print(dog_1.get_adres())