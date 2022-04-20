# ========================================<5> String ===================================================================
# 字符串为不可变序列
#
# ======================================================================================================================
# <5.1> creating String
# ----------------------------------------------------------------------------------------------------------------------
a = 'Python'
b = "Python"
c = '''Python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))                         # a, b, c三个变量的地址相同


# <5.1> search String
# ----------------------------------------------------------------------------------------------------------------------
# index(), 查找substr第一次出现的位置，如果不存在，则抛出valueError
# rindex(), 查找substr最后一次出现的位置，如果不存在，则抛出valueError
# find(), 查找substr第一次出现的位置，如果不存在，则返回-1
# rfind(), 查找substr最后一次出现的位置，如果不存在，则返回-1
s = 'hello,hello'
print(s.index('lo'))                    # result : 3
print(s.find('lo'))                     # result : 3
print(s.rindex('lo'))                   # result : 9
print(s.rfind('lo'))                    # result : 9

# <5.2> String 常用操作
# ----------------------------------------------------------------------------------------------------------------------
# string大小写转换
# upper(), 把字符串中的字符全部转换为大写
# lower(), 把字符串中的字符全部转换为小写
# swapcase(), 把字符串中的字符的大小写互换
# capitalize(), 把字符串中的第一个字符换为大写，其余字符换为小写
# title(), 把字符串里每个单词的第一个字符换成大写，每个单词的其余字符换成小写
s = 'hello,PYTHON'
print(s.upper())                        # result : HELLO,PYTHON
print(s.lower())                        # result : hello,python
print(s.swapcase())                     # result : HELLO,python
print(s.capitalize())                   # result : Hello,python
print(s.title())                        # result : Hello,Python

# string 对齐操作
# center(), 居中对齐，第一个参数设置宽度，第二个参数设定填充，默认填充为空格，如果设置宽度小于实际宽度则返回原字符串
# ljust(), 左对齐，第一个参数设置宽度，第二个参数设定填充，默认填充为空格，如果设置宽度小于实际宽度则返回原字符串
# rjust(), 右对齐，第一个参数设置宽度，第二个参数设定填充，默认填充为空格，如果设置宽度小于实际宽度则返回原字符串
# zfill(), 右对齐，左边用0填充，唯一的一个参数设置宽度，如果设置宽度小于实际宽度则返回原字符串
print(s.center(20, '*'))                # result : ****hello,PYTHON****
print(s.ljust(20, '*'))                 # result : hello,PYTHON********
print(s.rjust(20, '*'))                 # result : ********hello,PYTHON
print(s.zfill(20))                      # result : 00000000hello,PYTHON

# string的分隔
# split(), 默认用空格将字符串分隔，返回一个列表。通过参数sep来指定分隔符，参数maxsplit指定最大分隔次数，达到分隔次数上限后，剩余子串作为整体返回
# rsplit(),和split一样，区别为split从左侧开始分隔，rsplit()从右侧开始分隔
s1 = 'hello world python'
s2 = 'hello|world|python'
print(s1.split())                       # result : ['hello', 'world', 'python']
print(s2.split('|'))                    # result : ['hello', 'world', 'python']
print(s1.rsplit())                      # 如果不指定maxsplit，从左分隔和从右分隔的结果应该是一样的


# string内容判断方法
# isidentifier(), 判断指定的字符串是不是合法的标识符
# isspace(), 判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符等）
# isalpha(), 判断指定的字符串是否全部由字母组成
# isdecimal(), 判断指定的字符串是否全部由十进制的数字组成
# isnumeric(),  判断指定的字符串是否全部由数字组成
# isalnum(),  判断指定的字符串是否全部由字母和数字组成


# string的替换与合并
# replace(), 第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，返回替换后得到的字符串，替换前的字符串不发生变化，第三个参数可以指定最大
# 替换次数
# join(), 将列表或元组中的字符串合并成一个字符串
s = 'hello, python, python, python'
print(s.replace('python', 'java'))      # result : hello, java, java, java

lst = ['hello', 'java', 'python']
print('|'.join(lst))                    # result : hello|java|python

t = ('hello', 'java', 'python')
print(''.join(t))                       # result ：hellojavapython


# <5.3> String 的比较
# ----------------------------------------------------------------------------------------------------------------------
# 通过运算符 >, >=, <, <=, ==, != 来比较两个字符串的大小
# 比较规则： 首先比较两个字符串上的第一个字符，如果相等则继续比较下一个字符，依次比较，知道两个字符上的字符不相等时，字符的大小根据ascii码来判断
print('apple' > 'banana')               # result ：False
print(ord('a'), ord('b'))               # result ：97 98
print(chr(97), chr(98))                 # result ：a b


# <5.4> String 的切片操作
# ----------------------------------------------------------------------------------------------------------------------
# 字符串是不可变类型，因此不具备增删改等操作，切片操作将产生新的对象
# 切片规则 string[start:end:step]
s = 'hello,python'
print(s[:5])                            # result ：hello
print(s[6:])                            # result ：python
print(s[:5] + '!' + s[6:])              # result ：hello!python


# <5.5> String 格式化输出
# ----------------------------------------------------------------------------------------------------------------------
# 用%来做占位符 %s表示string %i或%d表示integer %f表示float
name = 'chan'
age = 20
print('my name is ：%s， I am %d years old' % (name, age))           # result ：my name is ：chan， I am 20 years old
# 控制宽度和精度
# %10d表示输出宽度为99， %.3f表示输出精度为小数点后三位
print('%10d' % 99)                                                  # result ：        99
print('%.3f' % 3.1415926)                                           # result ：3.142
# 同时指定控制输出宽度为10，精度为小数点后3位
print('%10.3f' % 3.1415926)

# 用{}来做占位符
print('{0} is {1} years old'.format(name, age))                   # result ：chan is 20 years old
# 输出3位数
print('{0:.3}'.format(3.1415926))                                 # result : 3.14
# 输出小数点后3位
print('{0:.3f}'.format(3.1415926))                                # result ：3.142
# 输出宽度为10，精度为小数点后3位
print('{0:10.3f}'.format(3.1415926))                                # result ：     3.142
# f'string来表示格式化
print(f'my name is {name}, and I am {age} years old')             # result ：my name is chan, and I am 20 years old


# <5.5> String 编码与解码
# ----------------------------------------------------------------------------------------------------------------------
# 字符串的底层是二进制数据，将字符串转换为二进制的过程叫编码，将二进制的数据转换为可读字符串的过程为解码
# 编码示例
s = '天涯共此时'
print(s.encode(encoding='GBK'))         # GBK这种编码格式中，一个汉字占2个字节，b表示binary
                                        # result ：b'\xcc\xec\xd1\xc4\xb9\xb2\xb4\xcb\xca\xb1'
print(s.encode(encoding='UTF-8'))       # UTF-8这种编码格式中，一个汉字占3个字节，b表示binary
                                        # result ：b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'

# 解码示例
byte1 = s.encode(encoding='GBK')
print(byte1.decode(encoding='GBK'))     # result ：天涯共此时

