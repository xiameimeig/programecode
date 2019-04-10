'''根据传入的参数不同，可以返回不同的装饰器'''
import time
def factory(arg=None):

    # 装饰器
    def timefun(func):
        def inner():
            if arg:
                print(func.__name__,time.ctime(),'第一种装饰器')
            else:
                print(func.__name__,time.time(),'第二种装饰器')
            # return func()
        return inner
    return timefun




@factory(123)
def test():
    print('被装饰的函数')

if __name__ == '__main__':
    test()