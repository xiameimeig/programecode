import pygame


skier_images = ["./pic/skier_down.png", "./pic/skier_right1.png", "./pic/skier_right2.png","./pic/skier_left2.png", "./pic/skier_left1.png"]


class SkierClass(pygame.sprite.Sprite):
    '''实现精灵类的继承，完成滑雪小人的写成'''
    def __init__(self,image,speed):
        '''
        :param image: 指的是图片的路径
        :param speed: 列表类型，[横轴的速度,纵轴的速度]
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image) #<Surface(30x64x32 SW)>，加载雪人的状态图像
        self.rect = self.image.get_rect() #<rect(0, 0, 30, 64)> # 获取图像边界的矩形
        # 设置小人儿的初始位置
        self.rect.center = [320,150]
        self.speed = speed

    def move(self):
        '''这个方法实现了小人的移动，利用的是rect内置的move方法'''
        # retdata = self.rect.move(self.speed)
        # print('move方法的返回值',retdata)
        # self.rect = retdata
        # if self.rect.left < 0 or self.rect.right > 640:
        #     self.speed[0] = -self.speed[0]
        # if self.rect.top < 0 or self.rect.bottom >600:
        #     self.speed[1] = -self.speed[1]
        # self.rect.centerx = self.rect.centerx + 1
        pass



    def turn(self,status):
        '''这个方法实现的是小人的转向问题
        左转两个状态，主要是转向的幅度不同
        右转一样
        status: 代表的是用户的输入状态
        '''
        if status == 0:
            self.image = pygame.image.load(skier_images[status])
        elif status == 1:
            self.image = pygame.image.load(skier_images[status])
        elif status == 3:
            self.image = pygame.image.load(skier_images[status])



pygame.sprite.spritecollide()


if __name__ == '__main__':
    # 进行初始化操作：创建新窗口，设置帧
    pygame.init()
    window = pygame.display.set_mode((640, 640))
    window.fill([255, 255, 255])  # rgb 值 白色背景

    # 设置帧,创建了一个时间对象
    clock = pygame.time.Clock()

    ski = SkierClass(skier_images[0],[0,1])
    window.blit(ski.image,ski.rect)
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('关闭窗口')
                exit()

            if event.type == pygame.KEYDOWN:
                '''判断用户是否在键盘有时间输入'''
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    print('按下的是向下的键')
                    ski.turn(0)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    print('按下向左的键')
                    ski.turn(3)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    print('按下向右的键')
                    ski.turn(1)
                    print(ski.image)
        ski.move()


        window.fill([255,255,255])
        window.blit(ski.image, ski.rect)
        pygame.display.flip()
        # 这三句话非常重要，绘制新的屏幕，展示图像的新位置

        pygame.display.update()
