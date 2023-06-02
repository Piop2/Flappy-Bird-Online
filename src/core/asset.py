import pygame

from src.util.clip import clips

IMAGE_SCALE = 3


class Asset:
    def __init__(self):
        self.font = Font()
        self.icon = Icon()
        self.image = Image()
        self.sound = Sound()


class Save:
    pass


class Font:
    pass


class Icon:
    def __init__(self):
        self.flappy29 = load_image("asset/icon/flappy29.png", 1)


class Image:
    def __init__(self):
        self.background = load_image("asset/image/background.png")
        self.floor = load_image("asset/image/floor.png")

        titles = load_images("asset/image/titles.png", [(0, 0, 96, 22), (0, 26, 94, 19), (0, 48, 87, 22)])
        self.title_flappy_bird = titles[0]
        self.title_game_over = titles[1]
        self.title_get_ready = titles[2]


class Sound:
    pass


def load_image(path: str, scale: int = IMAGE_SCALE) -> pygame.Surface:
    return pygame.transform.scale_by(pygame.image.load(path), scale)


def load_images(path: str, rects: list[tuple[int, int, int, int]], scale: int = IMAGE_SCALE) -> list[pygame.Surface]:
    return [pygame.transform.scale_by(surf, scale) for surf in clips(pygame.image.load(path), rects)]
