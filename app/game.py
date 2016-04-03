from app.drawing.drawerGame import DrawerGame
from app.logic.logicHandler import LogicHandler
from app.event.eventHandlerFactory import EventHandlerFactory

from app.player import Player
from app.map.gamedata import MapData
from app.map.mapMemory import MapMemory


class Game():
    def __init__(self, screen):
        # Écran
        self.screen = screen
        self.screenType = type(self)

        #Map : HardCoded
        self.gameData = MapData("Map_01")
        self.mapMemory = MapMemory()
        self.mapMemory.enteringMap(self.gameData)

        # TODO: See where to put player. In gameData? But he will reset with each map change..?
        self.player = Player(540, 445)

        self.gameData.allSprites.add(self.player)
        self.gameData.camera.add(self.player)
        self.camera = self.gameData.camera

        # Handler
        self.eventHandlerFactory = EventHandlerFactory()
        self.eventHandlerFactory.setPlayer(self.player)
        self.eventHandlerGame = self.eventHandlerFactory.create(self.screenType, self.camera, self.gameData)
        self.logicHandler = LogicHandler(self.gameData)
        self.drawer = DrawerGame()

        self.endState = None

    def mainLoop(self):
        sceneRunning = True
        while sceneRunning:
            self.eventHandlerGame.handle()
            sceneRunning = self.eventHandlerGame.sceneRunning and self.logicHandler.sceneRunning

            self.logicHandler.handle(self.player, self.mapMemory)
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
            self.eventHandlerGame.eventHandlerPlayer.soundControllerPlayer = self.gameData.soundController

            self.logicHandler.gameData = self.gameData
            self.logicHandler.collisionChecker.soundControl = self.gameData.soundController
            self.logicHandler.newMap = None
