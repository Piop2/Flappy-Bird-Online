import json

import pygame

from src.util.image import clips


class Animation:
    def __init__(self, images: list[pygame.Surface], durations: list[int]):
        self.images = images
        self.durations = durations

        self.frame = 0
        self.timer = 0
        self.speed = 1
        self.playing = True
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
        return cls(images=frame_images, durations=durations)

    def pause(self):
        self.playing = False
        return

    def play(self):
        self.playing = True
        return

    @property
    def image(self) -> pygame.Surface:
        return self.images[self.frame]

    def update(self, dt: int):
        if not self.playing:
            return

        self.timer += dt * self.speed
        if self.timer >= self.durations[self.frame]:
            self.timer = 0

            self.frame += 1
            if self.frame == len(self.images):
                self.frame = 0
        return
