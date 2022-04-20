# ========================================<10> Inheritance =============================================================
# 下面例子展现类的继承与多态
# ======================================================================================================================

class Vehicle:
    """
        交通工具，代表所有具体的交通工具（火车、飞机）
    """

    def transport(self, str_position):
        # 因为父类太过抽象，所以写不出方法体
        pass


class Person:
    """
        客户端代码，用交通工具
    """
    def __init__(self, name):
        self.name = name

    def go_to(self, vehicle, str_position):
        """
            调用交通工具的运输方法
            多态， 传入的如果是car，则执行car的运输方法，传入的如果是飞机，则调用airplane的运输方法
        :param vehicle:
        :param str_position:
        :return:
        """
        vehicle.transport(str_position)

# -----------------以上代码由架构师完成，以下代码由程序员完成-------------------------------------


class Car(Vehicle):
    def transport(self, str_position):
        print("car go go go")


class Airplane(Vehicle):
    def transport(self, str_position):
        print("airplane fly fly fly")



