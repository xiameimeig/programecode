'''补课'''
# 字符串

str1 = 'abcd'
str2 = "123"
_str = '123'

int_num = 123
print(type(str1))
print(type(str2))
print(type(int_num))
print(str2)
print(int_num)
i = 0
while i <3:

    age = int(input('请你输入您的年龄：'))
    # if 年龄大于等于18:
    #     买酒
    if age >= 18:
        print('可以买酒')
        #pass
    else:
        print('年龄未到')
    i = i+1