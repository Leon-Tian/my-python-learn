# 一个球，上下左右键控制移动

import pygame

# 1. 画个框

# 初始化导入的pygame中的模块
pygame.init()
# 初始化用于显示的窗口并设置窗口尺寸
screen = pygame.display.set_mode((800, 600))
# 设置当前窗口的标题
pygame.display.set_caption('小球移动')

r = 50
x = 100
y = 100
sx = 20
sy = 20

# 3. 监听“键盘”，移动
running = True
while running:
    screen.fill((255, 255, 255))
    
    # 从消息队列中获取事件并对事件进行处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 处理键盘事件的代码
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - sx
                if x < r:
                    x = r
            elif event.key == pygame.K_RIGHT:
                x = x + sx
                if x > 800 - r:
                    x = 800 - r
            elif event.key == pygame.K_UP:
                y = y - sy
                if y < r:
                    y = r
            elif event.key == pygame.K_DOWN:
                y = y + sy
                if y > 600 - r:
                    y = 600 - r

    # 2. 画个球
    color = (0, 255, 255)
    pygame.draw.circle(screen, color, (x, y), r, 0)

    # 刷新
    pygame.display.flip()
    pygame.time.delay(50)