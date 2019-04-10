# def showStyle():
#     print('有无数种')


class Person(object):
    '''创建Person类，
    属性有姓名、年龄、性别，
    创建方法personInfo,打印这个人的信息
    '''
    country = '中国'
    #类属性
    name = '哈哈哈'

    @staticmethod
    def a():
        print('a')


    @classmethod
    def info(cls,con):
        print('这是类方法')
        cls.country = con
        print(cls.country)

    @classmethod
    def countryInfo(cls):

        print('未修改前，默认国籍为：',cls.country)


    @classmethod
    def changeCountry(cls,newcountry):
        cls.country = newcountry
        print('此时修改之后的国籍为：',cls.country)

    @staticmethod
    def shoeStyle():
        # 静态方法
        print('有无数种')

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def personInfo(self):
        # print('姓名：%s,年龄：%s，性别：%s'%(self.name,self.age,self.gender))

        print('姓名：', self.name)

if __name__ == '__main__':
    # Person.shoeStyle()
    # Person.info('a')
    Person.personInfo()
    # ming = Person('a',10,'boy')
    # ming.shoeStyle()
    # ming.info('a')