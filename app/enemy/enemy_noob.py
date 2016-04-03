import math
import pygame
import os

from app.enemy.enemy import Enemy
from app.settings import *

class Enemy_noob(Enemy):
    def __init__(self, x, y, direction="Right"):
        super().__init__(x, y, os.path.join('img', 'enemy1_v1.png'))

        self.name = "enemy_noob"

        self.imageEnemy_v1 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'enemy1_v1.png')), (TILEDIMX, TILEDIMY))
        self.imageEnemy_v2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'enemy1_v2.png')), (TILEDIMX, TILEDIMY))

        self.initx = self.rect.x
        self.inity = self.rect.y

        self.speedBase = 1
        self.distanceMax = 200

        self.speedx = self.speedBase
        self.speedy = 0
        self.distance = 0

        self.direction = direction
        if self.direction == "Left":
            self.speedx = -self.speedBase
            self.image = self.imageEnemy_v2

        self.isGravityApplied = True
        self.isCollisionApplied = True

    def setDirection(self, direction):
        self.direction = direction
        if self.direction == "Left":
            self.speedx = -self.speedBase
            self.image = self.imageEnemy_v2
        if self.direction == "Right":
            self.speedx = self.speedBase
            self.image = self.imageEnemy_v1

    def setDistanceMax(self, distance):
        self.distanceMax = distance

    def update(self):

        if self.speedx == 0 or self.distance >= self.distanceMax:
            if self.direction == "Right":
                self.direction = "Left"
                self.image = self.imageEnemy_v2
                self.speedx = -self.speedBase
            elif self.direction == "Left":
                self.direction = "Right"
                self.image = self.imageEnemy_v1
                self.speedx = self.speedBase

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        self.distance = math.fabs(self.initx - self.rect.x)
