'''阶乘'''
# 1! = 1
# 2! = 1*2 = 1!*2 = 2
# 3! = 1*2*3 = 2!*3 = 6
# 4！= 1*2*3*4 = 3!*4 = 24
# fun1(n) = n* fun1(n-1)


def fun1(num):
    '''
    这是利用普通的方法来实现阶乘
    :param num: 参数
    :return: num!
    '''
    i = 1
    res = 1
    while i<=num:
        res = res*i
        i +=1
    return res

# print(fun1(1))
# print(fun1(2))
# print(fun1(3))
# print(fun1(4))


def func2(num):
    '''
    利用递归的方式完成阶乘
    :param num: 值
    :return: num!
    '''
    if num == 1:
        return 1
    else:
        return num*func2(num-1)

print(func2(1))
print(func2(2))
print(func2(3))
print(func2(4))

f = lambda :1+2
print(f())