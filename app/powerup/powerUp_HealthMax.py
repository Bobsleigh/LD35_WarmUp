import pygame
import os

from app.powerup.powerUp import PowerUp
from app.settings import *

class PowerUp_HealthMax(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y, os.path.join('img', 'powerUp_HealthMax_v1.png'))

        self.name = "powerUp_HealthMax"

        self.imagePUP = list()
        self.imagePUP.append(pygame.transform.scale(pygame.image.load(os.path.join('img', 'powerUp_HealthMax_v1.png')), (TILEDIMX, TILEDIMY)))
        self.imagePUP.append(pygame.transform.scale(pygame.image.load(os.path.join('img', 'powerUp_HealthMax_v2.png')), (TILEDIMX, TILEDIMY)))
        self.imagePUP.append(pygame.transform.scale(pygame.image.load(os.path.join('img', 'powerUp_HealthMax_v3.png')), (TILEDIMX, TILEDIMY)))
        self.imagePUP.append(pygame.transform.scale(pygame.image.load(os.path.join('img', 'powerUp_HealthMax_v4.png')), (TILEDIMX, TILEDIMY)))

        self.imageIterState = 0
        self.imageWaitNextImage = 5
        self.imageIterWait = 0

    def update(self):

        self.imageIterWait += 1
        if self.imageIterWait >= self.imageWaitNextImage:
            self.imageIterState = (self.imageIterState+1) % len(self.imagePUP)
            self.image = self.imagePUP[self.imageIterState]
            self.imageIterWait = 0