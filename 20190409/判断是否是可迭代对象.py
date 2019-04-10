# 列表 字典
from collections import Iterable,Iterator

dict_new = {'a':1,'b':2}
ret1 = isinstance({1,2,3,4},Iterable)  #判断可否迭代
ret2 = isinstance(iter({1,2,3,4}),Iterator) # 判断是否是迭代器
print(ret1)
print(ret2)













# for i in dict_new.items():
#     print(i)