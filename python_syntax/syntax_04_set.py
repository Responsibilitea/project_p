# ========================================<4> Set ======================================================================
# 集合set中的元素不允许重复，重复元素会自动会删除
# 集合中元素是无序的
# ======================================================================================================================
# <3.1> creating set
# ----------------------------------------------------------------------------------------------------------------------
set_1 = {1, 2, 3, 4, 5, 9, 4, 3}
print(set_1)                                        # result : {1, 2, 3, 4, 5, 9}

set_2 = set([1, 2, 3, 4, 5, 3, 2, 1])
print(set_2)                                        # result : {1, 2, 3, 4, 5}

# 创建空集合
set_3 = set()
print(type(set_3), set_3)                           # result : <class 'set'> set()

# 集合生成式
set_4 = {i * i for i in range(6)}
print(set_4)                                        # result :{0, 1, 4, 9, 16, 25}

# <3.2> access set
# ----------------------------------------------------------------------------------------------------------------------
# 判断元素是否在set中
set_1 = {10, 20, 30, 40, 50}
print(10 in set_1)                                  # result : True
print(10 not in set_1)                              # result : False
print(100 in set_1)                                 # result : False

# <3.3> modify set
# ----------------------------------------------------------------------------------------------------------------------
# 添加一个元素进set
set_1.add(80)
print(set_1)                                        # result : {80, 50, 20, 40, 10, 30}

# 将另一个set, list, tuple添加进set
set_1.update({1, 2})
set_1.update([3, 4])
set_1.update([5, 6])
print(set_1)                                        # result : {1, 2, 3, 4, 5, 6, 10, 80, 20, 30, 40, 50}

# 删除集合
# remove()删除集合中的一个元素，如果指定元素不存在，则抛出异常
set_1.remove(50)
print(set_1)                                        # result : {1, 2, 3, 4, 5, 6, 10, 80, 20, 30, 40}
# discard()删除集合中的一个元素，如果指定元素不存在，不会抛出异常
set_1.discard(100)
print(set_1)                                        # result : {1, 2, 3, 4, 5, 6, 10, 80, 20, 30, 40}
# pop() 删除集合中的任意一个元素
set_1.pop()
print(set_1)                                        # result : {2, 3, 4, 5, 6, 10, 80, 20, 30, 40}
# clear() 清空集合
set_1.clear()
print(set_1)                                        # result : set()


# <3.4> relations between sets
# ----------------------------------------------------------------------------------------------------------------------
# 判断两个集合是否相等（两个集合内的元素是否相同）
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 2, 1, 5}
print(set_1 == set_2)                               # result : True
print(set_1 != set_2)                               # result : False

# 判断一个集合是否为另一个集合的子集
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 2, 1, 5, 6}
set_3 = {3, 4, 2, 1, 5}
set_4 = {3, 4, 2, 1, 8}
print(set_1.issubset(set_2))                        # result : True
print(set_1.issubset(set_3))                        # result : True
print(set_1.issubset(set_4))                        # result : False

# 判断一个集合是否为另一个集合的超集
print(set_2.issuperset(set_1))                      # result : True
print(set_3.issuperset(set_1))                      # result : True
print(set_4.issuperset(set_1))                      # result : False

# 判断两个集合是否无交集
print(set_1.isdisjoint(set_4))                      # result : False  因为set_1和set_4是有交集的 所以返回false

# 求交集
set_1 = {10, 20, 30, 40}
set_2 = {20, 30, 40, 50, 60}
print(set_1.intersection(set_2))                    # result : {40, 20, 30}
print(set_1 & set_2)                                # result : {40, 20, 30}

# 求并集
print(set_1.union(set_2))                           # result : {40, 10, 50, 20, 60, 30}
print(set_1 | set_2)                                # result : {40, 10, 50, 20, 60, 30}

# 求差集
print(set_1.difference(set_2))                      # result : {10}
print(set_1 - set_2)                                # result : {10}

# 求对称差集
print(set_1.symmetric_difference(set_2))            # result : {50, 10, 60}
print(set_1 ^ set_2)                                # result : {50, 10, 60}

