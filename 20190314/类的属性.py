'''实现类的属性，对比实例的属性'''


class Peoson(object):
    # 类的属性
    country = '中国'
    def __init__(self,name,age):
        '''实例属性'''
        self.book = '我在隔壁'
        self.name = name
        self.age = age


if __name__ == '__main__':
    wang = Peoson('老王',48)
    print(wang.age)
    wang.age = 104
    print(wang.age)


    # print(Peoson.name)
    # print(Peoson.age)


#
# one = Peoson()
# print(one.book) #调用实例属性
# print(one.name) #通过实例调用类属性
# print(Peoson.name) # 通过类调用类属性
#
# # print(one.__age)
# # print(Peoson.__age)

