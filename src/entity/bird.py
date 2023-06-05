from src.entity._entity import PhysicsEntity


class Bird(PhysicsEntity):
    def __init__(self, game):
        self.game = game

        super().__init__(
            pos=[0, 0],
            animation=game.asset.image.bird_fly_ani
        )

    def jump(self):
        self.y_acc = - self.game.world.jump
        return

    def update(self, dt: int):
        self.y_acc += self.game.world.gravity

        if self.pos[1] <= -10:
            self.pos[1] = -10
            self.y_acc = 0

        super().update(dt)
        return
