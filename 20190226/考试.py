# str1 = '123334567890asdv'
# 求列表的中的最大值与最小值[1,2,3,4,5,6,7,8,9,'a','asd','dfg',[123,234]]
# 统计字符串中字母出现的个数，最终的显示形式：a:123，b:3456 str2 =  'jdgsfhkshkdhjkqgakgksgf'
# list_new = [1,2,3,4,5,6,7,8,9,'a','asd','dfg',[123,234]]


list_new = [1,2,3,4,'a','s','e',1,2,3]
list_after = list()

for i in list_new:
    if i not in list_after:
        list_after.append(i)
print(list_after)

print(list(set(list_new)))










# print(list_new[::-1])
# list_new.reverse()
# print(list_new)



# int_list = []
# for i in list_new:
#     if type(i) == int:
#         int_list.append(i)
# print(int_list)


# str2 =  'jdgsfhkshkdhjkqgakgksgf'
# dict_new = {}
# for i in str2:
#     dict_new[i] = 1
# print(dict_new)



