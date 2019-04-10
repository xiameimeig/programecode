str_new = 'i love work,work pay my money!'
str_new.isdigit()
# ret = str_new.count('work123')
# print(ret)

list_new = [1,2,3,4,'5',"6","asd"]
list_new[4] = 5
list_new[list_new.index('6')] =6

# list_new.pop()
# list_new.remove('asd')

del list_new[6]

del list_new
print(list_new)











# print(list_new[4:])
# print(list_new[::-1])















# 左闭右开

# name = input('请您输入姓名：')
#
# print('############打卡考勤系统#############')
# con = '%s，欢迎来到本系统,%s'%(name,str_new[2:])
# print(con)
# print('#####################################')