'''实现匿名函数'''
def func2(total,count):
    '''
    实现求多个数据的平均值
    :param total: 这个形参是指所有数据的和
    :param count: 这个形参是指数据的个数
    :return: 均值
    '''
    avg = total/count
    return avg
# func2()


avg = lambda total,count:total/count
print(avg(12,3))




ret=(lambda a,b:a+b)(1,2)
print(ret)

info_list = [
    {'name':'zhang1',"age":19},
    {'name':'zhang2',"age":20},
    {'name':'zhang3',"age":8}
]
# list1 = [1,2,4,5,22,0]
# list1.sort()
# print('普通',list1)
info_list.sort(key=lambda x:x['age'])
# sort这个函数在原来列表上做操作，没有返回值
print('排序',info_list)
