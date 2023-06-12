import pygame

from src.core.input import Event
from src.ui._ui import Interface


class Button(Interface):
    def __init__(self, image: pygame.Surface, push_y: int = 10):
        size = image.get_size()
        super().__init__(size, image)

        self._down = False
        self._is_active = False
        self._push_y = push_y
        return

    @property
    def is_active(self) -> bool:
        return self._is_active

    def setup(self):
        self._is_active = False
        self._down = False
        return

    def update(self, event: Event):
        pos = (
            self.pos[0] - (self.size[0] / 2),
            self.pos[1] - (self.size[1] / 2)
        )
        self._is_active = False
        if not (pos[0] <= event.mouse_pos[0] <= pos[0] + self.size[0] and pos[1] <= event.mouse_pos[1] <= pos[1] + self.size[1]):
            self._down = False
            return

        if event.click_l:
            self._down = True
        elif self._down:
            self._down = False
            self._is_active = True
        return

    def render(self, display: pygame.Surface):
        pos = [self.pos[0] - (self.image.get_width() / 2), self.pos[1] - (self.image.get_height() / 2)]
        if self._down:
            pos[1] += self._push_y
        display.blit(self.image, pos)
        return
