'''实现集合操作'''
# 集合增加一个元素或者多个元素，一个元素使用add，多个可以使用update
set_new = {'python','java'}
set_new.add('c++')
print(set_new)
set_new.update(['php','c#','js'])
set_new.add(12)
print(type(set_new))
print(set_new)

#删除元素
try:
    set_new.remove(12)
except:
    pass
print(set_new)
