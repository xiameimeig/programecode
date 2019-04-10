'''字符串的操作'''
# str_new = 'python is good,java is good!python'
# # 查找指定的字符串（三种方法）
# ret1 = str_new.index('python')
# # index(self, sub, start=None, end=None)
# print(ret1)
# # print(str_new[0:6])
# ret2 = str_new.find('python123')
# # find(self, sub, start=None, end=None)
# print(ret2)
# ret3 = str_new.count('python123')
# print(ret3)
#
# # 字符串的替换
# # 字符串的分割
# # 去空格

'''列表'''
list_new = [1,2,3,'a','b','c']
print(list_new[0:2])
print(list_new[::-1])
print('***************************')
for i in list_new:
    print(i)
print('***************************')
ret = list_new.append([100,200])
print(list_new)
print(ret)
list_new.extend([100,'m','m'])
print(list_new)
list_new.insert(0,'java')
print(list_new)
print('#############################')
ret1 = list_new.pop()
ret2 = list_new.pop()
ret3 = list_new.pop()
ret4 = list_new.pop()
print(ret1)
print(ret2)
print(ret3)
print(ret4)
print(list_new)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
list_new.remove('java')
print(list_new)
del list_new[2]
del list_new
print(list_new)

