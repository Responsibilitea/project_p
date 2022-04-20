# ========================================<7> Exception ================================================================
# try:
#       code may have error
#       code may have error
#       ...
# except Exception1:                                               注： 多个except结构，捕获异常的顺序应按照先子类后父类的顺序，
#       code to fix exception1                                         为了避免遗漏可能出现的异常，可以在最后增加BaseException
#       code to fix exception1
# except Exception2:
#       code to fix exception2
#       code to fix exception2
# except BaseException:
#       code to fix base exception
#       code to fix base exception
# else:
#       code will run when no error occur in try block            注: 若果try中的代码出现错误，则else中的代码不会执行
#       ...
# finally:
#       code will run whatever in try block                       注: 无论try中的code是否有error，finally中的代码都会执行
#        ...

# ======================================================================================================================

try:
    a = int(input('enter first number\n'))
    b = int(input('enter second number\n'))
    result = a/b
    print('result : ', result)
except ZeroDivisionError:
    print('error : divider can not be zero')
except ValueError:
    print('input can only be number')
else:
    print('result : ', result)

print('program ends')

# ======================================================================================================================
# <7.1> 常见的error
# ZeroDivisionError 除数为零
# IndexError        序列中没有此索引
# KeyError          映射中无此键
# NameError         未声明/初始化 变量
# SyntaxError       Python语法错误
# ValueError        传入无效的参数
# ----------------------------------------------------------------------------------------------------------------------



# ======================================================================================================================
# <7.2> traceback 模块使用
# import traceback
# try:
#   ....
# except:
#   traceback.print_exc()                       打印错误信息
#
# ----------------------------------------------------------------------------------------------------------------------

