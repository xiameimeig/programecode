'''这是实现一个简单的剪刀石头布的游戏，角色：玩家和电脑'''
import random

while True:

    # 使用随机整数随机出现一个值，来模拟电脑
    computer = random.randint(0,2)

    play = int(input('请输入一个值，0-石头，1-代表剪刀，2-代表布'))

    print('电脑的输入',computer)
    print('玩家的输入',play)
    #输，赢，平局
    # 剪刀-布 布-石头 石头-剪刀

    if (play==1 and computer==2) or (play==2 and computer==0) or (play==0 and computer==1):
        print('我赢啦')
    elif play==computer:
        print('平局')
    else:
        print('输了')

