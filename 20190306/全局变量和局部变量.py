'''这是实现全局变量与局部变量的实例'''

# def info1():
#     name = 'wang'
#     print('修改之前',name)
#
#     name = 'zhang'
#     print('修改之后', name)
#
#
# def info2():
#     name = 'li'
#     print(name)
#
#
# # info1()
# info2()


# 全局变量

name = 'zhang'
age = 18

def info1():
    name = 'wang'
    print(name)


def info2():
    '''
    这个函数实现修改全局变量的功能
    :return:
    '''
    global name,age

    name='xxxxxxx'
    print(name)


def info3():
    print(name1)



info1()
# info2()
info3()


# L局部命名空间  E(外部嵌套函数的命名空间)  G(全局命名空间) B 内置命名空间