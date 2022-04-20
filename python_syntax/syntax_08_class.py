# ========================================<8> Class ====================================================================
# 对象成员变量示例
# 类成员:
#  实例： 对象的数据（变量），对象的行为（方法）
#  类：   类的数据（变量），类的行为（方法），可以被所有对象共同操作的数据
#  静态方法：
#        实例方法操作实例变量，表示“个体”行为
#        类方法操作类变量，表示“大家”行为
#        静态方法不能操作数据，表示为函数都可以
# ======================================================================================================================
class Student:
    # __init__ 函数内初始化实例对象的属性
    # 参数self，是一个形参指向了类的对象的地址
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print("%s is %d years old, score is %d, sex is %s" % (self.name, self.age, self.score, self.sex))


student_list = [
    Student('赵敏', 28, 100, '女'),
    Student('苏大强', 68, 62, '男'),
    Student('明玉', 30, 95, '女'),
    Student('无忌', 29, 70, '男'),
    Student('张三丰', 130, 96, '男'),
]


def find_by_name(name: str):
    """
        find student by name
    """
    for student in student_list:
        if student.name == name:
            return student
    # return none                        如果一个函数没有返回值，其实默认返回的是none，所以这一行不用写


def find_by_sex(sex: str):
    """
        find student by sex
        return a list of matched student
    """
    result = []
    for student in student_list:
        if student.sex == sex:
            result.append(student)
    return result


stu1 = find_by_name('苏大强')
stu1.print_self_info()
male_student_list = find_by_sex('男')

# ======================================================================================================================
# 类成员变量示例
# ======================================================================================================================


class ICBC:
    """
        工商银行
    """
    # 这个变量属于类的变量，不属于类的实例对象
    total_money = 1000000

    # 创建一个类方法，来操作类的变量
    # 类方法不可访问实例成员，因此类方法不可以操作实例变量，但是实例方法可以操作类变量
    # 类方法的第一个参数cls，指向这个类本身(即:cls储存类的地址)
    @classmethod
    def print_total_money(cls):
        print('总行还剩%d块钱' % cls.total_money)

    def __init__(self, name, money):
        self.name = name
        self.money = money
        ICBC.total_money -= money


bank1 = ICBC('广渠门支行', 100000)
bank2 = ICBC('陶然亭支行', 100000)
ICBC.print_total_money()
