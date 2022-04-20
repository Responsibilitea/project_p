# ========================================<3> tuple ====================================================================
# 元组tuple是不可变序列，无法对其进行修改
# 例：
# tuple_1 = (1, [20, 30, 40], 99)
# tuple_1[0] = 100         这里会报错，因为无法修改元组内容
# tuple_2[1].append(100)   这里不会报错，因为元组1号位上储存的为一个list，对list内元素进行修改，并没有修改该list object
# ======================================================================================================================
# <3.1> creating tuple
# ----------------------------------------------------------------------------------------------------------------------
tuple_1 = ('python', 'world', 99)
print(tuple_1, type(tuple_1))

tuple_2 = tuple(('element1', 'element2', 'element3'))
print(tuple_2, type(tuple_2))

# 如果元组里只有一个元素，创建时需要加括号和逗号
tuple_3 = ('elem1',)
print(tuple_3, type(tuple_3))

# 创建空元组
tuple_4 = ()
tuple_5 = tuple()

# <3.2> iterate tuple
# ----------------------------------------------------------------------------------------------------------------------
tuple_3 = ('python', 'world', 98, 100)
for item in tuple_3:
    print(item)
