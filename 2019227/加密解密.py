list_new = ['ABCDEFGHI','JKLMNOPQR','STUVWXYZ*']

# 1号 :
str1 = 'ABCDEFGHI'
print(str1)
#2号 :BCDEFGHIA
str2 = str1[1:] + str1[0:1]
print(str2)
str3 = str1[2:] + str1[0:2]
print(str3)
