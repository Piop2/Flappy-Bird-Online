from src.entity._entity import PhysicsEntity


class Bird(PhysicsEntity):
    def __init__(self, game):
        self.game = game

        super().__init__(
            pos=[0, 0],
            animation=game.asset.image.bird_fly_ani
        )

    def update(self, dt: int):
        gravity = self.game.world.gravity

        self.y_acc += gravity
        super().update(dt)
        return
