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
        self.menuPause = Menu(
                              pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        self.menuPause.addOption('Resume', self.close)
        self.menuPause.addOption('Back to Main Menu', backToMain)
        self.menuPause.addOption('Exit', quitGame)

        self.eventHandler = EventHandlerPauseMenu()


    def mainLoop(self):
        self.menuRunning = True
        while self.menuRunning:
            self.draw()
            self.menuPause.spritesMenu.update() #Ce serait la logique.
            self.eventHandler.eventHandle(self.menuPause.optionList, self.menuPause.selector, self.close)

    def draw(self):
        self.optionList = self.menuPause.optionList
        self.menuPause.spritesMenu.draw(self.screen)

        pygame.display.flip()

    def close(self):
        self.menuRunning = False
