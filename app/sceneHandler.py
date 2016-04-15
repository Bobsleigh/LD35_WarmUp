__author__ = 'Bobsleigh'

from app.settings import *
from app.game import Game
from app.gameOverScene import GameOverScene
from app.winScene import WinScene
from app.TitleScreen import TitleScreen


class SceneHandler():
    def __init__(self, screen, firstScene):

        self.handlerRunning = True
        self.runningScene = firstScene
        self.screen = screen

    def mainLoop(self):
        self.handlerRunning = True
        while self.handlerRunning:
            self.runningScene.mainLoop()

            #When we exit the scene, this code executes
            if self.runningScene.nextScene == GAME:
                self.runningScene = Game(self.screen)
            elif self.runningScene.nextScene == GAME_OVER:
                self.runningScene = GameOverScene(self.screen)
                self.handlerRunning = False
                self.runningScene.mainLoop()
            elif self.runningScene.nextScene == WIN:
                self.runningScene = WinScene(self.screen)
                self.handlerRunning = False
                self.runningScene.mainLoop()
            elif self.runningScene.nextScene == TITLE_SCREEN:
                self.runningScene = TitleScreen(self.screen)
                self.runningScene.mainLoop()

