#Imports
import os

import pygame

from app.event.EventHandlerTitleScreen import EventHandlerTitleScreen
from app.menu.Menu import Menu
from app.settings import *
from app.tools.functionTools import quitGame

class TitleScreen():
    def __init__(self, screen):

        self.screen = screen

        titleMenu = pygame.image.load(os.path.join('img', 'titlescreen.png'))
        self.screen.blit(titleMenu, (0,0))

        #Define MainMenu
        self.menu = Menu(pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 13 / 16, SCREEN_WIDTH / 3, SCREEN_HEIGHT * 0.25))
        self.menu.addOption('Start', self.close)
        self.menu.addOption('Exit', quitGame)

        self.eventHandler = EventHandlerTitleScreen()

        self.nextScene = None

    def mainLoop(self):
        self.menuRunning = True
        while self.menuRunning:
            self.eventHandler.eventHandle(self.menu.optionList, self.menu.selector)
            self.menu.spritesMenu.update() #This would be in the logic
            self.draw() #Drawer in THIS file, below


    def draw(self):

        self.menu.spritesMenu.draw(self.screen)

        pygame.display.flip()


    def close(self):
        self.nextScene = GAME
        self.menuRunning = False