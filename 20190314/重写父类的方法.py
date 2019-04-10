'''继承'''
class ChickenSoup(object):
    '''祖传的，秘方,爷爷留下来的'''
    def __init__(self):
        self.name = '飘香鸡秘方'

    def cookstyle(self):
        '''爷爷鸡汤的做法'''
        print('##########此处致敬爷爷的鸡汤############')
        print('加两斤的鸡，20g的盐,3斤水，熬成一锅')


# 多继承
class Chicken2Soup(ChickenSoup):
    '''小明学到的'''
    def cookstyle(self):
        # print('加两斤的鸡，20g的盐,3斤水，熬成一锅,再加50g糖')
        super(Chicken2Soup, self).cookstyle()
        super().cookstyle()
        ChickenSoup().cookstyle()
        print('哈啊啊啊啊啊啊啊，这是我自己的秘方')
    def newcook(self):
        super(Chicken2Soup, self).cookstyle()



if __name__ == '__main__':
    xiaoming = Chicken2Soup()
    # xiaoming.cookstyle()
    xiaoming.newcook()
    print(Chicken2Soup.__mro__)