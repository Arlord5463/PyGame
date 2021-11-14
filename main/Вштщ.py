import pygame
pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

hero_y = HEIGHT * 2 / 3 - 74
jump_counter = 30

# Основа
running = True
while running:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False
    # Jump
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                while jump_counter >= -30:
                    hero_y -= jump_counter / 3
                    jump_counter -= 1
                jump_counter = 30

    # Hero
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    hero = pygame.Rect(35, hero_y, 65, 90)

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0, HEIGHT * 2 / 3], [WIDTH, HEIGHT * 2 / 3])
    pygame.draw.rect(screen, YELLOW, hero)

    pygame.display.update()
pygame.quit()
