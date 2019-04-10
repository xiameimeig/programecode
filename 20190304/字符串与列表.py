'''列表与字符串的相互转换'''
str_new = 'hello world'
# str_to_list = list(str_new)
print(str_new.split())
print('#############################')
list_new = ['hello','world','!']
str1 = ''
for i in list_new:
    str1 +=i
print(str1)
print('################第二种方法##############')
str2 = ''.join(list_new)
print(str2)
print('*****************第三种********************')
str3 = ''.join([str(j) for j in list_new])
print(str3)