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
    def __init__(self, height, weight, name, age, master):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master

    def get_master(self):
        return self.__master

    def set_master(self):
        return self.__master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print('Bark!')

    def change_name(self, new_name):
        self.name = new_name


dog_1 = Dog(name='Billy', age=1, height=22, weight=3, master='alex')
print(dog_1.__dict__)

dog_1 = Dog('a',1,2,3,'g')
print(dog_1.__dict__)
