'''实现装饰器的功能'''
def wrapper(func):
    '''这个装饰器实现的是登录验证的功能'''
    def inner(*args,**kwargs):
        print('登录验证')
        func(*args,**kwargs)
    return inner


def cost(total):
    print('付款')


def joincar(sum):
    print('加入购物车')


def confirm(name,num):
    print('确认收货')


if __name__ == '__main__':
    cost()
    joincar()
    confirm()
