import pygame


class Object:
    def __init__(self, pos, image):
        self.pos = pos
        self.image = image

    def update(self, dt: int):
        return

    def render(self, display: pygame.Surface):
        display.blit(self.image, self.pos)
        return
