import pygame


class World:
    def __init__(self, game):
        self.game = game

    def update(self):
        dt = self.game.renderer.dt
        return

    def render(self, display: pygame.Surface):
        asset = self.game.asset

        display.blit(asset.image.background, (0, 0))
        return
