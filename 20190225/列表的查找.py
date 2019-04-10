'''这是实现查找的实例'''
list_new = [1,2,3,'a','python','java']

# in
# not in

if 'pythonasd' in list_new:
    print('python在列表中')
else:
    print('不在')

ret1 = list_new.index('java')
print('下标',ret1)
# index(self, value, start=None, stop=None) 如果有，则返回第一次出现的下标位置，如果不存在则报错

ret2 = list_new.count('java123')
print(ret2)


# [['xiaowang',18,'python开发工程师','1222222222'],['xiaowang1',18,'python开发工程师'],['xiaowang',18,'python开发工程师']]xiaowang