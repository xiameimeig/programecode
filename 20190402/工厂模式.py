# class Car(object):
#     def move(self):
#         print('车会跑')

class BmwX1(object):
    def __init__(self):
        self.price = 20
    def move(self):
            print('X1车会跑')

class Bmw730(object):
    def __init__(self):
        self.price = 100
    def move(self):
            print('730车会跑')


# 定义一个函数，用来模拟汽车工厂，判断车型，按照车型的不同返回不同的车辆实例
def createcar(type):
    '''这个函数相当于一个中间商'''
    if type == 'x1':
        carx1 = BmwX1()
        return carx1
    elif type == '730':
        car730 = Bmw730()
        return car730

class CarShop(object):
    '''BMW4S店'''
    def sale(self,type):
        car = createcar(type)
        return car

# 首先创建一个店面，用来销售车辆
shop = CarShop()
# 销售车辆
car_costumer = shop.sale('x1')
car_costumer.move()