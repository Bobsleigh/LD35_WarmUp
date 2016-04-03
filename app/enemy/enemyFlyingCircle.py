import math
import os

from app.enemy.enemy import Enemy


class EnemyFlyingCircle(Enemy):
    def __init__(self, xCenter, yCenter, radius=50):
        super().__init__(xCenter, yCenter, os.path.join('img', 'enemy2_v1.png'))

        self.name = "enemyFlyingCircle"

        self.rect = self.image.get_rect()

        self.xCenter = xCenter
        self.yCenter = yCenter

        self.angleBase = - 2 * math.pi / 100
        self.angleDir = self.angleBase
        self.angle = 0

        self.initx = self.xCenter + radius
        self.inity = self.yCenter

        self.rect.x = self.initx
        self.rect.y = self.inity

    def setRadius(self, radius):
        self.initx = self.xCenter + radius

    def setAngleDirection(self, factor):
        if factor == 1:
            self.angleDir = self.angleBase
        elif factor == -1:
            self.angleDir = -self.angleBase

    def update(self):
        self.angle = (self.angle - self.angleDir) % (2 * math.pi)
        self.rect.x = self.xCenter + (self.initx - self.xCenter) * math.cos(self.angle) \
                      + (self.inity - self.yCenter) * math.sin(self.angle)
        self.rect.y = self.yCenter - (self.initx - self.xCenter) * math.sin(self.angle) \
                      + (self.inity - self.yCenter) * math.cos(self.angle)
