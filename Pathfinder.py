import pygame as pg
from random import random
from collections import deque

cols, rows = 25, 15
TILE = 60

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()

while True:
    sc.fill(pg.Color('black'))

    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(10)