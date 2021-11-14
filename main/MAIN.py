import pygame
pygame.init()

WIDTH = 600
HEIGHT = 400
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



running = True
while running:
    screen.fill(WHITE)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if 200 < i.pos[0] < 400 and 165 < i.pos[1] < 165+70:
                    print('done')

    pygame.draw.rect(screen, (0, 255, 0), (200, 165, 200, 70))

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
