import pygame

from src.object._entity import Entity
from src.object._hitbox import HitBox


class Floor(Entity):
    def __init__(self, game):
        self.game = game

        image = game.asset.image.floor.copy()
        hitbox = HitBox(pos, (462 * 2, 168))

        super().__init__(pos=pos, image=image, hitbox=hitbox)
        return

    def setup(self):
        self.pos = [0, self.game.window.display_size[1] - self.image.get_height()]
        return

    def update(self, dt: int):
        speed = self.game.world.SPEED

        self.pos[0] -= speed * dt
        if self.pos[0] <= -self.image.get_width():
            self.pos[0] = 0

        super().update(dt)
        return

    def render(self, display: pygame.Surface):
        display.blit(self.image, self.pos)
        display.blit(self.image, (self.pos[0] + self.image.get_width(), self.pos[1]))
        return
