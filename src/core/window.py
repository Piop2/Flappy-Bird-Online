import pygame

from src.version import VERSION

MIN_WINDOW_SIZE = (432, 768)
WINDOW_SIZE_RATIO = (144, 256)


class Window:
    def __init__(self):
        display_info = pygame.display.Info()
        self.monitor_size = (display_info.current_w, display_info.current_h)

        self.window_size = (432, 768)
        self.window = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)

        self.display_size = (432, 768)
        self.display = pygame.Surface(self.display_size)

        self._is_full = False

        pygame.display.set_caption(
            f"Flappy Bird v{VERSION[0]}.{VERSION[1]}.{VERSION[2]}"
        )

    @property
    def is_full(self) -> bool:
        return self._is_full

    def set_fullscreen(self):
        self._is_full = True
        self.window = pygame.display.set_mode(self.monitor_size, pygame.FULLSCREEN)
        return

    def set_window(self):
        self._is_full = False
        self.window = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)
        return

    def update(self):
        if self._is_full:
            return

        resized_size = pygame.display.get_window_size()

        if resized_size == self.window_size:
            return

        final_size = list(resized_size)

        if resized_size[0] <= MIN_WINDOW_SIZE[0]:
            final_size[0] = MIN_WINDOW_SIZE[0]
        if resized_size[1] <= MIN_WINDOW_SIZE[1]:
            final_size[1] = MIN_WINDOW_SIZE[1]

        self.window_size = tuple(final_size)
        self.window = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)
