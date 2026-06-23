from random import randrange

import pygame as pg

from config import RANGE, TILE_SIZE


class Food:
    def __init__(self):
        self.rect = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
        self.place()

    def place(self):
        self.rect.center = randrange(*RANGE), randrange(*RANGE)

    def draw(self, screen):
        pg.draw.rect(screen, "red", self.rect)
