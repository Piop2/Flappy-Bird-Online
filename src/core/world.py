from dataclasses import dataclass

from pygame import Surface

from src.object.background import Background
from src.object.floor import Floor
from src.object.bird import Bird
from src.object.title import *
from src.ui.button import *
from src.layout.home import Home


@dataclass()
class Status:
    main: str
    sub: str


class World:
    def __init__(self, game):
        self.game = game

        # setting
        self.GRAVITY = 0.05
        self.MAX_HEIGHT = -20
        self.SPEED = 0.2
        self.JUMP = 1
        self.JUMP_ANGLE = 45
        self.ROTATE_SPEED = 0.1

        self.background = Background(game)
        self.floor = Floor(game)
        self.bird = Bird(game)

        self.title_flappy_bird = TitleFlappyBird(game)

        self.start_button = StartButton(game)
        self.score_button = ScoreButton(game)
        self.multi_button = MultiButton(game)

        self.status = Status(main="home", sub="")
        self.stage = {"home": Home(self)}

        self.init_stage()
        return

    def _get_stage(self):
        return self.stage[self.status.main]

    def init_stage(self):
        self._get_stage().init_object()
        return

    def update(self):
        self._get_stage().update(self.game.renderer.dt, self.game.input.event)
        return

    def render(self, display: Surface):
        display.fill((255, 255, 255))
        self._get_stage().render(display)
        return
