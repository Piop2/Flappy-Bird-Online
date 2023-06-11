import pygame

from src.util.animation import Animation


class Object:
    def __init__(
        self,
        pos=None,
        image: pygame.Surface = None,
        animation: Animation = None,
    ):
        if pos is None:
            pos = [0, 0]

        self.pos: list[int, int] = pos
        self.image: pygame.Surface = image
        self.animation: Animation = animation
        return

    def get_image(self) -> pygame.Surface:
        if self.animation is not None:
            return self.animation.image.copy()
        return self.image.copy()

    def setup(self):
        return

    def update(self, dt: int):
        if self.animation is not None:
            self.animation.update(dt)
        return

    def render(self, display: pygame.Surface):
        image = self.get_image()
        display.blit(
            image,
            (
                self.pos[0] - (image.get_width() / 2),
                self.pos[1] - (image.get_height() / 2),
            ),
        )
        return
