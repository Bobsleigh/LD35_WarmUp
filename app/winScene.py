
from app.screenGen import ScreenGen
import copy
import os
import pygame
from app.settings import *
from app.drawing.drawerGameOverScene import *

class WinScene(ScreenGen):
    def __init__(self, screen):
        super().__init__(screen)

        self.lastScreenBeforeDeath = copy.deepcopy(screen)

        #GameOverScreen
        self.monFont = pygame.font.Font(os.path.join('fonts', 'FreePixel.ttf'), 60)
        self.monFontSmaller = pygame.font.Font(os.path.join('fonts', 'FreePixel.ttf'), 36)
        self.monFont.set_bold(True)
        self.surface1 = self.monFont.render("CONGRATULATIONS!", False, RED)
        self.surface2 =  self.monFontSmaller.render("You Got Back Home Safely!", False, RED)


        self.maSurfaceSprite = pygame.sprite.Sprite()
        self.maSurfaceSprite.image = self.surface1
        self.maSurfaceSprite.rect = self.maSurfaceSprite.image.get_rect()
        self.maSurfaceSprite.rect.centerx = SCREEN_WIDTH/2
        self.maSurfaceSprite.rect.centery = SCREEN_HEIGHT/2-40

        self.maSurfaceSprite2 = pygame.sprite.Sprite()
        self.maSurfaceSprite2.image = self.surface2
        self.maSurfaceSprite2.rect = self.maSurfaceSprite2.image.get_rect()
        self.maSurfaceSprite2.rect.centerx = SCREEN_WIDTH/2
        self.maSurfaceSprite2.rect.centery = SCREEN_HEIGHT/2+40

        self.allSprites.add(self.maSurfaceSprite2, self.maSurfaceSprite)

        self.drawer = DrawerGameOverScene()