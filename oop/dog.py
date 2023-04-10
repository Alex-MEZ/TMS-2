class Dog():
    pet = 'dog'

    def __init__(self, name):
        self.name = name

    def bark(self):
        print('gav')

    def change_name(self, new_name):
        self.name = new_name


dog_1 = Dog("Bob")
dog_2 = Dog("Sharik")

dog_1.bark()
dog_1.name = "Bobik"
dog_1.change_name('Flint')
print(dog_1.pet)
print(dog_2.pet)
print(dog_1.name)
print(dog_2.name)
