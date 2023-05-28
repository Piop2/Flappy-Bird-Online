import pygame

from src.core.asset import Asset, Save
from src.core.window import Window
from src.core.renderer import Renderer
from src.core.input import Input
from src.core.world import World


class Game:
    def __init__(self):
        pygame.init()

        self.asset = Asset()
        self.window = Window(self)
        self.renderer = Renderer(self)
        self.input = Input(self)
        self.world = World(self)

    def update(self):
        self.window.update()
        self.renderer.update()
        self.input.update()
        self.world.update()

    def run(self):
        while True:
            self.update()


if __name__ == "__main__":
    Game().run()
