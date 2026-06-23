from random import randrange

import pygame as pg

from config import RANGE, RIGHT, TILE_SIZE, WINDOW


class Snake:
    def __init__(self):
        self.rect = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
        self.reset()

    def reset(self):
        self.rect.center = randrange(*RANGE), randrange(*RANGE)
        self.length = 1
        self.segments = [self.rect.copy()]
        self.direction = RIGHT  # snake's actual direction
        self.next_direction = RIGHT  # snake's next wished direction

    def set_direction(self, direction):
        self.next_direction = direction

    @staticmethod
    def turn_right(direction):  # q-learning method
        dx, dy = direction
        return (-dy, dx)  # 90 degrees clockwise

    @staticmethod
    def turn_left(direction):  # q-learning method
        dx, dy = direction
        return (dy, -dx)  # 90 degrees counter-clockwise

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

    def is_danger(self, point):  # q-learning adjusted with point
        test = self.rect.copy()
        test.center = point
        hit_wall = (
            test.left < 0 or test.right > WINDOW or test.top < 0 or test.bottom > WINDOW
        )
        self_eat = test.collidelist(self.segments[:-1]) != -1
        return hit_wall or self_eat

    def check_collision(self):
        return self.is_danger(self.rect.center)

    def danger_ahead(self, direction):
        head_x, head_y = self.rect.center
        point = (head_x + direction[0], head_y + direction[1])
        return self.is_danger(point)

    def food_dir(self, point):  # q-learning method
        head_x, head_y = self.rect.center
        point_x, point_y = point
        dx = (point_x > head_x) - (point_x < head_x)
        dy = (point_y > head_y) - (point_y < head_y)
        return dx, dy

    def draw(self, screen):
        for segment in self.segments:
            pg.draw.rect(screen, "green", segment)
