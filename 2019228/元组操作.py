'''实现元组'''
# tul_new = (12,)
tul_new = (12,'abc')
# 元组里面的元素可以是不同的类型
# print(type(tul_new))
print(tul_new[0]) #访问指定的元素
# tul_new[0] = '12' #修改元组，在Python中元组不支持修改其中的元素
tul_new.index(12)
print(tul_new)