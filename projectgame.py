import pygame
import random
import os



pygame.init()
# размеры игры
WIDTH = 1000
HEIGHT = 750

# ограничение кадров
fps = 100
clock = pygame.time.Clock()

# создание дисплея
display = pygame.display.set_mode((WIDTH, HEIGHT))

# название игры
pygame.display.set_caption("Лягуха прыгуха :)")
pygame.mixer.music.load('data/fonpesn.mp3')
pygame.mixer.music.set_volume(0.3)
jumpzv = pygame.mixer.Sound('data/prig.wav')
prizemzv = pygame.mixer.Sound('data/priz.wav')
poterserd = pygame.mixer.Sound('data/serdmin.wav')
proigral = pygame.mixer.Sound('data/proigral.wav')

# иконка игры
ikonka = pygame.image.load("data/lyag0.png")
pygame.display.set_icon(ikonka)
# кактусы
cac_im = [pygame.image.load("data/Cactus0.png"), pygame.image.load("data/Cactus1.png"),
          pygame.image.load("data/Cactus2.png")]
cac_opt = [69, 573, 37, 534, 40, 544]

# определение персонажа
pers_im = [pygame.image.load("data/lyag2.png"), pygame.image.load("data/lyag1.png"),
           pygame.image.load("data/lyag0.png")]
im_counter = 0

stone_im = [pygame.image.load("data/Stone0.png"), pygame.image.load("data/Stone1.png")]

# облака
cloud_im = [pygame.image.load("data/Cloud0.png"), pygame.image.load("data/Cloud1.png")]

scores = 0
max_score = 0
max_cact = 0
nad_cactus = False
health = 3
health_im = pygame.image.load('data/serd.png')
health_im = pygame.transform.scale(health_im, (30, 30))




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

# сам игровой цикл
def game_1():
    global m_jump
    pygame.mixer.music.play(-1)
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

        if keys[pygame.K_ESCAPE] or keys[pygame.K_PAUSE]:
            pause()

        if m_jump:
            jump()

        if check_colid(cac_array):
            game = False

        count_sc(cac_array)

        display.blit(land, (0, 0))
        p_text("Score: " + str(scores), 800, 10)
        show_health()


        draw_array(cac_array)
        move_ob(stone, cloud)

        d_lyag()

        pygame.display.update()
        clock.tick(fps)
    return u_game_over()


def jump():
    global user_y, m_jump, c_jump
    if c_jump >= -30:
        if c_jump == 30:
            pygame.mixer.Sound.play(jumpzv)
        if c_jump == -30:
            pygame.mixer.Sound.play(prizemzv)
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
            rad += 250
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

def obj_return(objects, obj):
    rad = find_rad(objects)
    choice = random.randrange(0, 3)
    image = cac_im[choice]
    width = cac_opt[choice * 2]
    height = cac_opt[choice * 2 + 1]

    obj.ret_self(rad, height, width, image)
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


def p_text(soobsh, x, y, sh_color=(0, 250, 0), sh_type="data/shrift.ttf", sh_size=35):
    sh_type = pygame.font.Font(sh_type, sh_size)
    text = sh_type.render(soobsh, True, sh_color)
    display.blit(text, (x, y))


def pause():
    paused = True
    pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        p_text("ИГРА ОСТАНОВЛЕНА, ЧТОБЫ ПРОДОЛЖИТЬ НАЖМИ НА ENTER", 50, 300)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(20)
    pygame.mixer.music.unpause()


def check_colid(bariers):
    for barier in bariers:
        if barier.y == 449:
            if not m_jump:
                if barier.x <= user_x + user_WIDTH - 35 <= barier.x + barier.width:
                    if check_h():
                        obj_return(bariers, barier)
                        return False
                    else:
                        return True
            elif c_jump >= 0:
                if user_y + user_HEIGHT - 5 >= barier.y:
                    if barier.x <= user_x + user_WIDTH - 40 <= barier.x + barier.width:
                        if check_h():
                            obj_return(bariers, barier)
                            return False
                        else:
                            return True
            else:
                if user_y + user_HEIGHT - 10 >= barier.y:
                    if check_h():
                        obj_return(bariers, barier)
                        return False
                    else:
                        return True
        else:
            if not m_jump:
                if barier.x <= user_x + user_WIDTH - 5 <= barier.x + barier.width:
                    if check_h():
                        obj_return(bariers, barier)
                        return False
                    else:
                        return True
            elif c_jump == 10:
                if user_y + user_HEIGHT - 5 >= barier.y:
                    if barier.x <= user_x + user_WIDTH - 5 <= barier.x + barier.width:
                        if check_h():
                            obj_return(bariers, barier)
                            return False
                        else:
                            return True
            elif c_jump >= 1:
                if user_y + user_HEIGHT - 5 >= barier.y:
                    if barier.x <= user_x + user_WIDTH - 35 <= barier.x + barier.width:
                        if check_h():
                            obj_return(bariers, barier)
                            return False
                        else:
                            return True
                else:
                    if user_y + user_HEIGHT - 10 >= barier.y:
                        if barier.x <= user_x + 5 <= barier.x + barier.width:
                            if check_h():
                                obj_return(bariers, barier)
                                return False
                            else:
                                return True


def count_sc(bar):
    global scores, max_cact, max_score
    nad_cactus = 0


    if -20 <= c_jump < 25:
        for barr in bar:
            if user_y + user_HEIGHT - 5 <= barr.y:
                if barr.x <= user_x <= barr.x + barr.width:
                    nad_cactus += 1
                elif barr.x <= user_x + user_WIDTH <= barr.x + barr.width:
                    nad_cactus += 1

        max_cact = max(max_cact, nad_cactus)
    else:
        if c_jump == -30:
            scores += max_cact
            max_cact = 0

def u_game_over():
    global scores, max_score
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event. type == pygame.QUIT:
                pygame.quit()
                quit()
        if scores > max_score:
            max_score = scores
            p_text("Новый рекорд! Score: " + str(max_score), 300, 200)
            p_text("ТЫ ПРОИГРАЛ, НИКЧЁМНЫЙ ЛЮДИШКА, Я НЕ УДИВЛЁН", 150, 300)
        p_text("ТЫ ПРОИГРАЛ, НИКЧЁМНЫЙ ЛЮДИШКА, Я НЕ УДИВЛЁН", 150, 300)



        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            return True

        if keys[pygame.K_ESCAPE]:
            return False

        pygame.display.update()
        clock.tick(60)


def show_health():
    global health
    health1 = 0
    x = 20
    while health1 != health:
        display.blit(health_im, (x, 20))
        x += 40
        health1 += 1


def check_h():
    global health
    health -= 1
    if health == 0:
        pygame.mixer.Sound.play(proigral)
        return False
    else:
        pygame.mixer.Sound.play(poterserd)
        return True




while game_1():
    scores = 0
    m_jump = False
    c_jump = 30
    user_y = HEIGHT - user_HEIGHT - 126
    health = 3

pygame.quit()
quit()
