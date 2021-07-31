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
clock = pygame.time.Clock(60)

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
            if i.key == pygame.K_LEFT:
                motion = 'Left'
            elif i.key == pygame.K_RIGHT:
                motion = 'Right'
            elif i.key == pygame.K_DOWN:
                motion = 'Down'
            elif i.key == pygame.K_UP:
                motion = 'Up'
        if i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
                motion = 'Stop'
    if x >= 420:
        x = -19
    elif x <= -20:
        x = 419
    elif y >= 420:
        y = -19
    elif y <= -20:
        y = 419
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