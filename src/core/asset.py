import pygame

IMAGE_SCALE = 3


class Asset:
    def __init__(self):
        self.animation = Animation()
        self.font = Font()
        self.icon = Icon()
        self.image = Image()
        self.sound = Sound()


class Save:
    pass


class Animation:
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
        self.bird = load_image("asset/image/bird.png")


class Sound:
    pass


def load_image(path: str, scale: int = IMAGE_SCALE) -> pygame.Surface:
    return pygame.transform.scale_by(pygame.image.load(path), scale)
