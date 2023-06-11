from dataclasses import dataclass
import sys

import pygame
from pygame.locals import *


@dataclass()
class Event:
    mouse_pos: tuple[int, int] = (0, 0)
    click_l: bool = False

    jump: bool = False


class Input:
    def __init__(self, game):
        self.game = game

        self.event = Event()
        return

    def update(self):
        self.event.mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # keyboard
            if event.type == KEYDOWN:
                if event.key == K_F11:
                    if self.game.window.is_full:
                        self.game.window.set_window()
                    else:
                        self.game.window.set_fullscreen()

                if event.key == K_SPACE:
                    self.event.jump = True

            # mouse
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.event.click_l = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    self.event.click_l = False
        return
