"""
    封装练习01：
        面向对象化：老张开车去东北
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


    @staticmethod
    def go_to(str_position, vehicle):
        vehicle.run(str_position)


class Car:

    @staticmethod
    def run(str_position):
        print("行驶到：", str_position)


lz = Person("老张")
car = Car()
lz.go_to("东北", car)


