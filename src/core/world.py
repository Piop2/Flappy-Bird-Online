from pygame import Surface

from src.object.background import Background
from src.object.floor import Floor


class World:
    def __init__(self, game):
        self.game = game

        # setting
        self.speed = 0.2

        self.background = Background(game)
        self.floor = Floor(game)

    def update(self):
        dt = self.game.renderer.dt
        self.floor.update(dt)
        return

    def render(self, display: Surface):
        self.background.render(display)
        self.floor.render(display)
        return
