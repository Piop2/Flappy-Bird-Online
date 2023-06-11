import sys

import pygame
from pygame.locals import *


class Input:
    def __init__(self, game):
        self.game = game

        self.jump = False
        return

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_F11:
                    if self.game.window.is_full:
                        self.game.window.set_window()
                    else:
                        self.game.window.set_fullscreen()

                if event.key == K_SPACE:
                    self.jump = True
        return
