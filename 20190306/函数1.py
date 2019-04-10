'''探究默认参数的值'''
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
print('####################')
f(3,[3,2,1])
print('####################')
f(4)