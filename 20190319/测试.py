# a = 10
# b = 0
# # print(a/b)
#
# f = open('a.txt')

# try:
#     ret = int(input('请输入整型数字：'))
# except:
#     print('发生错误')
# else:
#
#     print(ret)
#
# finally:
#     print('一定进入')

str1 = 'asd'
ret = str1.isdigit()
print(ret)


num_str = input('请输入需要输入的数字：')
if num_str.isdigit():
    num = int(num_str)
    print(num)