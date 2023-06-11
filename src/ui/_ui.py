import pygame

from src.core.input import Event


class Interface:
    def __init__(self, size: tuple[int, int], image: pygame.Surface):
        self.pos = [0, 0]
        self.size = size
        self.image = image

    def setup(self):
        return

    def update(self, event: Event):
        return

    def render(self, display: pygame.Surface):
        display.blit(self.image, (self.pos[0] - (self.image.get_width() / 2), self.pos[1] - (self.image.get_height() / 2)))
        return
