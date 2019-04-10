'''实现装饰器的功能'''
def wrapper(func):
    '''这个装饰器实现的是登录验证的功能'''
    def inner():
        print('登录验证')
        func()
    return inner

@wrapper
def cost():
    print('付款')


@wrapper
def joincar():
    print('加入购物车')

#
# if __name__ == '__main__':
#     # func = wrapper(joincar)
#     # func()
#     cost()
#     print('##########################')
#     joincar()


