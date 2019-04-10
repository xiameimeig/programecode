'''这是列表的展示实例'''
list_new = ['hello', 'world', 'python', ',', 'python', 'is', 'the', 'best!']
list_new2 = ['hello',1]
print(list_new)
print(list_new2)
# 列表里面的元素可以这是不同的类型

# 切片
print(list_new[0])
print(list_new[1])
print('*******************************')
# print(list_new[10])
# list index out of range

for i in list_new:
    print(i)


j = 0
while j<len(list_new):
    print(list_new[j])
    # j += 1
    j = j+1