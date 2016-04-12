import pygame
from sys import exit

class EventHandlerGen():
    def __init__(self):
        self.sceneRunning = True

    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.handleKeydown(event.key)
            if event.type == pygame.QUIT:
                self.handleQuit()

    def handleQuit(self):
        exit()

    def handleKeydown(self, key):
        if key == pygame.K_SPACE:
            pass