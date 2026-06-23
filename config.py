import pygame as pg

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)

UP = (0, -TILE_SIZE)
DOWN = (0, TILE_SIZE)
RIGHT = (TILE_SIZE, 0)
LEFT = (-TILE_SIZE, 0)

DIRECTIONS = {
    pg.K_w: UP,
    pg.K_s: DOWN,
    pg.K_d: RIGHT,
    pg.K_a: LEFT,
}

SPEED = 110
