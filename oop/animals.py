# Создать файл animals.py.
# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.
import random
import string


class Pet:
    __count = 0

    def __init__(self, name, age, master, weight, height, jump):
        self.name = name
        self.__age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.jump = jump
        Pet.__count += 1

    @staticmethod
    def get_random_name():
        result = random.choice(string.ascii_uppercase) + '-' + str(random.randint(1, 99))
        return result

    @classmethod
    def get_counter(cls):
        return cls.__count

    def jump(self):
        print(f'Jump {self.jump} meters')

    @staticmethod
    def go():
        print('go')

    def run(self):
        print(f'run{self.name}')

    def jump(self):
        print(f'jump {self.name}')

    def birthday(self):
        self.__age += 1

    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.2

    def change_height(self, arg=None):
        if arg:
            self.height += arg
        else:
            self.height += 0.2

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f' repr for class {self.__class__} - {self.name}'

    def __eq__(self, other):
        return (self.name, self.__age, self.height, type(self)) == (other.name, other.__age, other.height)


def __ne__(self, other):
    return (self.name, self.__age, self.height, type(self)) != (other.name, other.__age, other.height)


class Dog(Pet):
    def bark(self):
        print(f'bark {self.name}')

    def jump(self, x):
        if x > 0.5:
            print("Dogs cannot kump so high")
        else:
            super().jump(x)


class Cat(Pet):
    def meow(self):
        print(f'meow {self.name}')

    def jump(self, x):
        if x > 0.5:
            print("Cats cannot jump so high")
        else:
            super().jump(x)


class Parrot(Pet):
    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.05

    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height, species)
        self.species = species

    def jump(self, x):
        if x > 0.5:
            print("Parrots cannot jump so high")
        else:
            super().jump(x)

    def fly(self):
        if self.height > 0.5:
            print(f"this parrot {self.name} cannot fly")
        else:
            print(f'fly {self.name}')


dog = Dog(name=Pet.get_random_name(), age=5, master='Boris', weight=10, height=15, jump=2)
cat = Cat('May', age=2, master='Boss', weight=11, height=12, jump=4)
parrot = Parrot('Kar', age=55, master='Manager', weight=120, height=152, species="wavy")
# dog.jump()
Parrot.go()
cat.change_weight()
parrot.change_weight()
print(Pet.get_counter())
print(Pet._Pet__count)
print(Pet.get_random_name())
print(dog)
s = 1
