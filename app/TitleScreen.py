#Imports
import pygame
from app.screenGen import ScreenGen

from menu.Menu import Menu
from app.game import Game
from sys import exit

import os
from app.settings import *

from app.event.EventHandlerTitleScreen import EventHandlerTitleScreen

from app.tools.functionTools import quitGame

class TitleScreen():
    def __init__(self, screen):

        self.screen = screen

        titleMenu = pygame.image.load(os.path.join('img', 'titlescreen.png'))
        self.screen.blit(titleMenu, (0,0))

        #Define MainMenu
        self.menu = Menu(screen, pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 13 / 16, SCREEN_WIDTH / 3, SCREEN_HEIGHT * 0.25))
        self.menu.addOption('Start', self.close)
        self.menu.addOption('Exit', quitGame)

        self.eventHandler = EventHandlerTitleScreen()

    def mainLoop(self):
        self.menuRunning = True
        while self.menuRunning:
            self.draw()
            self.eventHandler.eventHandle(self.menu.optionList, self.menu.selector)

    def draw(self):
        self.optionList = self.menu.optionList

        count = 0
        while count < self.menu.optNum:
            option = self.optionList[count]

            pygame.draw.rect(self.screen, option.color1,
                      (option.button.left, option.button.top, option.button.width, option.button.height))
            pygame.draw.rect(self.screen, option.color2,
                      (option.button.left, option.button.top, option.button.width, option.button.height), 7)
            self.screen.blit(option.name, option.textPos)

            count += 1

        pygame.display.flip()


    def close(self):
        self.menuRunning = False