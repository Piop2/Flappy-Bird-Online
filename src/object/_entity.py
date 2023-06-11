import pygame

from src.object._object import Object
from src.util.animation import Animation
from src.object._hitbox import HitBox
from src.util.image import rotate


class Entity(Object):
    def __init__(
            self,
            pos=None,
            image: pygame.Surface = None,
            animation: Animation = None,
            hitbox: HitBox = None,
            rotate_pos: tuple[int, int] = (0, 0),
    ):
        if pos is None:
            pos = [0, 0]
        super().__init__(pos, image, animation)

        self.hitbox = hitbox
        self.angle = 0
        self.rotate_pos = rotate_pos
        return

    def update(self, dt: int):
        self.hitbox.pos = self.pos
        super().update(dt)
        return

    def is_collide(self, hitbox_list: list[HitBox]):
        return self.hitbox.is_collide(hitbox_list)

    def render(self, display: pygame.Surface):
        image = self.get_image()
        display.blit(
            *rotate(
                image,
                self.pos,
                self.rotate_pos,
                self.angle,
            )
        )
        return


class PhysicsEntity(Entity):
    def __init__(
            self,
            pos=None,
            image: pygame.Surface = None,
            animation: Animation = None,
            hitbox: HitBox = None,
            rotate_pos: tuple[int, int] = None,
    ):
        if pos is None:
            pos = [0, 0]
        super().__init__(pos, image, animation, hitbox, rotate_pos)

        self.y_acc = 0
        return

    def update(self, dt: int):
        self.pos[1] += self.y_acc * dt
        super().update(dt)
        return
