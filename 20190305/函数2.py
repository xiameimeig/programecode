'''实现函数的问题,多参数'''
def info(name,age,gender):
    '''
    实现打印个人信息的函数
    :param name:
    :param age:
    :param gender:
    :return:
    '''
    print('name:',name)
    print('age:',age)
    print('gender:',gender)
    return '哈哈哈哈','打印完成'

    # return后面的语句不执行（在函数里面）,如果返回多个数据，则打包成元组



ret = info('wang',19,'girl')
info(name='zhang',gender='boy',age=10)
print(ret)
# info('wang','boy',10)


# 有参数，有返回值
# 有参数，无返回值
# 无参数，有返回值
# 无参数，无返回值
