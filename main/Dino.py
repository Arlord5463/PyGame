import pygame

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400
FPS = 60

# Hero
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
hero_y = 0
hero = pygame.Rect(35, hero_y, 95, 95)
hero_img = pygame.image.load('hero.png')
hero_img = pygame.transform.scale(hero_img, (95, 95))

# Кактусы
kaktus_img = pygame.image.load('KAKTUS-removebg-preview.png')
kaktus_img = pygame.transform.scale(kaktus_img, (75, 75))
kaktus = kaktus_img.get_rect()

# Пол
flour = pygame.Rect(0, HEIGHT * 2 / 3 - 74 + 85, WIDTH, 1)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

# Основа
running = True
isJump = False
count_of_jumps = 0
GRAVITY = 0.1
jump = 0.05
while running:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False

        # Прыжок
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if pygame.Rect.colliderect(hero, flour):
                    jump = 1.25
                    isJump = True
                    count_of_jumps = 0

    # Падение
    if not pygame.Rect.colliderect(hero, flour) and not isJump:
        hero.top += jump
        jump += GRAVITY
    elif isJump:
        hero.top += jump
        jump -= GRAVITY
        count_of_jumps += 1
        if count_of_jumps == 40:
            isJump = False

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, flour)
    screen.blit(hero_img, (hero.left, hero.top))

    pygame.display.update()
pygame.quit()
