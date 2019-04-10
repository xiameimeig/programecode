'''实现一个烧烤类'''
# 烧烤：
# 属性：生熟程度、调料[孜然，盐，辣椒粉，油]
# 方法：烤、加料


class Bbq(object):
    '''这是实现烧烤类'''
    def __init__(self,level):
        self.level = level # 这是生熟程度
        self.flavour = [] # 这是调料
        self.levelstring = '生' # 字符串类型，描述烧烤的生熟程度

    def kao(self,time):
        '''这是实现烤的过程,时间由用户决定'''
        self.level += time
        self.levelstring = '%d成熟'%self.level
        if self.level >10:
            self.levelstring = '碳化'

    def add(self,fla):
        '''增加调料'''
        self.flavour.append(fla)


    def __str__(self):
        # return self.levelstring
        str1 = ''
        for i in self.flavour:
            str1 += i+', '

        str1 = str1.strip(', ')
        return '生熟的程度:%s,调料是:%s'%(self.levelstring,str1)


if __name__ == '__main__':
    obj1 = Bbq(0)
    print(obj1)
    print('##################################')

    obj1.add('孜然')
    print(obj1)
    print('##################################')

    obj1.add('辣椒')
    print(obj1)
    print('##################################')


    obj1.kao(10)
    print(obj1)
    print('##################################')