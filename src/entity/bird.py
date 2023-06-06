from src.entity._entity import Entity, PhysicsEntity


class Bird(PhysicsEntity):
    def __init__(self, game):
        self.game = game

        self.stop = True

        super().__init__(
            pos=[0, 0],
            animation=game.asset.image.bird_fly_ani.copy()
        )

    def ready(self):
        """game ready"""
        self.stop = True
        self.pos = [115, 370]
        self.animation.speed = 0.2
        return

    def play(self):
        """game play"""
        self.stop = False
        self.animation.speed = 1
        return

    def jump(self):
        if self.stop:
            return

        self.y_acc = - self.game.world.JUMP
        return

    def update(self, dt: int):
        if self.pos[1] <= -20:
            self.pos[1] = -20
            self.y_acc = 0

        if not self.stop:
            self.y_acc += self.game.world.GRAVITY

        super().update(dt)
        return


class IntroBird(Entity):
    def __init__(self, game):
        self.game = game

        animation = game.asset.image.bird_fly_ani.copy()
        animation.speed = 0.1

        super().__init__(
            pos=[0, 0],
            animation=animation
        )

    def setup(self):
        self.animation.reset()
        return

    def update(self, dt: int):
        super().update(dt)
        return
