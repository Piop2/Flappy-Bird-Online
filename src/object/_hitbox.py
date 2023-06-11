import pygame


class HitBox:
    def __init__(self, size: tuple[int, int]):
        self._pos: list[int] = [0, 0]
        self._size: tuple[int, int] = size

    @property
    def pos(self) -> list[int]:
        return self._pos

    @pos.setter
    def pos(self, new: list[int]):
        self._pos = new
        return

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self._pos[0] - (self._size[0] / 2), self._pos[1] - (self._size[1] / 2), *self._size)

    def is_collide(self, hitbox_list) -> bool:
        rect = self.get_rect()
        for hitbox in hitbox_list:
            if rect.colliderect(hitbox.get_rect()):
                return True
        return False
