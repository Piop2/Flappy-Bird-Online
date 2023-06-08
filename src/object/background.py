from src.object._object import Object


class Background(Object):
    def __init__(self, game):
        display_size = game.window.display_size
        super().__init__(
            pos=[display_size[0] / 2, display_size[1] / 2],
            image=game.asset.image.background.copy(),
        )
