'''实现判断数据类型'''
list_new = [[1,2,3],'abc',1,3,5,7,2.3,[2,3,4]]
dict_new = {'a':1,'b':2}
for obj in list_new:
    if isinstance(obj,list):
        for i in obj:
            print(i)
    elif isinstance(obj,int):
        print(obj)
    elif isinstance(obj,float):
        print(obj)
    else:
        pass


# print(isinstance(list_new,int))
# enumerate()
print('#######################枚举函数#####################')
ret = enumerate(list_new)
print(ret)
for m in ret:
    print(m)