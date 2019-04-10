'''
实现集合的实例，与字典的对比
'''
#  手机付款
# 结果符合
'''
健身房看
时间开始发酵法律
斯卡哈分开发货

'''
str_new = 'python is best!' # 'python is "good"'
list_new = [1,2,3,'a','b','c',"d",'c',1,2,3]
dict_new = {'name':'xiaowang','age':18}
print(dict_new.get('name123'))
# print(dict_new['name123'])

set_new = {'python','good','java','c++','c++'}
# 集合可以自动去重
print(set_new)
# set_new2 = {'python'}
# print(type(set_new))
# print(type(set_new2))
print('原来的列表',list_new)
print('现在的列表',set(list_new))
