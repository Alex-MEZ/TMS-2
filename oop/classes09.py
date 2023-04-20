class All:
    def __init__(self, name, damage, health):
        self.__name = name
        self.__damage = damage
        self.__health = health

    def name(self):
        return self.__name
    @damage
    def damage(self):
        return self.__damage
    @health
    def health(self):
        return self.__health

    @damage.setter
    def damage(self, new_damage):
        self.__damage = new_damage

    @damage.getter
    def damage(self, new2_damage):
        self.__adres = new2_damage

    @health.setter
    def health(self, new_health):
        self.__health = new_health

    @health.getter
    def health(self, new2_health):
        self.__health = new2_health


class Dog(All):
class Cat(All):
class Snake(All):
class Insect(All):
class Zombi(All):
