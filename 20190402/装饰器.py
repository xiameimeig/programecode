'''实现装饰器'''
'''闭包的实现'''
# y = kx+b

def line_conf(k,b): # K,B 自由变量，环境变量

    def line(x):
        '''真正实现一次函数'''
        return k*x+b
    return line

line1 = line_conf(1.0,1.0) # X+1
line2 = line_conf(2,1) # 2x+1
print(type(line1))
result1 = line1(8) # 相当于执行的是 line(8)
result2 = line2(8)
print('一次函数执行的结果是',result1)
print('一次函数执行的结果是',result2)
print(line1.__closure__)



# def line(k,b,x):
#     return k*x+b
# LEGB