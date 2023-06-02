import pygame


class Object:
    def __init__(self, pos: list[int, int], image: pygame.Surface):
        self.pos: list[int, int] = pos
        self.image: pygame.Surface = image
        return

    def update(self, dt: int):
        return

    def render(self, display: pygame.Surface):
        display.blit(self.image, self.pos)
        return
