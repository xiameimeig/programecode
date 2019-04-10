'''这是实现拷贝的几种方式'''
old_list = [[1],2,3,4,5]
# new_list = old_list
# print(id(old_list))
# print(id(new_list))
#
# old_list.append(6)
# print(old_list)
# print(new_list)
#
new2 = old_list.copy()
print(id(old_list))
print(id(new2))

new2.append('新列表的追加')
old_list[0].append('旧列表修改')
print(old_list)
print(new2)

# import copy
# new3 = copy.deepcopy(old_list)
# old_list[0].append('旧列表修改')
# print(id(new3))
# print(id(old_list))
# print('新列表',new3)
# print(old_list)
# #
# is
# ==

