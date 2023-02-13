import pygame as pg

cols, rows = 25, 15
TILE = 60

pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()

while True:
    sc.fill(pg.Color('black'))