class Dog(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('这只狗正在吃饭')

    def introduce(self):
        '''介绍小狗的名字以及年龄'''
        print('dog1的名字%s,年龄是%s'%(self.name,self.age))


dog1 = Dog('小白',18) # 这里面的参数自动传参给__init__方法
dog2 = Dog('小黑',20)
print(dog1.name)
print(dog1.age)
dog1.introduce()
print(id(dog1))
print(Dog.__mro__)
print(dog1)
print(id(dog2))
print(dog2)

