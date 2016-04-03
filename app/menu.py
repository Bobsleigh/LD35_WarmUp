import pygame

from app.screenGen import ScreenGen
from app.settings import *
import os


class Menu(ScreenGen):
    def __init__(self, screen):
        super().__init__(screen)


        # Trucs dans le screen
        self.monFont = pygame.font.SysFont('comicsansms', 36)
        self.surface1 = self.monFont.render("PRESS SPACE TO BEGIN", False, RED)
        self.maSurfaceSprite = pygame.sprite.Sprite()
        self.maSurfaceSprite.image = self.surface1
        self.maSurfaceSprite.rect = self.maSurfaceSprite.image.get_rect()
        self.maSurfaceSprite.rect.centerx = SCREEN_WIDTH/2
        self.maSurfaceSprite.rect.centery = SCREEN_HEIGHT-60

        self.titleSprite = pygame.sprite.Sprite()
        self.titleSprite.image = pygame.image.load(os.path.join('img', 'titlescreen.png'))
        self.titleSprite.rect = self.maSurfaceSprite.image.get_rect()
        self.titleSprite.rect.x = 0
        self.titleSprite.rect.y = 0
        self.titleSprite.image.set_colorkey(WHITE)

        self.spritesHUD = pygame.sprite.Group()

        self.allSprites.add(self.maSurfaceSprite,self.titleSprite)
