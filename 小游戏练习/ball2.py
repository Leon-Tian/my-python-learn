# 目标： 自由落体小球

import pygame

# 1. 画个框

# 初始化导入的pygame中的模块
pygame.init()
# 初始化用于显示的窗口并设置窗口尺寸
screen = pygame.display.set_mode((800, 600))
# 设置当前窗口的标题
pygame.display.set_caption('小球移动')

r = 50
x = 400
y = 100
sx = 20
sy = 0

# 3. 监听“键盘”，移动
running = True
while running:
    screen.fill((255, 255, 255))
    
    y = y - sy
    if y > 600 - r:
        y = 600 - r
        sy = - int (sy * 0.9)

    sy = sy - 10

    # 2. 画个球
    color = (0, 255, 255)
    pygame.draw.circle(screen, color, (x, y), r, 0)

    # 刷新
    pygame.display.flip()
    pygame.time.delay(50)