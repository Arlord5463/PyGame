import pygame
import random
import time

# Настройки окна
WIDTH = 500
HEIGHT = 500
FPS = 60

# Настройки цвета
BLACK = (0, 0, 0)

# Инициализация
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Персонаж
x, y = WIDTH / 2, HEIGHT / 2
hero = pygame.Rect(x, y, 60, 50)
heroImg = pygame.image.load('razorinv.png')

# Время
last_time = 0
current_time = 0

# Противники
enemies = []
enemyCd = 5
enemy_img = pygame.image.load('invaderinv.png')
enemy_rect = enemy_img.get_rect()
enemy_width = enemy_rect.width
enemy_height = enemy_rect.height

# Пули
bullet_width = 2
bullet_height = 5
bullet_img = pygame.image.load('bullet.png')
bullets = []
isShot = False

motion = 'Stop'

pygame.init()
running = True
while running:
    screen.fill(BLACK)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                motion = 'Left'
            if i.key == pygame.K_d:
                motion = 'Right'
            if i.key == pygame.K_s:
                motion = 'Down'
            if i.key == pygame.K_w:
                motion = 'Up'
            if i.key == pygame.K_SPACE:
                isShot = True
        if i.type == pygame.KEYUP:
            if i.key in [pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w]:
                motion = 'Stop'
    # Передвижение персонажа
    if motion == 'Left' and hero.left > 0:
        hero.left -= 5
    if motion == 'Right' and hero.right < WIDTH:
        hero.left += 5
    if motion == 'Down' and hero.bottom < HEIGHT:
        hero.bottom += 5
    if motion == 'Up' and hero.top > 0:
        hero.bottom -= 5

# ПРОТИВНИКИ
    # Создание противников
    current_time = pygame.time.get_ticks()
    if current_time - last_time > enemyCd:
        x_enemy = random.randint(0, WIDTH-enemy_width)
        enemies.append(pygame.Rect(x_enemy, -enemy_height, enemy_width, enemy_height))
        last_time = current_time
        enemyCd = random.randint(100, 5000)
    # Отрисовка противников
    for enemy in enemies:
        screen.blit(enemy_img, (enemy.left, enemy.top))
        enemy.top += 2

    # Удаление противников
    for enemy in enemies:
        if enemy.top > HEIGHT:
            enemies.remove(enemy)

# ПУЛИ
    # Создание пуль
    if isShot:
        bullet_rect = pygame.Rect(hero.left + 33, hero.top + 5, bullet_width, bullet_height)
        bullets.append(bullet_rect)
        isShot = False

    # Отрисовка пуль
    for bullet in bullets:
        screen.blit(bullet_img, (bullet.left, bullet.top))
        bullet.top -= 5

    # Удаление пуль
    for bullet in bullets:
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Пришельцы уничтожают экипаж, Плохая концовка.
        if hero.colliderect(enemy):
            time.sleep(0.5)
            running = False
            print('Game Over')
    # Уничтожение пришельца
    for enemy in enemies:
        for bullet in bullets:
            if enemy.colliderect(bullet):
                bullets.remove(bullet)
                enemies.remove(enemy)

    screen.blit(heroImg, (hero.left, hero.top))
    pygame.display.update()

    clock.tick(FPS)
pygame.quit()
