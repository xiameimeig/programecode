'''1-20之间所有的偶数'''
# 第一种
list1 = [2,4,6,8,10,12,14,16,18,20]



# 第二种 利用range
# ret1 = list(range(21))
ret1 = list(range(2,21,2))
#  range(i, j) produces i, i+1, i+2, ..., j-1.
print(ret1)





# 第三种
num_list = []
i = 1
while i <21:
    if i%2 == 0:
        num_list.append(i)
    i+=1
print(num_list)


# 第四种

num_list_4 = []
for j in range(1,21):
    if j %2 == 0:
        num_list_4.append(j)
print('num_list_4',num_list_4)


# 第五种
num_list_5 = [obj**3 for obj in range(1,21) if obj%2==0]
print('Num_list_5',num_list_5)

num_list_new = ['666' for m in range(10)]
print(num_list_new)