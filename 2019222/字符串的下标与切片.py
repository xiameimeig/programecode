'''实现字符串的下标与切片的实例'''
str1 = 'i love python'
print(str1[0])
#字符串的下标从0开始
print(str1[2])

# 切片,左闭右开，取不到右边的位置上的值
print(str1[2:6])
print(str1[2:10:2])
print(str1[::2])
print(str1[::-1])
print(str1[::-2])