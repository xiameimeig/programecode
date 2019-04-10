class Test(object):
    '''这个类实现的功能是：类装饰器'''
    def __init__(self,func):
        print('######初始化########')
        print(func)
        self.func = func
    def __call__(self, *args, **kwargs):
        '''在当前方法内完成对函数的装饰'''
        print('已经完成登录的验证')
        self.func()

@Test
def cost():
    print('总付款金额')


if __name__ == '__main__':
    cost()


