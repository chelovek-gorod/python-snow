import pygame as PG
import sys
from random import randint

PG.init()
PG.mouse.set_visible(False)

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 435
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PG.display.set_caption('Winter')
ICON = PG.image.load('./icon.png').convert_alpha()
PG.display.set_icon(ICON)

FPS = 60

CLOCK = PG.time.Clock()
SPRITE = PG.sprite.Sprite
GROUP = PG.sprite.Group

class Snowflake():
    def __init__(self):
        self.start_image = snowflake
        self.generate()
        self.rect.y = randint(0, SCREEN_HEIGHT-self.size)

    def generate(self):
        self.speed = randint(2, 4)
        self.size = randint(32, 100)
        self.rect = PG.Rect(
            randint(0, SCREEN_WIDTH-self.size), -self.size, self.size, self.size)
        self.image = PG.transform.scale(self.start_image, (self.size, self.size))

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT : self.generate()
        self.draw()

    def draw(self):
        SCREEN.blit(self.image, self.rect)

BG = PG.image.load('./winter_bg_750x435px.png').convert()
snowflake = PG.image.load('./snowflake_160x160px.png').convert_alpha()

snow_list = []

for i in range(100):
    snow_list.append(Snowflake())

# ИГРОВОЙ ЦИКЛ
game_loop_is = True
while game_loop_is:
    CLOCK.tick(FPS)

    SCREEN.blit(BG, (0, 0))

    for snowflake in snow_list : snowflake.update()

    PG.display.flip()

    for event in PG.event.get():
        # проверка выхода из игры (Escape или нажали на кнопку закрытия окна с игрой)
        if event.type == PG.QUIT \
        or (event.type == PG.KEYDOWN and event.key == PG.K_ESCAPE):
            game_loop_is = False

PG.quit()
sys.exit()
