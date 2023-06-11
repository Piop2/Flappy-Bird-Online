from src.ui._button import Button


class StartButton(Button):
    def __init__(self, game):
        super().__init__(image=game.asset.image.button_start.copy())
        return

    def setup(self):
        self.pos = [125, 480]
        return


class ScoreButton(Button):
    def __init__(self, game):
        super().__init__(image=game.asset.image.button_score.copy())
        return

    def setup(self):
        self.pos = [307, 480]
        return


class MultiButton(Button):
    def __init__(self, game):
        super().__init__(image=game.asset.image.button_multi.copy())
        return

    def setup(self):
        self.pos = [125, 560]
        return
