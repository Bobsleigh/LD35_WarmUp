import pygame
from app.event.eventHandlerGen import *

class EventHandlerGameOverScene(EventHandlerGen):
    def __init__(self):
        super().__init__()

    def handleKeydown(self, key):
        if key == pygame.K_SPACE:
            self.sceneRunning = False