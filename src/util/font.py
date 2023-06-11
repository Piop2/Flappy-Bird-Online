import json

import pygame

from src.util.image import clip


class Text:
    def __init__(self, image: pygame.Surface):
        self._image = image
        self._width = image.get_width()

    @property
    def image(self) -> pygame.Surface:
        return self._image

    @property
    def width(self) -> int:
        return self._width


class BitMapFont:
    def __init__(self, fonts: dict[str:Text], font_height: int, letter_space: int, line_space: int, space: int, scale: int):
        self.fonts = fonts
        self.font_height = font_height
        self.letter_space = letter_space
        self.line_space = line_space
        self.space = space
        self.scale = scale

    @classmethod
    def load(cls, path: str, scale: int = 1):
        with open(path, "r") as f:
            font_data = json.load(f)

        orders = font_data["fonts"]
        sprite = pygame.image.load(font_data["meta"]["image"])
        key = pygame.Color(font_data["meta"]["key"])
        font_height = font_data["meta"]["fontHeight"]
        letter_space = font_data["meta"]["letterSpace"]
        line_space = font_data["meta"]["lineSpace"]
        space = font_data["meta"]["space"]

        fonts = {}
        start_x = 0
        for letter in orders:
            for end_x in range(start_x, sprite.get_width()):
                if sprite.get_at((end_x, 0)) == key:
                    fonts[letter] = Text(clip(sprite, (start_x, 0, end_x - start_x, font_height)))
                    start_x = end_x + 1
                    break

        return cls(fonts=fonts, font_height=font_height, letter_space=letter_space, line_space=line_space, space=space, scale=scale)

    def _get_text(self, text: str) -> Text:
        return self.fonts[text]

    def _get_size(self, text: str) -> tuple[int, int]:
        lines = text.split("\n")

        width = 0
        height = (self.font_height + self.line_space) * len(lines) - self.line_space

        for line in lines:
            w = 0
            for i, letter in enumerate(line):
                if letter == " ":
                    w += self.space
                    continue
                try:
                    t = self._get_text(letter)
                except KeyError:
                    t = self._get_text("default")
                w += t.width
                if not i == len(line) - 1:
                    w += self.letter_space
            width = max(width, w)

        return width, height

    def get_size(self, text: str) -> tuple[int, int]:
        size = self._get_size(text)
        return size[0] * self.scale, size[1] * self.scale

    def get_image(self, text: str) -> pygame.Surface:
        surf = pygame.Surface(self._get_size(text))
        surf.fill((1, 1, 1))
        surf.set_colorkey((1, 1, 1))

        lines = text.split("\n")

        y = 0
        for line in lines:
            x = 0
            for i, letter in enumerate(line):
                if letter == " ":
                    x += self.space
                    continue
                try:
                    t = self._get_text(letter)
                except KeyError:
                    t = self._get_text("default")
                surf.blit(t.image, (x, y))
                x += t.width
                if not i == len(line) - 1:
                    x += self.letter_space
            y += self.font_height + self.line_space

        return pygame.transform.scale_by(surf, self.scale)
