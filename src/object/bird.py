from src.object._entity import Entity, PhysicsEntity
from src.object._hitbox import HitBox


class Bird(PhysicsEntity):
    def __init__(self, game):
        self.game = game

        animation = game.asset.image.bird_fly_ani.copy()

        rotate_pos = (25, 18)
        self.rotate_acc = 0

        self.stop = True

        super().__init__(
            animation=animation,
            hitbox=HitBox((51, 36)),
            rotate_pos=rotate_pos,
        )
        return

    def ready(self):
        """game ready"""
        self.stop = True
        self.pos = [115, 370]
        self.animation.speed = 0.2
        self.angle = 0
        self.rotate_acc = 0
        return

    def play(self):
        """game play"""
        self.stop = False
        self.animation.speed = 1
        return

    def jump(self):
        if self.stop:
            return

        self.angle = self.game.world.JUMP_ANGLE
        self.rotate_acc = 0

        self.y_acc = -self.game.world.JUMP
        return

    def update(self, dt: int):
        if not self.stop:
            self.rotate_acc += self.game.world.ROTATE_SPEED
            self.angle -= self.rotate_acc
            if self.angle <= -90:
                self.angle = -90
            self.y_acc += self.game.world.GRAVITY

        if self.pos[1] < -20:
            self.pos[1] = -20
            self.y_acc = 0
        if self.pos[1] > (floor_y_pos := self.game.window.display_size[1] - 168):
            self.pos[1] = floor_y_pos
            self.y_acc = 0

        super().update(dt)
        return


class IntroBird(Entity):
    def __init__(self, game):
        self.game = game

        animation = game.asset.image.bird_fly_ani.copy()
        animation.speed = 0.1

        super().__init__(pos=[0, 0], animation=animation)
        return

    def setup(self):
        self.animation.reset()
        return

    def update(self, dt: int):
        super().update(dt)
        return
