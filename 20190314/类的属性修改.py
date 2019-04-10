'''实现类的属性，对比实例的属性'''


class Peoson(object):
    # 类的属性
    country = '中国'
    def __init__(self):
        '''实例属性'''
        self.book = '我在隔壁'
        self.name = '小张'
        self.age = 13


if __name__ == '__main__':
    print('类属性:',Peoson.country)
    zhang = Peoson()
    zhang.country = '新加坡' #增加了一个实例属性
    Peoson.country = '南非' #真正修改类属性
    print('实例调用的类属性：',zhang.country)
    print('类属性:', Peoson.country)


