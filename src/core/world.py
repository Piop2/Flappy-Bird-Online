from pygame import Surface

from src.object.background import Background
from src.object.floor import Floor
from src.object.bird import Bird, IntroBird


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

        self._status = ""
        self.in_game = False

        self.background = Background(game)
        self.floor = Floor(game)

        self.title_flappy_bird = game.asset.image.title_flappy_bird
        self.title_game_over = game.asset.image.title_game_over
        self.title_get_ready = game.asset.image.title_get_ready

        self.bird = Bird(game)
        self.intro_bird = IntroBird(game)

        self.status = "ready"

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new: str):
        self._status = new
        match new:
            case "menu":
                self.in_game = False
                self.intro_bird.setup()
            case "ready":
                self.in_game = True
                self.bird.ready()
            case "play":
                self.in_game = True
                self.bird.play()
            case "gameOver":
                self.in_game = True
                self.bird.animation.pause()
                pass
        return

    def update(self):
        dt = self.game.renderer.dt
        game_input = self.game.input

        if not self.status == "gameOver":
            self.floor.update(dt)

        # MENU #

        if not self.in_game:
            self.intro_bird.update(dt)
            return

        # IN GAME #

        if self.bird.is_collide([self.floor.hitbox]):
            self.status = "gameOVer"

        if game_input.jump:
            self.status = "play"
            game_input.jump = False
            self.bird.jump()

        self.bird.update(dt)
        return

    def render(self, display: Surface):
        self.background.render(display)
        self.floor.render(display)

        # for test
        # display.blit(self.title_flappy_bird, (0, 0))
        # display.blit(self.title_game_over, (0, 100))
        # display.blit(self.title_get_ready, (0, 200))

        if self.status == "menu":
            self.intro_bird.render(display)
        else:  # in game
            self.bird.render(display)
        return
