from app.event.eventHandlerMenu import EventHandlerMenu
from app.event.eventHandlerGame import EventHandlerGame
from app.event.eventHandlerPlayer import EventHandlerPlayer
from app.event.eventHandlerGameOverScene import EventHandlerGameOverScene

from app.sound.soundGameController import soundGameController

class EventHandlerFactory:
    def __init__(self):
        self.player = None

    def createEventHandlerMenu(self):
        return EventHandlerMenu()

    def createEventHandlerGame(self, player, mapData):

        return EventHandlerGame(player, EventHandlerPlayer(player, mapData.soundController), soundGameController(), mapData)

    def createEventHandlerGameOverScene(self):
        return EventHandlerGameOverScene()

    def create(self, screenType, camera = None, mapData=None):
        from app.menu import Menu
        from app.game import Game
        from app.gameOverScene import GameOverScene
        from app.winScene import WinScene

        if screenType == Menu:
            return self.createEventHandlerMenu()
        if screenType == Game:
            return self.createEventHandlerGame(self.player, mapData)
        if screenType == GameOverScene:
            return self.createEventHandlerGameOverScene()
        if screenType == WinScene:
            return self.createEventHandlerGameOverScene()

    def setPlayer(self, player):
        self.player = player