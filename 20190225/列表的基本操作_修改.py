'''列表的操作问题，主要是增加，修改以及删除'''
list_new = [1,2,3]
# 追加，增加元素append,没有返回值，在原来的数据上做操作
list_new.append(4)
print(list_new)
# list_new.append([5,6])
list_new.extend([5,6])
print(list_new)
# extend 将可迭代对象取出来，挨个放到原来的列表上，在末尾逐个追加

list_new.insert(10,['a','b'])
print(list_new)
# insert将元素插入到指定下标的前面，如果溢出下标，则添加到末尾


'''实现列表的修改'''
list_new = [1,2,3]
print(list_new)
list_new[0] = 'a'
print(list_new)
