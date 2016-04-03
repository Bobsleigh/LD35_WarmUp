from app.drawing.drawerGame import DrawerGame
from app.logic.logicHandler import LogicHandler
from app.event.eventHandlerFactory import EventHandlerFactory

from menu.Menu import Menu

from app.player import Player
from app.map.gamedata import GameData
from app.settings import *
from app.map.mapMemory import MapMemory
import pyscroll
import pygame

class Game():
    def __init__(self, screen):
        # Écran
        self.screen = screen
        self.screenType = type(self)

        #Map : HardCoded
        self.gameData = GameData("Map_01")
        self.mapMemory = MapMemory()
        self.mapMemory.enteringMap(self.gameData)

        # TODO: See where to put player. In gameData? But he will reset with each map change..?
        self.player = Player(540, 445)

        self.gameData.allSprites.add(self.player)
        self.gameData.camera.add(self.player)
        self.camera = self.gameData.camera

        #Menu
        self.menuPause = Menu(self.screen, pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 3, SCREEN_HEIGHT / 4))
        self.menuPause.addOption('Resume',self.menuPause.close)
        self.menuPause.addOption('Back to Main Menu', self.backToMain)


        # Handler
        self.eventHandlerFactory = EventHandlerFactory()
        self.eventHandlerFactory.setPlayer(self.player)
        self.eventHandlerGame = self.eventHandlerFactory.create(self.screenType, self.camera, self.gameData)
        self.logicHandler = LogicHandler()
        self.drawer = DrawerGame()

        self.endState = None

    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandlerGame.handle()
            sceneRunning = self.eventHandlerGame.sceneRunning and self.logicHandler.sceneRunning

            self.logicHandler.handle(self.player, self.gameData, self.mapMemory)
            self.checkNewMap(self.logicHandler.newMap)

            self.drawer.draw(self.screen, self.gameData.camera, self.gameData.spritesHUD, self.player)

        self.endState = self.logicHandler.endState

    def checkNewMap(self, newMap):
        if newMap is not None:
            self.changeMap(newMap)

    def changeMap(self, newMap):
            self.player.rect.x = self.logicHandler.spawmPointPlayerx
            self.player.rect.y = self.logicHandler.spawmPointPlayery
            self.gameData = newMap
            self.gameData.allSprites.add(self.player)
            self.gameData.camera.add(self.player)
            self.mapMemory.enteringMap(self.gameData)
            self.mapMemory.updateMap(self.gameData)
            self.eventHandlerGame.newMap(self.gameData)
            self.logicHandler.newMap = None

    def close(self):
        self.scenerunning = False

    def backToMain(self):
        self.menuPause.close()
        self.close()