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

pygame.init()
running = True
while running:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen, ORANGE, (x, y), r)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if x >= WIDTH + r:
        x = -19
    elif x <= 0 - r:
        x = 419
    else:
        if keys[pygame.K_d]:
            x += 2
        elif keys[pygame.K_a]:
            x -= 2

    clock.tick(FPS)
pygame.quit()
