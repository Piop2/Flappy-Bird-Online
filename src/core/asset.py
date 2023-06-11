from src.util.animation import Animation
from src.util.image import load_image, load_images


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
        self.flappy29 = load_image("asset/icon/flappy29.png")
        return


class Image:
    def __init__(self):
        self.background = load_image("asset/image/background.png")
        self.floor = load_image("asset/image/floor.png")

        titles = load_images(
            "asset/image/titles.png",
            [(0, 0, 288, 66), (0, 78, 282, 57), (0, 144, 261, 66)],
        )
        self.title_flappy_bird = titles[0]
        self.title_game_over = titles[1]
        self.title_get_ready = titles[2]

        big_buttons = load_images(
            "asset/image/big_buttons.png",
            [(0, 0, 120, 42), (0, 90, 120, 42), (123, 90, 120, 42)]
        )
        self.button_start = big_buttons[0]
        self.button_score = big_buttons[1]
        self.button_multi = big_buttons[2]

        # animation
        self.bird_fly_ani = Animation.load("asset/animation/bird.json")
        return


class Sound:
    pass
