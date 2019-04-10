'''
计算1-100之间所有整数的和
'''

i = 0
sum = 0
# sum = sum+i
# 1 +2+3

while i <101:
    print('##########################')
    print('此时是上一次循环的和',sum)
    print('此时的I',i)
    sum = sum + i
    print(sum)
    print('**************************')
    i += 1