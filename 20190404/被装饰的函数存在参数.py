def wrapper(func):
    def inner(*args,**kwargs):
        print('登录验证')
        func(*args,**kwargs)
    return inner

@wrapper
def cost(total,m,n,a,s,d):
    print('总付款金额：%s'%total)
    print('总付款金额:',total)

@wrapper
def confirm(name,num):
    print('确认收货')

if __name__ == '__main__':
    # cost(10,1,1,1,1,1)
    confirm('小王',1234)
    # cost = wrapper(cost)
    # wrapper(confirm)(1,2)