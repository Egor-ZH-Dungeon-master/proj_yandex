import pygame
import random


pygame.init()
# размеры игры
WIDTH = 1000
HEIGHT = 750

# ограничение кадров
fps = 60
clock = pygame.time.Clock()

# создание дисплея
display = pygame.display.set_mode((WIDTH, HEIGHT))

# название игры
pygame.display.set_caption("Лягуха прыгуха :)")

# иконка игры
ikonka = pygame.image.load("data/lyag.png")
pygame.display.set_icon(ikonka)

cac_im = [pygame.image.load("data/Cactus0.png"), pygame.image.load("data/Cactus1.png"),
          pygame.image.load("data/Cactus2.png")]
cac_opt = [69, 573, 37, 534, 40, 544]

pers_im = [pygame.image.load("data/lyag2.png"), pygame.image.load("data/lyag1.png"),
           pygame.image.load("data/lyag0.png")]
im_counter = 0

stone_im = [pygame.image.load("data/Stone0.png"), pygame.image.load("data/Stone1.png")]


cloud_im = [pygame.image.load("data/Cloud0.png"), pygame.image.load("data/Cloud1.png")]




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



user_WIDTH = 50
user_HEIGHT = 50

# положение персонажа
user_x = WIDTH // 4
user_y = HEIGHT - user_HEIGHT - 126

m_jump = False
c_jump = 30

# размеры препятствия
cac_WIDTH = 20
cac_HEIGHT = 80

# положение препятствия
cac_x = WIDTH - 40
cac_y = HEIGHT - cac_HEIGHT - 80




def game_1():
    global m_jump
    game = True
    cac_array = []
    create_cac_arr(cac_array)
    land = pygame.image.load("data/Land.png")

    stone, cloud = open_r()

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            m_jump = True

        if m_jump:
            jump()

        display.blit(land, (0, 0))
        draw_array(cac_array)
        move_ob(stone, cloud)

        d_lyag()

        pygame.display.update()
        clock.tick(fps)


def jump():
    global user_y, m_jump, c_jump
    if c_jump >= -30:
        user_y -= c_jump / 2.5
        c_jump -= 1
    else:
        c_jump = 30
        m_jump = False


def create_cac_arr(array):
    choice = random.randrange(0, 3)
    image = cac_im[choice]
    width = cac_opt[choice * 2]
    height = cac_opt[choice * 2 + 1]
    array.append(Object(WIDTH + 50, height, width, image, 4))

    choice = random.randrange(0, 3)
    image = cac_im[choice]
    width = cac_opt[choice * 2]
    height = cac_opt[choice * 2 + 1]
    array.append(Object(WIDTH + 300, height, width, image, 4))

    choice = random.randrange(0, 3)
    image = cac_im[choice]
    width = cac_opt[choice * 2]
    height = cac_opt[choice * 2 + 1]
    array.append(Object(WIDTH + 600, height, width, image, 4))


def find_rad(array):
    maximum = max(array[0].x, array[1].x, array[2].x)
    if maximum < WIDTH:
        rad = WIDTH
        if rad - maximum < 50:
            rad += 150
    else:
        rad = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        rad += random.randrange(10, 15)
    else:
        rad += random.randrange(200, 350)

    return rad


def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            rad = find_rad(array)
            choice = random.randrange(0, 3)
            image = cac_im[choice]
            width = cac_opt[choice * 2]
            height = cac_opt[choice * 2 + 1]

            cactus.ret_self(rad, height, width, image)


def open_r():
    choice = random.randrange(0, 2)
    im_s = stone_im[choice]

    choice = random.randrange(0, 2)
    im_c = cloud_im[choice]

    stone = Object(WIDTH, HEIGHT - 80, 10, im_s, 5)
    cloud = Object(WIDTH, 80, 73, im_c, 3)

    return cloud, stone

def move_ob(stone, cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0, 2)
        im_s = stone_im[choice]
        stone.ret_self(WIDTH, 700 + random.randrange(10, 60), stone.width, im_s)

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        im_c = cloud_im[choice]
        cloud.ret_self(WIDTH, random.randrange(10, 200), cloud.width, im_c)


def d_lyag():
    global im_counter
    if im_counter == 18:
        im_counter = 0

    display.blit(pers_im[im_counter // 6], (user_x, user_y))
    im_counter += 1











def check_colid(barier):
    pass


game_1()
