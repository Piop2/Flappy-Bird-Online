from pygame import Surface

from src.object.background import Background
from src.object.floor import Floor
from src.entity.bird import Bird


class World:
    def __init__(self, game):
        self.game = game

        # setting
        self.GRAVITY = 0.05
        self.MAX_HEIGHT = -20
        self.SPEED = 0.2
        self.JUMP = 1

        self._status = ""

        self.background = Background(game)
        self.floor = Floor(game)

        self.title_flappy_bird = game.asset.image.title_flappy_bird
        self.title_game_over = game.asset.image.title_game_over
        self.title_get_ready = game.asset.image.title_get_ready

        self.bird = Bird(game)

        self.status = "ready"

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new: str):
        self._status = new
        match new:
            case "intro":
                pass
            case "ready":
                self.bird.ready()
            case "play":
                self.bird.play()
        return

    def update(self):
        game_input = self.game.input

        if game_input.jump:
            self.status = "play"
            game_input.jump = False
            self.bird.jump()

        dt = self.game.renderer.dt
        self.floor.update(dt)
        self.bird.update(dt)
        return

    def render(self, display: Surface):
        self.background.render(display)
        self.floor.render(display)

        # for test
        # display.blit(self.title_flappy_bird, (0, 0))
        # display.blit(self.title_game_over, (0, 100))
        # display.blit(self.title_get_ready, (0, 200))

        if not self.status == "intro":
            self.bird.render(display)
        return
