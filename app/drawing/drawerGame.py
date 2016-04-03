import pygame
from app.settings import *

class DrawerGame:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = FPS

    def draw(self, screen, camera, spritesHUD, player):
        camera.center(player.rect.center)
        camera.draw(screen)
        spritesHUD.draw(screen)
        pygame.display.flip()
        self.clock.tick(self.FPS)