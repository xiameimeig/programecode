class Dog(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('这只狗正在吃饭')

    def introduce(self):
        '''介绍小狗的名字以及年龄'''
        print('dog1的名字%s,年龄是%s'%(self.name,self.age))


    def __str__(self):

        return '这只小狗的名字是%s，年龄是%s'%(self.name,self.age)

baibai = Dog('小白',18) # 这里面的参数自动传参给__init__方法
print(baibai)
print('######################')
hei = Dog('黑黑',8) # 这里面的参数自动传参给__init__方法
print(hei)
