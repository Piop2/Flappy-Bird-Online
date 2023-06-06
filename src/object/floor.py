import pygame

from src.entity._entity import Entity


class Floor(Entity):
    def __init__(self, game):
        self.game = game

        image = game.asset.image.floor.copy()

        super().__init__(
            pos=[0, game.window.display_size[1] - image.get_height()],
            image=image
        )

    def update(self, dt: int):
        speed = self.game.world.SPEED

        self.pos[0] -= speed * dt
        if self.pos[0] <= - self.image.get_width():
            self.pos[0] = 0
        return

    def render(self, display: pygame.Surface):
        display.blit(self.image, self.pos)
        display.blit(
            self.image,
            (
                self.pos[0] + self.image.get_width(),
                self.pos[1]
            )
        )
        return
