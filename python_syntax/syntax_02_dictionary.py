# ========================================<2> Dictionary ===============================================================
# 字典结构中的key不可以重复，value可以重复
# 字典中元素是无序的
# 字典中key必须是不可变对象
# 字典会浪费较大内存,但速度快
# ======================================================================================================================
# <2.1> creating dictionary
# ----------------------------------------------------------------------------------------------------------------------
# 1st way
dic_1 = {'lee': 100, 'chan': 98, 'alex': 45}
print(type(dic_1), dic_1)                           # result : <class 'dict'> {'lee': 100, 'chan': 98, 'alex': 45}

# 2nd way, using function dic()
dic_2 = dict(name='lee', age=20)
print(type(dic_2), dic_2)                           # result : <class 'dict'> {'name': 'lee', 'age': 20}

# 字典生成式， 将两个列表中的值组合成一个字典
list_1 = ['fruits', 'books', 'others']
list_2 = [96, 78, 85, 100, 120]
dic = {item: price for item, price in zip(list_1, list_2)}
print(dic)                                          # result : {'fruits': 96, 'books': 78, 'others': 85}

# <2.2> access dictionary
# ----------------------------------------------------------------------------------------------------------------------
dic_1 = {'lee': 100, 'chan': 98, 'alex': 45}
# 1st way to access dictionary, if key does not exist, error will occur
print(dic_1['alex'])                                # result : 45
# 2nd way,  if key does not exist, get() will return none
print(dic_1.get('chan'))                            # result : 98
print(dic_1.get('daisy'))                           # result : None
print(dic_1.get('daisy', 999))                      # result : 999

# to see whether a key is in the dictionary
print('lee' in dic_1)                               # result : Ture
print('lee' not in dic_1)                           # result : False

# <2.3> modify dictionary
# ----------------------------------------------------------------------------------------------------------------------
# delete a key
del dic_1['chan']
print(dic_1)                                        # result : {'lee': 100, 'alex': 45}
# delete all the key
dic_1.clear()
print(dic_1)                                        # result : {}

# add a key
dic_1 = {'lee': 100, 'chan': 98, 'alex': 45}
dic_1['jax'] = 999
print(dic_1)                                         # result : {'lee': 100, 'chan': 98, 'alex': 45, 'jax': 999}

# change value
dic_1['jax'] = 888
print(dic_1)                                        # result : {'lee': 100, 'chan': 98, 'alex': 45, 'jax': 888}

# <2.4>  dictionary function
# ----------------------------------------------------------------------------------------------------------------------
# function keys() get all the keys in dictionary
print(dic_1.keys())                                 # result : dict_keys(['lee', 'chan', 'alex', 'jax'])
print(list(dic_1.keys()))                           # transfer keys into a list

# function values() get all the values in dictionary
print(dic_1.values())                               # result : dict_values([100, 98, 45, 888])
print(list(dic_1.values()))                         # result : [100, 98, 45, 888]

# function items() get all the key-value pairs in dictionary
print(dic_1.items())
print(list(dic_1.items()))                         # result : [('lee', 100), ('chan', 98), ('alex', 45), ('jax', 888)]


# <2.5>  iterate dictionary
# ----------------------------------------------------------------------------------------------------------------------
print(dic_1)
for item in dic_1:
    print(item, dic_1[item])

