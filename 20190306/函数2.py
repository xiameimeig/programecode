'''实现函数的问题,多参数'''
def info(name,age,gender,city='hz'):
    '''
    :param name:
    :param age:
    :param gender:
    :param city: 默认参数,缺省参数，放在参数的最后面
    :return:
    '''
    print('name:',name)
    print('age:',age)
    print('gender:',gender)
    print('city:',city)
    return '哈哈哈哈','打印完成'

    # return后面的语句不执行（在函数里面）,如果返回多个数据，则打包成元组



ret = info('wang',19,'girl','bj')



# 有参数，有返回值
# 有参数，无返回值
# 无参数，有返回值
# 无参数，无返回值
