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
        yield result
        print('#####3333333####')
        return 'ok'

if __name__ == '__main__':
    ret = fibo(5)
    # print(ret)
    while True:
        try:
            result1 = next(ret)
            print(result1)
        except StopIteration as e:
            print(e.value)
            break