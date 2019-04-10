'''字典的修改'''
dict_new = {'name':'xiaowang','tel':13155555555,'age':18}
list_new = [1,2,3,'a','python','java']

list_new[0] = 'c++'
print(list_new)
dict_new['name'] = 'laowang' #键名存在，则对存在的键名对应的值进行修改
dict_new['name123'] = 'laowang' #键名不存在，则在原来的字典中增加该键值结构
print(dict_new)

del list_new[2]
del dict_new['name123'] #如果键名不存在，则报错
# del dict_new #说明删除整个字典
dict_new.clear() #清空字典
print(dict_new)