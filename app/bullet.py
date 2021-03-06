import os

from app.enemy.enemy import Enemy
from app.logic.collision.collisionPlayer import *
from app.tools.animation import Animation

class Bullet(Enemy):
    def __init__(self, x, y, direction=RIGHT, friendly=True):
        super().__init__(x, y, os.path.join('img', 'bullet_v1.png'))

        self.name = "bullet"

        self.imageBulletRight = list()
        self.imageBulletRight.append(pygame.image.load(os.path.join('img', 'bullet_v3.png')))
        self.imageBulletRight.append(pygame.image.load(os.path.join('img', 'bullet_v1.png')))
        self.imageBulletRight.append(self.imageBulletRight[0])
        self.imageBulletRight.append(pygame.image.load(os.path.join('img', 'bullet_v2.png')))

        self.imageBulletLeft = list()
        self.imageBulletLeft.append(pygame.image.load(os.path.join('img', 'bullet_v4.png')))
        self.imageBulletLeft.append(pygame.image.load(os.path.join('img', 'bullet_v5.png')))
        self.imageBulletLeft.append(self.imageBulletLeft[0])
        self.imageBulletLeft.append(pygame.image.load(os.path.join('img', 'bullet_v6.png')))

        self.image = self.imageBulletRight[0]

        self.direction = direction

        self.rect = self.image.get_rect()
        self.rect.y = y - self.rect.height/2

        if direction == RIGHT:
            self.speedx = 10
            self.image = self.imageBulletRight[0]
            self.imageBulletList = self.imageBulletRight
            self.rect.x = x
        elif direction == LEFT:
            self.speedx = -10
            self.image = self.imageBulletLeft[0]
            self.imageBulletList = self.imageBulletLeft
            self.rect.x = x - self.rect.width
        self.speedy = 0

        self.animation = Animation(self.image, {RIGHT: self.imageBulletRight, LEFT: self.imageBulletLeft})

        self.friendly = friendly

    def update(self):
        self.rect.x += self.speedx
        self.animation.update(self)