import pygame
import os

from app.enemy.enemy import Enemy
from app.bullet import Bullet
from app.settings import *

class EnemyShooter(Enemy):
    def __init__(self, x, y, theMap, direction="Right"):
        super().__init__(x, y, os.path.join('img', 'enemy1_v1.png'))

        self.name = "enemyShooter"

        self.imageEnemy_v1 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'enemy3_v1.png')), (TILEDIMX, TILEDIMY))
        self.imageEnemy_v2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'enemy3_v2.png')), (TILEDIMX, TILEDIMY))

        self.speedx = 0
        self.speedy = 0

        self.theMap = theMap

        self.setDirection(direction)

        self.isGravityApplied = True
        self.isCollisionApplied = True

        self.imageIterShoot = 40
        self.imageWaitNextShoot = 80

    def setDirection(self, direction):
        self.direction = direction
        if self.direction == "Right":
            self.image = self.imageEnemy_v1
        if self.direction == "Left":
            self.image = self.imageEnemy_v2

    def update(self):

        self.imageIterShoot += 1
        if self.imageIterShoot > self.imageWaitNextShoot:

            if self.direction == "Right":
                bullet = Bullet(self.rect.x + self.rect.width +1, self.rect.centery, RIGHT, False)
            elif self.direction == "Left":
                bullet = Bullet(self.rect.x -1, self.rect.centery, LEFT, False)

            self.theMap.camera.add(bullet)
            self.theMap.allSprites.add(bullet)
            self.theMap.enemyBullet.add(bullet)

            self.imageIterShoot = 0



