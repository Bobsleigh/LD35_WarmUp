#Imports
import pygame

from app.event.EventHandlerPauseMenu import EventHandlerPauseMenu
from app.menu.Menu import Menu
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
            self.eventHandler.eventHandle(self.menuPause.optionList, self.menuPause.selector, self.close)
            self.menuPause.spritesMenu.update()  # This would be in the logic
            self.draw()  # Drawer in THIS file, below

    def draw(self):
        self.menuPause.spritesMenu.draw(self.screen)

        pygame.display.flip()

    def close(self):
        self.menuRunning = False
