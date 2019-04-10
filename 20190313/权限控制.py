'''继承'''
class ChickenSoup(object):
    '''祖传的，秘方,爷爷留下来的'''
    # 访问权限： 公有 私有__ 保护_
    def __init__(self):
        self.name = '爷爷祖传的秘方'
        self.__money = '10亿美金'
        self._price = '一份10元'
    def cookstyle(self):
        print('爷爷赚的钱',self.__money)
        print('加两斤的鸡，20g的盐,3斤水，熬成一锅')


class Student(ChickenSoup):
    '''爷爷的徒弟'''
    pass


if __name__ == '__main__':
    grandpa = ChickenSoup()
    print('#########强行获取###########')
    print(grandpa._ChickenSoup__money)
    # print('爷爷',grandpa.name)
    # print('爷爷',grandpa._price)
    # print('爷爷',grandpa.__money)
    # student = Student()
