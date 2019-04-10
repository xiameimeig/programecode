'''继承'''
class ChickenSoup(object):
    '''祖传的，秘方,爷爷留下来的'''
    def __init__(self):
        self.name = '飘香鸡秘方'

    def cookstyle(self):
        print('加两斤的鸡，20g的盐,3斤水，熬成一锅')

class NewEast(object):
    '''新东方技术学院'''
    def __int__(self):
        self.__cake = '飘香蛋糕'
    def eastcook(self):
        print('这是新东方做蛋糕')


# 多继承
class Chicken2Soup(NewEast,ChickenSoup):
    '''小明学到的'''
    def cookstyle(self):
        '''在爷爷的基础上，加以改进'''
        super(Chicken2Soup, self).cookstyle()





if __name__ == '__main__':
    xiaoming = Chicken2Soup()
    xiaoming.cookstyle()