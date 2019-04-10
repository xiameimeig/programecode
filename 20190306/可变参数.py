'''可变参数的实例'''
# help(print)
# print(print.__doc__) #魔法方法
def person_info(*args):
    '''

    :param args: 将所有的位置参数打包成元组
    :return:
    '''
    print(args)
    for i in args:
        print(i)

person_info(12,13,'zhang')
person_info(1)
person_info(1,2,4,5,6,7,8,9,11,12)

