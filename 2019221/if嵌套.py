'''实现嵌套的实例：朋友邀请出去玩'''
# 如果有时间：
#     如果天气好：
#         出去玩
#     天气不好，在家待着
# 没有时间：
#     拒绝

# time = 0
# time = 1

# 这是进行时间的输入
try:
    #进行试错，如果出现错误，则进入到except里面，如果没有错误，则征程运行
    time = int(input('请输入有无时间，0-无时间，1-有时间：'))
except:
    time = -1

#  这是进行天气的输入
try:
    #进行试错，如果出现错误，则进入到except里面，如果没有错误，则征程运行
    wether = int(input('请输入天气，0-天气差，1-天气优秀：'))
except:
    wether = -1

if time==1:
    if wether==1:
        print('出去玩')
    elif wether==0:
        print('在家宅着')
    else:
        print('请输入正确的字符')

elif time==0:
    print('没有时间，拒绝')
else:
    print('请输入正确的数字')
