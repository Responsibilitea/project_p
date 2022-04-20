

class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print("my age is : ", self.__age)


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score


print(Student.mro())
s1 = Student("lee", 22, 87)
print(s1.name)
print(s1._Person__age)
