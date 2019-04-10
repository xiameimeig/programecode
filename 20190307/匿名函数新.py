'''讲解匿名函数'''

# 携带参数的匿名函数
avg = lambda total,count:total/count
print(avg(12,3))

# 携带默认参数的匿名函数
ret1=(lambda a,b,c=100:a+b+c)(1,2,0)
print(ret1)
# 不定长参数
f = lambda *args:args
f1 = lambda **kwargs:kwargs
print(f(1,2,3,4,5,6))
print(f1(name='tony'))
# 真正的匿名函数
ret=(lambda a,b:a+b)(1,2)
print(ret)
print('########################匿名函数寻找三个数中的最大值最小值#######################')
print((lambda a,b,c:c if c >(a if a>b else b) else (a if a>b else b))(1,22,3))