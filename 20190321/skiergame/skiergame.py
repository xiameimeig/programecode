import pygame
import random
pygame.init()

window = pygame.display.set_mode((640,600))
window.fill([255, 255, 255]) # rgb 值

skier_images = ["./pic/skier_down.png", "./pic/skier_right1.png", "./pic/skier_right2.png","./pic/skier_left2.png", "./pic/skier_left1.png"]

class SkierClass(pygame.sprite.Sprite):
    '''实现精灵类的继承，完成滑雪小人的写成'''
    def __init__(self):
        '''
        :param image: 指的是图片的路径
        :param location: 列表类型的属性，[x横轴坐标，y纵轴坐标]
        :param speed: 列表类型，[横轴的速度,纵轴的速度]
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./pic/skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    def move(self):
        '''这个方法实现了小人的移动，利用的是rect内置的move方法'''
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 20:  self.rect.centerx = 20
        if self.rect.centerx > 620: self.rect.centerx = 620

    def turn(self,direction):
        self.angle = self.angle + direction
        if self.angle < -2:  self.angle = -2
        if self.angle > 2:  self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
        return speed

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
        self.passed = False



    def update(self):
        global speed
        self.rect.centery -= speed[1]
        if self.rect.centery < 0:
            self.kill()



def create_obstacle():
    '''这个函数用来真正创建小树和旗帜，并且它的大小和我们游戏界面的大小一致，我们设计将
    这个界面分成10份，创建10 个精灵分布在这个界面上，注意一定不能发生精灵重叠的现象，所以创建精灵的时候
    要判断位置，当真正刷新位置的时候，，这个界面整体上移，越过游戏界面顶部的精灵将会删除
    '''
    global group
    location_list = []
    # 创建10个精灵对象
    for i in range(10):
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        location = [row * 64+15, col * 64 +30+640]
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
    window.blit(skier.image, skier.rect)  # 将小人图像添加到窗口显示
    window.blit(text_obj ,[10,100])
    pygame.display.flip()

if __name__ == '__main__':

    # 创建单个小人实例

    skier = SkierClass()
    # 设置帧,创建了一个时间对象，替代了延迟操作
    clock = pygame.time.Clock()

    position = 0
    # 记录小树所在的那张图的位置

    speed = [0, 2]
    # 设置速度，这是一个全局变量

    # 创建一个组对象
    group = pygame.sprite.Group()
    # 设置一个字体对象
    font = pygame.font.Font(None,80)

    score = 0
    create_obstacle()
    while True:
        clock.tick(50)
        for event in pygame.event.get():
            # 这个for循环检测的是时间
            if event.type == pygame.QUIT:
                # 这个语句检测的是是否点击x按键关闭
                # print('关闭窗口')
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed = skier.turn(-1)
                elif event.key == pygame.K_RIGHT:
                    speed = skier.turn(1)



        window.fill([255,255,255]) #创建一个新背景，掩饰之前出现的遗留图像的问题
        skier.move()


        position += speed[1]
        # 标注小树以及旗帜的位置，随着循环，跟着小树的位置变化而变化
        if position >= 640:
            create_obstacle()
            position = 0

        # 调用函数，绘制图片
        group.update()

        return_list = pygame.sprite.spritecollide(skier,group,False)
        print(return_list)
        if return_list:
            # print('发生碰撞')
            if return_list[0].type == 'tree' and return_list[0].passed==False:
                print('碰到树')
                score = score - 100
                skier.image = pygame.image.load('./pic/skier_crash.png')
                draw_win()
                pygame.time.delay(1000)
                skier.image = pygame.image.load(skier_images[0])
                return_list[0].passed = True
            elif return_list[0].type == 'flag':
                print('碰到旗帜')
                pass
        # 设置需要展示的内容和以及字体的色彩
        text_obj = font.render('score:'+str(score),True,(0,0,0))
        draw_win()
        pygame.display.update()
        # pip install -i https://pypi.doubanio.com/simple pyinstaller