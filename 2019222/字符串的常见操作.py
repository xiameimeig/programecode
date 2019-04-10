'''实现字符串的常见操作的实例'''
str1 = 'hello world python , python is the best!'
ret = str1.find('pythonasd')
# find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
print(ret)
#  find寻找指定的字符串，如果找到就返回第一个字符的下标，如果找不到，返回-1

ret2 = str1.index('world')
print(ret2)
# index 寻找指定的字符串，如果找到就返回第一个字符的下标，如果找不到，就报错
# index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__

# 查找指定字符的个数
ret3 = str1.count('python123')
print(ret3)
# 寻找指定字符出现的个数，如果查找不到，返回0
# count(self, sub, start=None, end=None):  # real signature unknown; restored from __doc__

# 替换,将旧的字符串替换成新的字符串，如果原来的字符串中没有指定的字符串，返回原来的字符串，如果指定了替换的次数，则替换指定个数的旧字符串
ret4 = str1.replace('python','java',1)
print(ret4)
print(str1)
# replace(self, old, new, count=None): # real signature unknown; restored from __doc__

# 分隔符切片(非常重要),返回的是一个列表
ret5 = str1.split(' ')
ret6 = str1.split(' ',maxsplit=3)
print(ret5)
print(ret6)
print(str1)
# split(self, sep=None, maxsplit=-1)


str2 = 'python'
# ret7 = str2.rjust(20,'*')
ret7 = str2.rjust(20)
# 右对齐
print(str2)
print(ret7)
ret8 = str2.ljust(20)
print(ret8)
ret9 = str2.center(20)
print(ret9)

#  右对齐，左对齐，以及居中对齐，可以指定填充的值，但是一般空格填充


# 去空白字符（去空格）,或者指定去左边的空格或者右边的空格
ret10 = ret9.strip()
print(ret10)
ret9.lstrip()
ret9.rstrip()
print('#########################')
for i in str2:
    print(i)