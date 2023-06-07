import pygame

from src.util.animation import Animation


class Object:
    def __init__(self, pos: list[int, int], image: pygame.Surface = None, animation: Animation = None):
        self.pos: list[int, int] = pos
        self.image: pygame.Surface = image
        self.animation: Animation = animation
        return

    def get_image(self) -> pygame.Surface:
        if self.animation is not None:
            return self.animation.image.copy()
        return self.image.copy()

    def update(self, dt: int):
        if self.animation is not None:
            self.animation.update(dt)
        return

    def render(self, display: pygame.Surface):
        display.blit(self.get_image(), self.pos)
        return
