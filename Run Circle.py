import pygame

WIDTH = 400
HEIGHT = 400
FPS = 60

WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
PINK = (250, 218, 221)

r = 20
x = 200
y = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

screen.fill(WHITE)
pygame.draw.circle(screen, ORANGE, (x, y), r)
pygame.display.update()

motion = 'Stop'

pygame.init()
running = True
while running:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                motion = 'Left'
            elif i.key == pygame.K_d:
                motion = 'Right'
            elif i.key == pygame.K_s:
                motion = 'Down'
            elif i.key == pygame.K_w:
                motion = 'Up'
        if i.type == pygame.KEYUP:
            if i.key in [pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w]:
                motion = 'Stop'
    if x >= 380 and motion == 'Right' or x <= 20 and motion == 'Left' or y >= 380 and motion == 'Down' or y <= 20 and motion == 'Up':
        motion = 'Stop'
    else:
        if motion == 'Left':
            x -= 2
        elif motion == 'Right':
            x += 2
        elif motion == 'Down':
            y += 2
        elif motion == 'Up':
            y -= 2

    screen.fill(WHITE)
    pygame.draw.circle(screen, ORANGE, (x, y), r)
    pygame.display.update()
    keys = pygame.key.get_pressed()

    clock.tick(FPS)
pygame.quit()
