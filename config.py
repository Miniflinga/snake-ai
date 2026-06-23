import pygame as pg

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
DIRECTIONS = {
    pg.K_w: (0, -TILE_SIZE),
    pg.K_s: (0, TILE_SIZE),
    pg.K_a: (-TILE_SIZE, 0),
    pg.K_d: (TILE_SIZE, 0),
}
SPEED = 110
