'''实现兔子生兔子'''
def rab(month):
    '''
    该函数实现的是递归函数的写法，返回兔子的个数，古典问题
    :param month: 这是第几个月
    :return: 兔子的总个数
    '''
    if month == 1:
        return 1
    if month == 2:
        return 1
    else:
        count = rab(month-1)+rab(month-2)
        return count

print(rab(1))
print(rab(2))
print(rab(3))
print(rab(4))
print(rab(5))
print(rab(6))


