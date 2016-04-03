import pygame
from app.drawing.drawerGame import DrawerGame
from app.logic.logicHandler import LogicHandler
from app.event.eventHandlerFactory import EventHandlerFactory

from menu.Menu import Menu

from app.settings import *
from app.player import Player
from app.map.gamedata import MapData
from app.map.gameMemory import GameMemory


class Game:
    def __init__(self, screen):
        # Écran
        self.screen = screen
        self.screenType = type(self)

        #Map : HardCoded
        self.mapData = MapData("Map_01")
        self.gameMemory = GameMemory()
        self.gameMemory.enteringMap(self.mapData)

        # TODO: See where to put player. In mapData? But he will reset with each map change..?
        self.player = Player(540, 445)

        self.mapData.allSprites.add(self.player)
        self.mapData.camera.add(self.player)
        self.camera = self.mapData.camera



        # Handler
        self.eventHandlerFactory = EventHandlerFactory()
        self.eventHandlerFactory.setPlayer(self.player)
        self.eventHandlerGame = self.eventHandlerFactory.create(self.screenType, self.camera, self.mapData)
        self.logicHandler = LogicHandler(self.mapData)
        self.drawer = DrawerGame()

        self.endState = None

        #Menu
        self.menuPause = Menu(self.screen, pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3.5))
        self.menuPause.addOption('Resume',self.menuPause.close)
        self.menuPause.addOption('Back to Main Menu', self.backToMain)
        self.menuPause.addOption('Exit', self.eventHandlerGame.handleQuit)
        self.eventHandlerGame.menuPause = self.menuPause


    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandlerGame.handle()
            self.sceneRunning = self.eventHandlerGame.sceneRunning and self.logicHandler.sceneRunning

            self.logicHandler.handle(self.player, self.gameMemory)
            self.checkNewMap(self.logicHandler.newMap)

            self.drawer.draw(self.screen, self.mapData.camera, self.mapData.spritesHUD, self.player)

        self.endState = self.logicHandler.endState


    def checkNewMap(self, newMap):
        if newMap is not None:
            self.changeMap(newMap)

    def changeMap(self, newMap):

            self.player.rect.x = self.logicHandler.spawmPointPlayerx
            self.player.rect.y = self.logicHandler.spawmPointPlayery

            self.mapData = newMap
            self.mapData.allSprites.add(self.player)
            self.mapData.camera.add(self.player)

            self.gameMemory.enteringMap(self.mapData)
            self.gameMemory.updateMap(self.mapData)

            self.eventHandlerGame.newMap(self.mapData)
            self.eventHandlerGame.eventHandlerPlayer.soundControllerPlayer = self.mapData.soundController

            self.logicHandler.mapData = self.mapData
            self.logicHandler.collisionChecker.soundControl = self.mapData.soundController
            self.logicHandler.newMap = None

    def close(self):
        self.eventHandlerGame.sceneRunning = False

    def backToMain(self):
        self.menuPause.close()
        self.close()