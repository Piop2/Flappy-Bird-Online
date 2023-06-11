import pygame

from src.core.input import Event


class Layout:
    def __init__(self, world):
        self.world = world
        self.status = world.status
        return

    def setup(self):
        return

    def update(self, dt: int, event: Event):
        return

    def render(self, display: pygame.Surface):
        return
