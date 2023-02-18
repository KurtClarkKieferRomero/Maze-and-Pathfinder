import pygame as pg
from random import random
from collections import deque

def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


cols, rows = 25, 15
TILE = 60

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()
grid = [[1 if random() < 0.2 else 0 for col in range(cols)]
        for row in range(rows)]

while True:
    sc.fill(pg.Color('black'))
    # draw grid
    [[pg.draw.rect(sc, pg.Color('darkorange'), get_rect(x, y), border_radius=TILE // 5) for x, col in enumerate(row) if col] for y, row in enumerate(grid)]

    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(10)