'''实现函数之间的调用关系，func1:实现数据的相加操作，func2实现数据的求平均值操作'''
def func1(*args):
    '''

    :param args: 输入需要相加的数据
    :return: 返回所有数据的和
    '''
    # print(args)
    sum = 0
    data_len = len(args)
    # 这是求的数据的个数
    for obj in args:
        sum += obj
    return sum,data_len



def func2(total,count):
    '''
    实现求多个数据的平均值
    :param total: 这个形参是指所有数据的和
    :param count: 这个形参是指数据的个数
    :return: 均值
    '''
    avg = total/count
    return avg


ret,data_len = func1(1,2,3,6,7,99,123,134)
print('所有数据的和',ret)
print('所有数据的个数',data_len)
avg = func2(ret,data_len)
print('所有数据的平均值',avg)