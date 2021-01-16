import pygame
from pygame import *
import sys
import os

WIDTH = 992
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
pygame.display.set_caption("Good")
clock = pygame.time.Clock()

screen.fill(BLACK)
pygame.display.flip()

level = [
       "-------------------------------",
       "-                             -",
       "-                             -",
       "-                ----         -",
       "-            --               -",
       "-                             -",
       "--    --                      -",
       "-                             -",
       "-                   ---       -",
       "-                             -",
       "-                             -",
       "-      ---                    -",
       "-                             -",
       "-   -----------               -",
       "-                             -",
       "-                -            -",
       "-                   --        -",
       "-                             -",
       "-                             -",
       "-    ---                      -",
       "-                             -",
       "-------------------------------"]

x = y = 0
for row in level:
    for col in row:
        if col == "-":
            pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
            pf.fill(WHITE)
            screen.blit(pf, (x, y))
            display.update()

        x += PLATFORM_WIDTH
    y += PLATFORM_HEIGHT
    x = 0

MOVE_SPEED = 7
WIDTH_P = 22
HEIGHT_P = 32

left = right = False

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH_P, HEIGHT_P))
        self.image.fill(BLUE)

        self.rect = Rect(x, y, WIDTH_P, HEIGHT_P)

    def update(self, left, right):
        if left:
            self.xvel = -MOVE_SPEED

        if right:
            self.xvel = MOVE_SPEED

        if not (left or right):
            self.xvel = 0

        self.rect.x += self.xvel

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

hero = Player(55, 55)



running = True
while running:
    clock.tick(FPS)
    x = y = 0
    hero.draw(screen)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_LEFT:
            left = True
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            right = True

        elif event.type == KEYUP and event.key == K_RIGHT:
            right = False
        elif event.type == KEYUP and event.key == K_LEFT:
            left = False
    hero.update(left, right)
    display.update()

pygame.quit()