import pygame

from app.drawing.drawer import Drawer
from app.event.eventHandlerFactory import EventHandlerFactory

class ScreenGen:
    def __init__(self, screen):

        # Écran
        self.screen = screen
        self.screenType = type(self)

        # Trucs dans le game
        self.allSprites = pygame.sprite.Group()

        # Handler
        self.eventHandlerFactory = EventHandlerFactory()
        self.eventHandler = self.eventHandlerFactory.create(self.screenType)
        self.drawer = Drawer()

    def mainLoop(self):
        sceneRunning = True
        while sceneRunning:
            self.eventHandler.handle()
            sceneRunning = self.eventHandler.sceneRunning
            self.drawer.draw(self.screen, self.allSprites)