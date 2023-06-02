import pygame

from src.object._object import Object
from src.util.animation import Animation


class Entity(Object):
    def __init__(self, pos: list[int, int], image: pygame.Surface = None, animation: Animation = None):
        super().__init__(pos, image)
        self.animation: Animation = animation
        # self.hitbox = hitbox
        return

    def update(self, dt: int):
        if self.animation is not None:
            self.animation.update(dt)
        return

    def render(self, display: pygame.Surface):
        image = self.image
        if self.animation is not None:
            image = self.animation.image

        display.blit(image, self.pos)
        return


class PhysicsEntity(Entity):
    def __init__(self, pos: list[int, int], image: pygame.Surface = None, animation: Animation = None):
        super().__init__(pos, image, animation)

        self.y_acc = 0
        return

    def update(self, dt: int):
        self.pos[1] += self.y_acc * dt
        super().update(dt)
        return
