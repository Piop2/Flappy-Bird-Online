from src.object._object import Object


class Background(Object):
    def __init__(self, game):
        super().__init__(
            pos=[0, 0],
            image=game.asset.image.background.copy()
        )
