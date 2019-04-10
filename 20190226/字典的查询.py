'''实现字典的取值与获取打印'''
dict_new = {'name':'xiaowang','tel':13155555555,'age':18}
list_new = ['xiaowang',13155555555,18 ]


dict_new2 = {'name':'xiaozhang','tel':13155555556,'age':38}
# print(dict_new)
# print('名片的姓名',dict_new['name']) #通过直接取键名的方式获取值，如果没有键名报错


# print(dict_new.values())
# print(dict_new.keys())

ret1 = dict_new.get('name123','jerry')
ret2 = dict_new.get('name123')
print(ret1)
print(ret2)
# get获取指定的键名，如果不存在，不会报错,如果没有定义默认值，返回none，如果有返回自定义的默认值
