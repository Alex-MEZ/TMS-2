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
    def __init__(self, height, weight, name, age, master, adres='Minsk'):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master
        self.__adres = adres

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @name.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, new_master):
        self.__master = new_master
    @property
    def adres(self):
        return self.__adres
    @adres.setter
    def adres(self,new_adres):
        self.__adres = new_adres

    # def get_adres(self):
    #     return self.__adres
    # def set_adres(self):
    #     return self.__adres
    # def jump(self):
    #     print('Jump!')
    # def run(self):
    #     print('Run!')
    # def bark(self):
    #     print('Bark!')
    # def change_name(self, new_name):
    #     self.name = new_name


dog_1 = Dog(name='Billy', age=1, height=22, weight=3, master='Timmy')
print(dog_1.__dict__)

dog_1 = Dog('a', 1, 2, 3, 'g')
print(dog_1.__dict__)
print(dog_1.get_adres())
dog_1.set_adres = 'Gomel'
dog_1.height = 50
print(dog_1.height)

dog_1.age = 22
print(dog_1.age)
