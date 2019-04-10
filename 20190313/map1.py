# def func(x):
#     return x**2
# ret = map(func,[1,2,3])
# print(ret)
# for i in ret:
#     print(i)


# str1 = "k:1|k1:2|k2:3|k3:4"
# ret = str1.split('|')
# print(ret)
#
# new_dict = {}
#
# for obj in ret:
#     print(obj)
#     obj_split_list= obj.split(':') #例如;['k', '1']
#     new_dict[obj_split_list[0]] = obj_split_list[1]
#     print(new_dict)


s='k:1|k1:2|k2:3|k3:4'
d={}
s=s.split('|')
for i in s:
    a=i.split(':')
    d.update({a[0]:a[1]})
print(d)