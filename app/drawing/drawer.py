import pygame
from app.settings import *

class Drawer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = FPS


    def draw(self, screen, sprites):
        screen.fill(WHITE)

        sprites.draw(screen)
        pygame.display.flip()
        self.clock.tick(self.FPS)
