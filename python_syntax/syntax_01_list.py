#
# ========================================<1> list =====================================================================
# ======================================================================================================================
# <1.1> creating list
# ----------------------------------------------------------------------------------------------------------------------
# 1st way to create list
list_1 = ['hello', 'world', 98]
# 2nd way to create list
list_2 = list(['hello', 'world', 98])
# 3rd way to create list with for loop
list_3 = [i for i in range(1, 10)]
print(list_3)                                   # result :   [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ----------------------------------------------------------------------------------------------------------------------
# <1.2> access the list
# ----------------------------------------------------------------------------------------------------------------------
# getting the index by giving specific element
list_1 = ['hello', 'world', 98, 'hello']
print(list_1.index('hello'))                   # print index of element 'hello',return first index if multiple
                                               # same elements in list

# Getting the element in the list by gaven index
# Index start with 0, if index has to < the length of list, otherwise will get an error
print(list_1[0])                               # print the first element in list
print(list_1[1])                               # print the second element in list


# slice the list  by list_1[start:stop:step], it results a new list , the element on stop index will not be included
list_3 = [10, 20, 30, 40, 50, 60, 70, 80]
print(list_3[2:5:1])                           # result : [30, 40, 50]


# ----------------------------------------------------------------------------------------------------------------------
# <1.3> iterate the list
# ----------------------------------------------------------------------------------------------------------------------
# to see a certain element is whether in the list or not, use key word in
list_4 = [10, 20, 30, 'hello', 'name']
print(10 in list_4)                            # result : true
print('hello' in list_4)                       # result : true
print('world' in list_4)                       # result : false

# to loop through list
for item in list_4:
    print(item)

# ----------------------------------------------------------------------------------------------------------------------
# <1.4> add modify the element in the list
# ----------------------------------------------------------------------------------------------------------------------
# using the function append() to add an element at the end of list
list_5 = [10, 20, 30]
print(list_5)                               # result : [10, 20, 30]
list_5.append(40)
print(list_5)                               # result : [10, 20, 30, 100]

# function extend() can extend another list to the original list
list_6 = [50, 60, 70, 80]
list_5.extend(list_6)
print(list_5)                               # result : [10, 20, 30, 40, 50, 60, 70, 80]

# function insert() can add an element at a specific index of the list
list_5.insert(2, 9999)
print(list_5)                               # result : [10, 20, 9999, 30, 40, 50, 60, 70, 80]

# using slicing to add any elements in the list
print(id(list_5), list_5)       # result : 2889365337920 [10, 20, 9999, 30, 40, 50, 60, 70, 80]
list_7 = ['cool', 'lisa', 'jason', 'chan']

list_5[3:5:] = list_7           # change the element of index 3,4 in the list_5 to the list_7
print(id(list_5), list_5)       # result : 2889365337920 [10, 20, 9999, 'cool', 'lisa', 'jason', 'chan', 50, 60, 70, 80]

# ----------------------------------------------------------------------------------------------------------------------
# <1.5> delete the element in the list
# ----------------------------------------------------------------------------------------------------------------------
# function remove() to remove an element in the list with specific name
# remove the first element if multiple same element are in the list
list_8 = [10, 20, 30, 40, 50, 30, 60]
print(list_8)                   # result : [10, 20, 30, 40, 50, 30, 60]
list_8.remove(30)
print(list_8)                   # result : [10, 20, 40, 50, 30, 60]

# function pop() to remove an element with gaven index number
# it removes the last element in the list  if not give the index
list_8.pop(3)
print(list_8)                   # result : [10, 20, 40, 30, 60]
list_8.pop()
print(list_8)                   # result : [10, 20, 40, 30]

# slicing the list to remove multiple elements, but it will result a new list object
print(list_8)                   # result : [10, 20, 40, 30]
list_9 = list_8[1:3]
print(list_9)                   # result : [20, 40]
# slicing the list without creating a new list object
print(list_8)                   # result : [10, 20, 40, 30]
list_8[1:3] = []
print(list_8)                   # result : [10, 30]

# function clear() to delete all the elements in the list, the list object still exists
print(list_8)                   # result : [10, 30]
list_8.clear()
print(list_8)                   # result : []

# use keyword del to delete list object
del list_8
# print(list_8)      this will result an error, cause list_8 object no long exist

# ----------------------------------------------------------------------------------------------------------------------
# <1.6> modify the element in the list
# ----------------------------------------------------------------------------------------------------------------------
list_8 = [10, 20, 30, 40, 50]
print(list_8)                       # result : [10, 20, 30, 40, 50]
list_8[2] = 999
print(list_8)                       # result : [10, 20, 999, 40, 50]

# slicing the list
print(id(list_8), list_8)           # result :2863112600512 [10, 20, 999, 40, 50]
list_8[1:3] = ['lee', 'jack', 'chris', 'chan']
print(id(list_8), list_8)           # result : 2863112600512 [10, 'lee', 'jack', 'chris', 'chan', 40, 50]

# ----------------------------------------------------------------------------------------------------------------------
# <1.7> sort the list
# ----------------------------------------------------------------------------------------------------------------------
# sort the list without creating a new list
list_sort = [80, 3, 299, 42, 99, 76, 88]
print(id(list_sort), list_sort)     # result : 2115847405504 [80, 3, 299, 42, 99, 76, 88]
list_sort.sort()                    # sort the list with ascend order
print(id(list_sort), list_sort)     # result : 2115847405504 [3, 42, 76, 80, 88, 99, 299]

list_sort.sort(reverse=True)        # sort the list with descend order
print(id(list_sort), list_sort)     # result : 2115847405504 [299, 99, 88, 80, 76, 42, 3]

# sort the list and create a new list
list_sort = [80, 3, 299, 42, 99, 76, 88]
print(id(list_sort), list_sort)     # result : 2761529844544 [80, 3, 299, 42, 99, 76, 88]
new_list = sorted(list_sort)        # sort the list with ascend order
print(id(list_sort), list_sort)     # result : 2761529844544 [80, 3, 299, 42, 99, 76, 88]
print(id(new_list), new_list)       # result : 2761532456768 [3, 42, 76, 80, 88, 99, 299]

