#Imports
from pygame import init,display,Rect,mixer,time,font

from menu.Menu import Menu
from app.game import Game

from app.settings import *

class TitleScreen():
    def __init__(self, screen):
        menuOption = Menu(screen, Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 3, SCREEN_HEIGHT * 2 / 6))
        menuOption.addOption('Sound', game.mainLoop)
        menuOption.addOption('Sound Effect', game.mainLoop)

        menu = Menu(screen, Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4, SCREEN_WIDTH / 3, SCREEN_HEIGHT * 2 / 6))
        menu.addOption('Start', game.mainLoop)
        menu.addOption('Option', menuOption.mainLoop)
        menu.addOption('Credit', game.mainLoop)
        menu.addOption('Exit', quit)

        menuOption.addOption('Back', menuOption.close)

        menu.mainLoop()