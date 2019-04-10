'''类的基本构造'''
'''
狗：
类名：DOG
属性：品种、毛色、性别、名字、尾巴、腿儿个数
方法：跑、叫、咬人、拆家、吃饭
'''
class Dog:
    '''这是经典类的写法啊'''

    def run(self):
        print('这只狗正在跑')

    def bark(self):
        print('这只狗正在叫')

    def eat(self):
        print('这只狗正在吃饭')


    def introduce(self):
        '''介绍小狗的名字以及年龄'''
        print('dog1的名字%s,年龄是%s'%(dog1.name,dog1.age))

dog1 = Dog()
dog1.run()
dog1.bark()
dog1.eat()
dog1.name = '小白'
dog1.age = 3
dog1.introduce()

print(Dog.__mro__)
# 临时添加属性
# print(dog1.name)
# print('###################################')
# dog2 = Dog()
# dog2.run()
# dog2.bark()
# dog2.eat()
# dog2.age = 3
# print(dog2.age)


























class Person(object):
    '''这是新式类的写法'''
    pass