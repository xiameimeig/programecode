'''实现函数'''
def printinfo():
    print('wang')
    print(18)
    print('boy')


def addnum(num1,num2):
    '''
    实现两个数字的相加,num1,num2叫做形参
    :param num1: int,float
    :param num2: int,float
    :return:
    '''
    total = num1+num2
    print('函数体内执行的',total)
    return total


# printinfo()
ret = addnum(1,2)
print(ret)
# help(addnum)
# help(print)