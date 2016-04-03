import pygame
import os

from app.settings import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image=os.path.join('img', 'enemy1_v1.png')):
        super().__init__()

        self.name = "enemy"

        self.image = pygame.transform.scale(pygame.image.load(image), (TILEDIMX, TILEDIMY))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.jumpState = JUMP
        self.specialState = None
        self.specialWallSide = None
        self.shape = None

        self.isPhysicsApplied = False
        self.isGravityApplied = False
        self.isFrictionApplied = False
        self.isCollisionApplied = False

    def update(self):
        pass