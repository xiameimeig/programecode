import pygame
import random


class TreeFlagClass(pygame.sprite.Sprite):
    '''这是实现小树和旗帜的类'''
    def __init__(self,image_file,location,type):
        '''

        :param image_file: 这是旗帜或者树木的图片
        :param location: 位置,列表[320,100]
        :param type: 标注是旗帜还是树木
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type


    def update(self):
        global speed
        self.rect.centery -= speed[1]
        if self.rect.centery < 0:
            self.kill()

def create_obstacle():
    '''这个函数用来真正创建小树的旗帜，并且它的大小和我们游戏界面的大小一致，我们设计将
    这个界面分成10份，创建10 个精灵分布在这个界面上，注意一定不能发生精灵重叠的现象，所以创建精灵的时候
    要判断位置，当真正刷新位置的时候，，这个界面整体上移，越过游戏界面顶部的精灵将会删除
    '''
    global group
    location_list = []
    # 创建10个精灵对象
    for i in range(10):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [row * 64+15, col * 64 +30+ 640]
        if location not in location_list:
            # 判断位置是否在位置列表里面，如果不在则创建新的精灵
            location_list.append(location)
            type = random.choice(['tree', 'flag'])
            if type == 'tree':
                image_file = './pic/skier_tree.png'

            elif type == 'flag':
                image_file = './pic/skier_flag.png'

            obj = TreeFlagClass(image_file, location, type)
            group.add(obj)

def draw_win():
    '''绘制屏幕，除去之前的痕迹'''
    global window
    global group
    window.fill([255,255,255])
    group.draw(window)
    pygame.display.flip()



if __name__ == '__main__':
    # 进行初始化操作：创建新窗口，设置帧
    pygame.init()
    window = pygame.display.set_mode((640, 640))
    window.fill([255, 255, 255])  # rgb 值 白色背景


    # 设置帧,创建了一个时间对象
    clock = pygame.time.Clock()

    position = 0
    # 记录小树所在的那张图的位置

    speed = [0, 2]
    # 设置速度，这是一个全局变量


    # 创建一个组对象
    group = pygame.sprite.Group()

    create_obstacle()
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('关闭窗口')
                exit()


        position += speed[1]
        # 标注小树以及旗帜的位置，随着循环，跟着小树的位置变化而变化
        if position >= 640:
            create_obstacle()
            position = 0
        group.update()
        draw_win()
        pygame.display.update()