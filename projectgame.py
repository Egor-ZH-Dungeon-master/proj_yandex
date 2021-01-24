import pygame
import random
import os


pygame.init()

WIDTH = 1000
HEIGHT = 750

fps = 100
clock = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Лягуха прыгуха :)")
pygame.mixer.music.load('data/fonpesn.mp3')
pygame.mixer.music.set_volume(0.3)
jumpzv = pygame.mixer.Sound('data/prig.wav')
prizemzv = pygame.mixer.Sound('data/priz.wav')
poterserd = pygame.mixer.Sound('data/serdmin.wav')
proigral = pygame.mixer.Sound('data/proigral.wav')
plusserd = pygame.mixer.Sound('data/plusserd.wav')
click = pygame.mixer.Sound('data/click.wav')


ikonka = pygame.image.load("data/lyag0.png")
pygame.display.set_icon(ikonka)


cac_im = [pygame.image.load("data/Cactus0.png"), pygame.image.load("data/Cactus1.png"),
          pygame.image.load("data/Cactus2.png")]
cac_opt = [69, 573, 37, 534, 40, 544]


pers_im = [pygame.image.load("data/lyag2.png"), pygame.image.load("data/lyag1.png"),
           pygame.image.load("data/lyag0.png")]
im_counter = 0


stone_im = [pygame.image.load("data/Stone0.png"), pygame.image.load("data/Stone1.png")]


cloud_im = [pygame.image.load("data/Cloud0.png"), pygame.image.load("data/Cloud1.png")]


scores = 0
max_score = 0


max_cact = 0
nad_cactus = False


health = 2
health_im = pygame.image.load('data/serd.png')
health_im = pygame.transform.scale(health_im, (30, 30))


def s_men():
    men_im = pygame.image.load("data/fon.jpg")
    show = True

    start_b = Button(260, 70)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(men_im, (0, 0))
        start_b.draw(350, 400, "ПЕРЕЙТИ В ИГРУ!", s_game, 50)

        pygame.display.update()
        clock.tick(60)


def s_game():
    global scores, m_jump, c_jump, user_y, health
    while game_1():
        scores = 0
        m_jump = False
        c_jump = 30
        user_y = HEIGHT - user_HEIGHT - 126
        health = 2


class Object:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:

            return False

    def ret_self(self, rad, y, width, image):
        self.x = rad
        self.y = y
        self.width = width
        self.image = image

        display.blit(self.image, (self.x, self.y))


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.active_clr = (0, 200, 0)
        self.noactive_clr = (0, 100, 0)

    def draw(self, x, y, message, action=None, fon_size=30):
        mouse = pygame.mouse.get_pos()
        clicknul = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_clr, (x, y, self.width, self.height))
            if clicknul[0] == 1:
                pygame.mixer.Sound.play(click)
                pygame.time.delay(300)
                if action is not None:
                    action()
        else:
            pygame.draw.rect(display, self.noactive_clr, (x, y, self.width, self.height))

        p_text(message, x + 10, x + 60)


user_WIDTH = 70
user_HEIGHT = 60

user_x = WIDTH // 4
user_y = HEIGHT - user_HEIGHT - 126

m_jump = False
c_jump = 30

cac_WIDTH = 25
cac_HEIGHT = 80

cac_x = WIDTH - 40
cac_y = HEIGHT - cac_HEIGHT - 80


def game_1():
    global m_jump
    pygame.mixer.music.play(-1)

    game = True
    cac_array = []
    create_cac_arr(cac_array)
    land = pygame.image.load("data/Land.png")

    stone, cloud = open_r()
    heart = Object(WIDTH, 460, 30, health_im, 4)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            m_jump = True

        if keys[pygame.K_ESCAPE] or keys[pygame.K_PAUSE]:
            pause()

        if m_jump:
            jump()

        if check_colid(cac_array):
            game = False

        count_sc(cac_array)

        display.blit(land, (0, 0))
        p_text("Score: " + str(scores), 800, 10)

        heart.move()
        plus_h(heart)
        show_health()

        draw_array(cac_array)
        move_ob(stone, cloud)

        d_lyag()

        pygame.display.update()
        clock.tick(fps)
    return u_game_over()


