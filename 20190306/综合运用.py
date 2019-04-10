'''函数参数的混合运用，有位置参数，默认，可变参数'''
def sum_num(a,*args,c=7,**kwargs):
    print(a)
    print(c)
    print(args)
    print(*args)
    # *解释器拆包传递
    print(kwargs)
    print(*kwargs)
    for key,value in kwargs.items():
        print('key',key,'value',value)
sum_num(1,2,3,c=5,m=6,n=7)