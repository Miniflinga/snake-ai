from random import randrange

import pygame as pg

from config import RANGE, TILE_SIZE, WINDOW


class Snake:
    def __init__(self):
        self.rect = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
        self.reset()

    def reset(self):
        self.rect.center = randrange(*RANGE), randrange(*RANGE)
        self.length = 1
        self.segments = [self.rect.copy()]
        self.direction = (0, 0)  # snake's actual direction
        self.next_direction = (0, 0)  # snake's next wished direction

    def set_direction(self, direction):
        self.next_direction = direction

    def move(self):
        if (
            self.next_direction[0] + self.direction[0],
            self.next_direction[1] + self.direction[1],
        ) != (0, 0):
            self.direction = self.next_direction
        self.rect.move_ip(self.direction)  # move snake head
        self.segments.append(
            self.rect.copy()
        )  # save the head's position last in the list
        self.segments = self.segments[
            -self.length :
        ]  # keep only last length segments (=snake length)

    def grow(self):
        self.length += 1

    def check_collision(self):
        self_bite = pg.Rect.collidelist(self.rect, self.segments[:-1]) != -1
        hit_wall = (
            self.rect.left < 0
            or self.rect.right > WINDOW
            or self.rect.top < 0
            or self.rect.bottom > WINDOW
        )
        return self_bite or hit_wall

    def draw(self, screen):
        for segment in self.segments:
            pg.draw.rect(screen, "green", segment)
