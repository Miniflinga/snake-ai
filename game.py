import pygame as pg

from config import DIRECTIONS, SPEED, WINDOW
from food import Food
from snake import Snake


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode([WINDOW] * 2)
        self.clock = pg.time.Clock()
        self.font = pg.font.Font(None, 60)
        self.snake = Snake()
        self.food = Food()
        self.time = 0
        self.time_step = SPEED
        self.running = True

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key in DIRECTIONS:
                    self.snake.set_direction(DIRECTIONS[event.key])
                if event.key == pg.K_ESCAPE:
                    self.running = False

    def update(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.time_step:
            self.time = time_now
            self.snake.move()
            if self.snake.check_collision():
                self.snake.reset()
                self.food.place()
                # self.time_step = SPEED
            if self.snake.rect.center == self.food.rect.center:
                self.food.place()
                self.snake.grow()
                # self.time_step -= 10

    def draw(self):
        self.screen.fill("black")
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        score = self.font.render(f"Score: {self.snake.length - 1}", True, "white")
        self.screen.blit(score, (20, 20))
        pg.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pg.quit()
