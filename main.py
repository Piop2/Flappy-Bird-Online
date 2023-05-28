import pygame

from src.core.window import Window
from src.core.renderer import Renderer
from src.core.input import Input


class Game:
    def __init__(self):
        pygame.init()

        self.window = Window()
        self.renderer = Renderer(self)
        self.input = Input(self)

    def update(self):
        self.window.update()
        self.renderer.update()
        self.input.update()

    def run(self):
        while True:
            self.update()


if __name__ == '__main__':
    Game().run()
