#Imports
import pygame

from menu.Menu import Menu

from app.event.EventHandlerPauseMenu import EventHandlerPauseMenu

from app.settings import *

from app.tools.functionTools import quitGame

class MenuPause():
    def __init__(self, screen,backToMain):

        self.screen = screen

        # Menu
        self.menuPause = Menu(self.screen,
                              pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3.5))
        self.menuPause.addOption('Resume', self.close)
        self.menuPause.addOption('Back to Main Menu', backToMain)
        self.menuPause.addOption('Exit', quitGame)

        self.eventHandler = EventHandlerPauseMenu()


    def mainLoop(self):
        self.menuRunning = True
        while self.menuRunning:
            self.draw()
            self.eventHandler.eventHandle(self.menuPause.optionList, self.menuPause.selector, self.close)

    def draw(self):
        self.optionList = self.menuPause.optionList

        count = 0
        while count < self.menuPause.optNum:
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
