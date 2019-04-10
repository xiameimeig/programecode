'''这是实现自助餐小朋友购票的选择'''
# 如果身高在一米及以下：
#     免费
# 如果在1-1.4之间：
#     8折
# 如果大于1.4 ：
#     全票
height = float(input('请输入身高：'))
# if height <=1.0:
#     print('免费')
#     print('*******1********')
# if 1.0 < height <=1.4:
#     print('8折')
#     print('*******2********')
# if height > 1.4:
#     print('全票')
#     print('*******3********')
if height <=1.0:
    print('免费')
elif 1.0 < height <=1.4:
    print('8折')
else:
    print('全票')












# try:
#     #进行试错，如果出现错误，则进入到except里面，如果没有错误，则征程运行
#     height = float(input('请输入小朋友的身高：'))
# except:
#     height = -1
# print(type(height))
# if 0<height<=1.0:
#     print('小朋友是免费的')
# elif 1<height<=1.4:
#     print('小朋友是8折')
# elif 1.4<height<2:
#     print('全票')
# else:
#     print('请输入正确的身高')
#
