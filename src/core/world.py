from pygame import Surface

from src.object.background import Background
from src.object.floor import Floor
from src.entity.bird import Bird


class World:
    def __init__(self, game):
        self.game = game

        # setting
        self.speed = 0.2
        self.gravity = 0.05
        self.jump = 1

        self.background = Background(game)
        self.floor = Floor(game)

        self.title_flappy_bird = game.asset.image.title_flappy_bird
        self.title_game_over = game.asset.image.title_game_over
        self.title_get_ready = game.asset.image.title_get_ready

        self.bird = Bird(game)

    def update(self):
        game_input = self.game.input

        if game_input.jump:
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

        self.bird.render(display)
        return
