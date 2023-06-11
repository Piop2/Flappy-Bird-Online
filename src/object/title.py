import pygame

from src.object._object import Object


class TitleFlappyBird(Object):
    def __init__(self, game):
        self.game = game

        super().__init__()

        self.title = game.asset.image.title_flappy_bird.copy()
        self.bird_ani = game.asset.image.bird_fly_ani.copy()
        self.bird_ani.speed = 0.5
        self.bird_space = [20, 10]

        self.range = (180, 200)
        self.speed = 0.05
        self.direction = 1

    def setup(self):
        self.pos = [
            (self.game.window.display_size[0] / 2)
            - ((self.title.get_width() + self.bird_ani.size[0] + self.bird_space[0]) / 2),
            180,
        ]
        return

    def update(self, dt: int):
        self.bird_ani.update(dt)

        self.pos[1] += self.direction * self.speed * dt
        if self.pos[1] <= self.range[0]:
            self.direction *= -1
            self.pos[1] = self.range[0]
        if self.pos[1] >= self.range[1]:
            self.direction *= -1
            self.pos[1] = self.range[1]
        return

    def render(self, display: pygame.Surface):
        display.blit(self.title, self.pos)
        display.blit(
            self.bird_ani.image,
            (self.pos[0] + self.title.get_width() + self.bird_space[0], self.pos[1] + self.bird_space[1]),
        )
        return
