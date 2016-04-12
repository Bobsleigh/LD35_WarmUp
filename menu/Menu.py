import pygame

from menu.Option import *
from menu.EventHandlerMenu import *
from menu.Selector import *
from app.settings import *

class Menu():
    def __init__(self,dimension):

        # Menu center
        self.x = dimension.left
        self.y = dimension.top

        # Menu dimension
        self.menuWidth = dimension.width
        self.menuHeight = dimension.height

        # Menu list
        self.optionList = []
        self.eventHandler = EventHandlerMenu()

        #All sprite
        self.spritesMenu = pygame.sprite.Group()

    def addOption(self,name,method):
        self.optionList.append(Option(name,method))
        self.createMenu()

    def createMenu(self):

        # Default select opt. 1
        self.optionList[0].isSelected = True
        self.optionList[0].setOptionStyle()

        # Mecanics.
        self.optNum = len(self.optionList)
        self.setOptionSize()
        self.selector = Selector(self.optNum)

        # Add to sprite
        for option in self.optionList:
            self.spritesMenu.add(option)


    def setOptionSize(self):
        # Button real space
        spaceWidth = self.menuWidth
        spaceHeight = self.menuHeight / (self.optNum)

        for option in self.optionList:
            option.image = pygame.Surface([spaceWidth*0.9,spaceHeight*0.7])
            option.rect = option.image.get_rect()

            count = self.optionList.index(option)
            option.rect.x = self.x-spaceWidth*0.45
            option.rect.y = self.y+self.menuHeight*(2*count-self.optNum)/(2*self.optNum)+spaceHeight*0.15

            option.button = option.rect.inflate(-option.image.get_height()*0.2,-option.image.get_height()*0.2)
            option.button.x = option.image.get_height()*0.1
            option.button.y = option.image.get_height()*0.1

            option.textPos =[(option.image.get_width()-option.name.get_width())*0.5,(option.image.get_height()-option.name.get_height())*0.5]

