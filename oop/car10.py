class Car():
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def speed_plus(self, number=5):
        self.__speed += number

    def speed_minus(self, number=5):
        self.__speed -= number

    def stop(self):
        self.__speed = 0

    def show_speed(self):
        return self.__speed
    @property
    def speed(self):
        return self.__speed

    def change_speed(self):
        self.__speed = - self.__speed


car = Car("Vw", "Golf", 2000)
print(car.show_speed())
print(car.speed)
car.speed_minus()
car.speed_minus()
car.speed_minus()
car.speed_minus()
car.speed_plus()
print(car.speed)