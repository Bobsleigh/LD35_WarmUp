#Imports
import pygame
from app.settings import *


#Objets
class Option(pygame.sprite.Sprite):
    def __init__(self,name,method):
        super().__init__()

        self.optFont = pygame.font.SysFont('arial', 30)
        self.name = self.optFont.render(name, True, (0, 0, 0))
        self.button = pygame.Rect(0,0,0,0)
        self.isSelected = False
        self.method = method
        self.soundSelect = pygame.mixer.Sound('menu/sound/menu_select.wav')
        self.soundChange = pygame.mixer.Sound('menu/sound/menu_change.wav')

        #Color
        self.color1 = COLOR_MENU_1
        self.color2 = COLOR_MENU_2

    def update(self):
        pass

    def select(self):
        self.isSelected = True
        self.soundChange.play(0)
        self.setOptionStyle()

    def deselect(self):
        self.isSelected = False
        self.setOptionStyle()

    def doOption(self):
        self.soundSelect.play(0)
        self.method()

    def setOptionStyle(self):
        if self.isSelected:
            self.color1 = COLOR_MENU_SELECT_1
            self.color2 = COLOR_MENU_SELECT_2
        else:
            self.color1 = COLOR_MENU_1
            self.color2 = COLOR_MENU_2


