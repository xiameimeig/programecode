'''实现类的私有属性和方法'''

class Father(object):
    '''实现父类、基类'''
    def __init__(self):
        self.nickname = '隔壁老王'
        self._name = '王一二'
        self.__money = '8百块'


    def printname(self):
        print(self._name)


    def __costmoney(self):
        '''定义私有属性'''
        print(self.__money)

    def costmoney(self):
        '''调用私有方法'''
        self.__costmoney()

    def chagenickname(self):
        '''实现修改他的昵称'''
        print('修改之前的昵称：',self.nickname)
        self.nickname = input('请输入修改之后的昵称')
        print('修改之后的昵称：',self.nickname)



class Son(Father):
    '''实现子类，派生类'''
    pass


if __name__ == '__main__':
    # 创建一个父类的实例
    A = Father()
    # A.costmoney()
    print(A._Father__money)
    # A._Father__costmoney()
    # #  A调用属性
    # # print(A.__money) 实例不可以直接访问私有属性
    # print(A._name) #实例直接访问保护属性
    # print(A.nickname)
    #
    # a = Son()
    # a.costmoney()
    # # print(a.__money)
    # print(a._name)
    # print(a.nickname)
