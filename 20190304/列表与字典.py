'''实现列表与字典的练习'''
list1 = ['name','age','gender']
list2 = ['laowang',19,'boy']
#
# ret = dict(zip(list1,list2))
# print(ret)
# for i  in ret:
#     print(i)

# dict_new = dict()
# for i in range(3):
#     dict_new[list1[i]] = list2[i]
# print(dict_new)

new_dict = {list1[i]:list2[i] for i in range(3)}
print(new_dict)


