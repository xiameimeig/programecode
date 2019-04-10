import pygame
pygame.init()
skier_images = ['./skier_crash.png','./pic/skier_down.png','./skier_left1.png','./skier_left2.png','./skier_right1.png','./skier_right2.png']


window = pygame.display.set_mode((640,600))
window.fill([255, 255, 255])


pygame.display.set_caption('cool')
# image = pygame.image.load('skierGame.jpeg').convert()

skier = pygame.image.load(skier_images[1]).convert()


# pygame.display.set_icon()
while True:
    # window.blit(image,(0,0))



    window.blit(skier,(320-15,20))

    ret = pygame.event.get()
    x = 305
    y = 20
    # pygame.key.get_pressed()
    for obj in ret:
        if obj.type == pygame.QUIT:
            print('关闭窗口')
            exit()

        elif obj.type == pygame.KEYDOWN:
            # print('此时有键盘操作')
            # print('此时按下的键是',obj.key)
            if obj.key == pygame.K_DOWN or obj.key == pygame.K_s:
                print('此时按了向下的键')
                y = y +1
            elif obj.key == pygame.K_LEFT or obj.key == pygame.K_a:
                print('left')
                x = x-1


            elif obj.key == pygame.K_RIGHT or obj.key == pygame.K_d:
                print('right')
                x = x+1

    pygame.display.update()