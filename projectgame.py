import os
import sys
import pygame

pygame.init()
size = WIDTH, HEIGHT = 1000, 900
screen = pygame.display.set_mode(size)
FPS = 50
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
perehod = pygame.mixer.Sound('data/perehod.wav')


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Правила игры:",
                  "",
                  "",
                  "",
                  "Вам нужно собирать мух, для перехода на следующий уровень.",
                  "Когда собирете определённое кол-во мух, вас перекидывает на следующий уровень,",
                  "Последний уровень: убить Босса"
                  "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "                                                                                                                           Создатели и помощники:",
                  "                                                                                                                           Артем Степанов",
                  "                                                                                                                           Егор Жижло",
                  "                                                                                                                           Александр Маньшин(Граф.Дизайнер)"]

    fon = pygame.transform.scale(load_image('nach.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 25)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(perehod)

                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением \'{fullname}\' не найден')
        sys.exit()
    image = pygame.image.load(fullname)

    if color_key:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == 'p':
                Tile('muxa', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y


tile_images = {
    'wall': load_image('stena.png'),
    'empty': load_image('pol.png'),
    'muxa': load_image("mukha.png")
}

wall_img = pygame.image.load("data/stena.png")

empty_img = pygame.image.load('data/pol.png')
muxa_img = pygame.image.load('data/mukha.png')

player_image = load_image('heros.png')

tile_width = tile_height = 50


def move_hero(hero, movement):
    x, y = hero.pos

    if movement == "up":
        if y > 0 and level[y - 1][x] == "." or y > 0 and level[y - 1][x] == "p":
            hero.move(x, y - 1)
    elif movement == "down":
        if y < level_y - 1 and level[y + 1][x] == "." or y < level_y - 1 and level[y + 1][x] == "p":
            hero.move(x, y + 1)
    elif movement == "left":
        if x > 0 and level[y][x - 1] == "." or x > 0 and level[y][x - 1] == "p":
            hero.move(x - 1, y)
    elif movement == "right":
        if x < level_x - 1 and level[y][x + 1] == "." or x < level_x - 1 and level[y][x + 1] == "p":
            hero.move(x + 1, y)




class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = pos_x, pos_y

    def move(self, x, y):
        self.pos = (x, y)
        global pos
        self.rect = self.image.get_rect().move(
            tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)


if __name__ == '__main__':
    start_screen()
    player = None
    level = load_level('map.txt')
    player, level_x, level_y = generate_level(level)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_hero(player, 'right')
                if event.key == pygame.K_LEFT:
                    move_hero(player, 'left')
                if event.key == pygame.K_UP:
                    move_hero(player, 'up')
                if event.key == pygame.K_DOWN:
                    move_hero(player, 'down')
                screen.fill(pygame.Color('black'))
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)