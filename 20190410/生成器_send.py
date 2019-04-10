'''斐波那契数列的生成器版本实现'''
def fibo(num):
    a = 0
    b = 1
    current_index = 0
    print('##########111111111#######')
    while current_index<num:
        result = a # 0
        a,b = b,a+b # a=1,b=1
        current_index += 1 # 1
        print('#####2222222#######')
        params = yield result
        # params 是指生成器接收的参数 ，send传递的参数
        print('参数是',params)
        print('######3333333333333###########')


if __name__ == '__main__':
    ret = fibo(5)
    # print(ret)
    # print(ret.send(None))
    print(next(ret))
    print(ret.send('hello'))
    print(ret.send('python'))
    print(ret.send('java'))
    print(ret.send(1))