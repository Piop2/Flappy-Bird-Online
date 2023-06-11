import pygame

from src.core.input import Event
from src.layout._layout import Layout


class Home(Layout):
    def __init__(self, world):
        super().__init__(world)

        self.background = world.background
        self.floor = world.floor
        self.title = world.title_flappy_bird

        self.start_button = world.start_button
        self.score_button = world.score_button
        self.multi_button = world.multi_button

    def init_object(self):
        self.floor.setup()
        self.title.setup()
        self.start_button.setup()
        self.score_button.setup()
        self.multi_button.setup()
        return

    def update(self, dt: int, event: Event):
        self.floor.update(dt)
        self.title.update(dt)
        self.start_button.update(event)
        self.score_button.update(event)
        self.multi_button.update(event)
        return

    def render(self, display: pygame.Surface):
        self.background.render(display)
        self.floor.render(display)
        self.title.render(display)
        self.start_button.render(display)
        self.score_button.render(display)
        self.multi_button.render(display)
        return
