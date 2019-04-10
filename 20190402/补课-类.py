# class MyClass:
#     pass
#
# class HerClass(object):
#     pass
# 父类 --子类
# def a():
#     print('a')
# a()
class Cat(object):
    def __init__(self,nickname,color):
        '''init方法里面进行属性的赋值操作'''
        self.name = '猫'
        self.leg = 4
        self.nickname = nickname
        self.color = color

    def run(self,style=0):
        print(self.nickname) # 在类里面调用实例的属性
        if style == 1:
            print('这只猫正在跑')
        elif style == 2:
            print('这只猫正在跳')
        elif style == 0:
            print('默认姿势')
    def eat(self):
        print('这只猫吃饭')


# 创建一个实例对象
hellokitty = Cat('hellokitty','白')
print('这只猫的名字',hellokitty.nickname)
print(hellokitty.color)
# hellokitty.run(1)

print('######分割线##########')

jia = Cat('加菲猫','黄')
print(jia.nickname)
print(jia.leg)
# jia.run()
