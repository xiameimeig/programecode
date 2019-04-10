'''这个功能实现了动态判断顾客是否可以买酒的判断'''
age = input('请输入您的年龄：')
print(type(age))
age = int(age)
print(type(age))
# 如果 年龄>18：
#     可以买酒

if age >= 18:
    print('可以买酒')
else:
    print('好好学习')
