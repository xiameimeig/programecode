'''实现列表的删除'''
list_new = [1,2,3,'a','python','java']
print('原来的列表',list_new)
# del list_new[4]
# print('删除操作之后',list_new)
# del 是按照指定的位置索引来进行操作

# list_new.remove('java123')
# print(list_new)

ret1 = list_new.pop()
1, 2, 3, 'a', 'python'
ret2 = list_new.pop()
1, 2, 3, 'a',
ret3 = list_new.pop()
1, 2, 3,
print(ret1)
print(ret2)
print(ret3)

print(list_new)