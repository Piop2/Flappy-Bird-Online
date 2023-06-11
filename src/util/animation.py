import json

import pygame

from src.util.image import clips


class Animation:
    def __init__(
        self,
        images: list[pygame.Surface],
        durations: list[int],
        size: tuple[int, int],
        speed: int = 1,
    ):
        self._images = images
        self._durations = durations
        self._size = size

        self._frame = 0
        self._timer = 0
        self._speed = speed
        self._playing = True
        return

    @classmethod
    def load(cls, path: str):
        with open(path, "r") as f:
            ani_data = json.load(f)

        frame_data = []
        durations = []
        for frame in ani_data["frames"]:
            frame_data.append(tuple(frame["frame"].values()))
            durations.append(frame["duration"])

        sprites = pygame.image.load(ani_data["meta"]["image"])
        frame_images = clips(sprites, frame_data)
        size = tuple(ani_data["meta"]["size"].values())
        return cls(images=frame_images, durations=durations, size=size)

    @property
    def size(self) -> tuple[int, int]:
        return self._size

    @property
    def speed(self) -> int | float:
        return self._speed

    @speed.setter
    def speed(self, new: int | float):
        self._speed = new
        return

    def copy(self):
        return Animation(
            images=self._images,
            durations=self._durations,
            size=self._size,
            speed=self._speed,
        )

    def reset(self):
        self._frame = 0
        return

    def pause(self):
        self._playing = False
        return

    def play(self):
        self._playing = True
        return

    @property
    def image(self) -> pygame.Surface:
        return self._images[self._frame]

    def update(self, dt: int):
        if not self._playing:
            return

        self._timer += dt * self._speed
        if self._timer >= self._durations[self._frame]:
            self._timer = 0

            self._frame += 1
            if self._frame == len(self._images):
                self._frame = 0
        return
