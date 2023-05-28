import pygame


class Renderer:
    def __init__(self, game):
        self.game = game

        self.fps = 60
        self.dt = 0
        self.clock = pygame.time.Clock()

    def update(self):
        window_size = (
            self.game.window.window_size
            if not self.game.window.is_full
            else self.game.window.monitor_size
        )
        window = self.game.window.window
        display_size = self.game.window.display_size
        display = self.game.window.display

        self.dt = self.clock.tick(60)
        window.fill((0, 0, 0))
        display.fill((255, 255, 255))

        self.game.world.render(display)

        if window_size[1] * display_size[0] / display_size[1] <= window_size[0]:
            ratio = window_size[1] / display_size[1]
        else:
            ratio = window_size[0] / display_size[0]

        window.blit(
            pygame.transform.scale(
                display, (int(display_size[0] * ratio), int(display_size[1] * ratio))
            ),
            (
                (window_size[0] / 2) - (display_size[0] * ratio / 2),
                (window_size[1] / 2) - (display_size[1] * ratio / 2),
            ),
        )

        pygame.display.update()
