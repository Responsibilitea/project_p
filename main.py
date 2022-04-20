# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Hero:
    power = 100

    def __init__(self, name, hp, attack, power):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.power = power


    def get_attack(self):
        return self.__attack


    def set_attack(self, attack):
        if attack < 999:
            self.__attack = attack
        else:
            raise ValueError("wrong attack")

    attack = property(get_attack, set_attack)


jinx = Hero("jinx", 1000, 88, 50)
print(jinx.__dict__)
jinx.hp = 2000
jinx.attack = 99
print(jinx.__dict__)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
