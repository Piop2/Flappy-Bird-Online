import pygame

from src.object._object import Object
from src.util.animation import Animation
from src.object._hitbox import HitBox


class Entity(Object):
    def __init__(self, pos: list[int, int], image: pygame.Surface = None, animation: Animation = None,
                 hitbox: HitBox = None):
        super().__init__(pos, image, animation)
        self.hitbox = hitbox
        return


class PhysicsEntity(Entity):
    def __init__(self, pos: list[int, int], image: pygame.Surface = None, animation: Animation = None,
                 hitbox: HitBox = None):
        super().__init__(pos, image, animation, hitbox)

        self.y_acc = 0
        return

    def update(self, dt: int):
        self.pos[1] += self.y_acc * dt
        super().update(dt)
        return
