'''继承'''
class ChickenSoup(object):
    '''祖传的，秘方,爷爷留下来的'''
    def __init__(self):
        self.name = '爷爷祖传的秘方'
        self.money = '10亿美金'
    def cookstyle(self):
        print('加两斤的鸡，20g的盐,3斤水，熬成一锅')


class Student(ChickenSoup):
    '''爷爷的徒弟'''
    pass



class NewEast(object):
    '''新东方技术学院'''
    def eastcook(self):
        print('这是新东方做法')



# 多继承
class Chicken2Soup(NewEast,ChickenSoup):
    '''小明学到的'''
    def cookstyle(self):
        print('加一斤的鸽子，20g的盐,3斤水，熬成一锅')



if __name__ == '__main__':
    xiaoming = Chicken2Soup()
    xiaoming.eastcook()
    print(Chicken2Soup.__mro__)