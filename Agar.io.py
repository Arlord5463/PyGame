import pygame
import random

WIDTH = 400
HEIGHT = 400
FPS = 60

WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
PINK = (250, 218, 221)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

x = WIDTH / 2
y = HEIGHT / 2
size = 40
hero = pygame.Rect(x, y, size, size)
hero_img = pygame.image.load('Hero.png')
hero_img = pygame.transform.scale(hero_img, (40, 40))

food_size = 20
foods = [pygame.Rect(random.randint(0, WIDTH - food_size), random.randint(0, HEIGHT - food_size), food_size, food_size)
         for i in range(20)]
food_img = pygame.image.load('Food.png')
food_img = pygame.transform.scale(food_img, (20, 20))
food_counter = 0
new_food = 30

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

    if motion == 'Left' and hero.left > 0:
        hero.left -= 2
    elif motion == 'Right' and hero.right < WIDTH:
        hero.left += 2
    elif motion == 'Down' and hero.bottom < HEIGHT:
        hero.top += 2
    elif motion == 'Up' and hero.top > 0:
        hero.bottom -= 2

    food_counter += 1
    if food_counter >= new_food:
        foods.append(pygame.Rect(random.randint(0, WIDTH - food_size), random.randint(0, HEIGHT - food_size), food_size, food_size))
        food_counter = 0

    for food in foods:
        if hero.colliderect(food):
            foods.remove(food)
            hero.width += 1
            hero.height += 1
            hero_img = pygame.transform.scale(hero_img, (hero_img.get_width() + 1, hero_img.get_height() + 1))

    screen.fill(WHITE)
    for food in foods:
        screen.blit(food_img, (food.left, food.top))
    screen.blit(hero_img, (hero.left, hero.top))
    pygame.display.update()

    clock.tick(FPS)
pygame.quit()
