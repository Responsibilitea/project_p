# ========================================<8> Encapsulation ============================================================
# 封装
# ======================================================================================================================
# 通过名字前面加__对类的属性和方法进行私有化
class People:
    def __init__(self, name, age, weight):
        # python里对属性进行私有化，通过在属性明前加__，
        # 本质上是将属性名字改为了 _类名__属性名,借此来实现私有化
        self.name = name
        self.__age = None                           # age和weight此时为私有化属性
        self.set_age(age)
        self.__weight = weight

    def get_age(self):                              # 将类内的一些属性进行私有化后，一般都会提供必要的set，get方法
        return self.__age                           # 来让使用者从来外部来修改私有化的属性


    def set_age(self, age):                         # set_age方法需求输入的age在21-31之间，否则会报错
        if 21 <= age <= 31:                         # 这样通过私有化属性加set，get方法， 我们对该属性进行了保护
            self.__age = age
        else:
            raise ValueError("wrong age")


people1 = People("Jinx", 25, 87)
# python内置变量，将实例对象的所有变量存在__dict__字典中
print(people1.__dict__)             # result: {'name': 'Jinx', '_People__age': 87, '_People__weight': 87}

people1.__age = 107                 # 此代码在people1这个对象中从外部加入了一个名为__age的属性，并不能改编其类的本身私有化属性age
print(people1.__dict__)             # result: {'name': 'Jinx', '_People__age': 87, '_People__weight': 87, '__age': 107}

people1._People__age = 107          # 理解python的私有化原理后，通过(_类名__属性名)来强行改编私有化属性age
print(people1.__dict__)             # result: {'name': 'Jinx', '_People__age': 107, '_People__weight': 87, '__age': 107}


# ======================================================================================================================
# python里对属性封装的终极版！
#
# 通过@property修饰器对属性进行封装
# 公开的实例变量，缺少逻辑验证
# 私有的实例变量与两个公开的方法结合，又显得操作略显复杂
# 而属性可以将两个方法的使用方式像操作变量一样简单
# 1.定义：
#           @property
#           def name(self):
#               return self.__name
#
#           @name.setter
#           def name(self, name):
#               self.__name = name
# 2.调用：
#        读：变量 = 对象.属性名
#        写：对象.属性名 = 数据
# 3.说明：
#       --通常两个公开的属性，保护一个私有的变量
#       --@property负责读取，@属性名.setter负责写入
#       --只写: 属性名= property(None, 写入方法名)
#       --只读：只提供@property,不提供@属性名.setter
# ======================================================================================================================
class Hero:

    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        if attack < 999:
            self.__attack = attack
        else:
            raise ValueError("wrong attack")


lee = Hero("Lee", 100, 150)
print(lee.__dict__)






