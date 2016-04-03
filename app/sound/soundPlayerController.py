import pygame
import os

class soundPlayerController():
    def __init__(self):
        self.jumpSound = pygame.mixer.Sound(os.path.join('sample', 'jump2.wav'))
        self.maxHealthPowerupSound = pygame.mixer.Sound(os.path.join('sample', 'maxhealthpowerup.wav'))
        self.healthPowerupSound = pygame.mixer.Sound(os.path.join('sample', 'healthpowerup.wav'))
        self.hurtSound = pygame.mixer.Sound(os.path.join('sample', 'hit_hurt.wav'))
        self.shootSound = pygame.mixer.Sound(os.path.join('sample', 'shoot.wav'))

    def update(self):
        pass

    def jump(self):
        self.jumpSound.play()

    def maxHealthPowerup(self):
        self.maxHealthPowerupSound.play()

    def healthPowerup(self):
        self.healthPowerupSound.play()

    def hurt(self):
        self.hurtSound.play()

    def shoot(self):
        self.shootSound.play()

    def updateSpeedRight(self):
        pass


    def updateSpeedLeft(self):
        pass


    def updateSpeedUp(self):
        pass


    def updateSpeedDown(self):
        pass