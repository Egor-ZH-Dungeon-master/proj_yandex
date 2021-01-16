import pygame
from pygame import *
import sys
import os

WIDTH = 1000
HEIGHT = 700
DISPLAY = (WIDTH, HEIGHT)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


FPS = 60


PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Good COCK")
clock = pygame.time.Clock()

screen.fill(BLACK)
pygame.display.flip()

level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-                       -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------        -",
       "-                       -",
       "-                -      -",
       "-                   --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]

x = y = 0  # координаты
for row in level:  # вся строка
    for col in row:  # каждый символ
        if col == "-":
            # создаем блок, заливаем его цветом и рисеум его
            pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
            pf.fill(WHITE)
            screen.blit(pf, (x, y))
            display.update()

        x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
    y += PLATFORM_HEIGHT  # то же самое и с высотой
    x = 0  # на каждой новой строчке начинаем с нуля




running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()