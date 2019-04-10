'''实现的3个数相加并且求均值'''
def sum_avg(a,b,c):
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''
    total = a+b+c
    avg = total/3
    return total,avg


m,n = sum_avg(1,2,3)
print(m)
print(n)
# print(ret)
# print(ret[0])
# print(ret[1])