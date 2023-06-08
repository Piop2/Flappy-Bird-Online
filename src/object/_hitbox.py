import pygame


class HitBox:
    def __init__(self, size: tuple[int, int]):
        self.size: tuple[int, int] = size

    def get_rect(self, pos: list[int, int]) -> pygame.Rect:
        return pygame.Rect(*pos, *self.size)

    def is_collide(self, pos: list[int, int], hitbox_list) -> bool:
        for hitbox in hitbox_list:
            if self.get_rect(pos).colliderect(hitbox.get_rect()):
                return True
        return False