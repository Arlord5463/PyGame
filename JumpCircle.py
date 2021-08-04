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
y = 380

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

screen.fill(WHITE)
pygame.draw.circle(screen, ORANGE, (x, y), r)
pygame.display.update()

make_jump = False
jump_counter = 30

pygame.init()
running = True

while running:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        make_jump = True

    if make_jump:
        if jump_counter >= -30:
            y -= jump_counter / 3
            jump_counter -= 1
        else:
            jump_counter = 30
            make_jump = False    

    screen.fill(WHITE)
    pygame.draw.circle(screen, ORANGE, (x, y), r)
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
