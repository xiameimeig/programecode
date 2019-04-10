import time
def wrapper1(func):
    def inner(*args,**kwargs):
        print('登录验证',time.ctime())
        func(*args,**kwargs)
    return inner

def wrapper2(func):
    def inner(*args,**kwargs):
        print('登录验证',time.time())
        func(*args,**kwargs)
    return inner

def create(choose):
    '''
    这个函数创造的是装饰器，根据用户的需求，返回不同的装饰器
    :param choose: 这个参数控制的是装饰器的生成种类
    :return: 返回的是装饰器对象
    '''
    def warpper(func):
        def inner():
            if choose=='第一种':
                print('登录验证', time.ctime())
            elif choose=='第二种':
                print('登录验证', time.time())
            else:
                print('登录失败')
            func()
        return inner
    return warpper

# ret = create('第一种')
# print(ret)

@create('第3种')
def cost():
    print('总付款金额')


if __name__ == '__main__':
    cost()

    # warpper = create('第一种')
    # inner = warpper(cost)
    # inner()