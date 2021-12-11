import pygame
import time
pygame.init()

# Screen
WIDTH = 1200
HEIGHT = 800
FPS = 60

# Hero
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
hero_y = 0
hero = pygame.Rect(35, hero_y, 95, 95)
hero_img = pygame.image.load('hero.png')
hero_img = pygame.transform.scale(hero_img, (95, 95))

# Пол
flour = pygame.Rect(0, HEIGHT * 2 / 3 + 11, WIDTH, 1)

# Кактусы
kaktus_img = pygame.image.load('KAKTUS-removebg-preview.png')
kaktus_img = pygame.transform.scale(kaktus_img, (75, 75))
list_of_kaktus = []
kaktus_CD = 600
current_time = 0
last_time = 0

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
isStay = False
count_of_jumps = 0
GRAVITY = 0.3
jump = 0.05
while running:
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False

        # Прыжок
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if not isJump and isStay:
                    jump = 1.25
                    isJump = True
                    isStay = False
                    count_of_jumps = 0

    # Падение
    if not isStay and not isJump:
        hero.top += jump
        jump += GRAVITY
        if hero.colliderect(flour):
            isStay = True
    elif isJump:
        hero.top += jump
        jump -= GRAVITY
        count_of_jumps += 1
        if count_of_jumps == 40:
            isJump = False

    current_time += 1
    if current_time - last_time >= kaktus_CD:
        kaktus = kaktus_img.get_rect()
        kaktus.top = flour.top - kaktus.height
        kaktus.left = WIDTH
        list_of_kaktus.append(kaktus)
        last_time = current_time

    for kaktus_i in list_of_kaktus:
        if hero.colliderect(kaktus_i):
            running = False

    for kaktus_i in list_of_kaktus:
        if kaktus_i.right < 0:
            list_of_kaktus.remove(kaktus_i)

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, flour)
    screen.blit(hero_img, (hero.left, hero.top))

    for kaktus_i in list_of_kaktus:
        pygame.draw.rect(screen, LIGHT_BLUE, kaktus_i)
        screen.blit(kaktus_img, (kaktus_i.left, kaktus_i.top))
        kaktus_i.left -= 5

    pygame.display.update()
pygame.quit()
