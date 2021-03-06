import pygame
import sys
from app.bullet import Bullet
from app.settings import *
from app.event.eventHandlerGen import *

class EventHandlerGame(EventHandlerGen):
    def __init__(self, player, eventHandlerPlayer, musicGameController, mapData):
        super().__init__()
        self.eventHandlerPlayer = eventHandlerPlayer
        self.musicGameController = musicGameController
        self.endState = None
        self.player = player
        self.mapData = mapData
        self.menuPause = None

    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.eventHandlerPlayer.handleKeydown(event.key)
                if event.key == pygame.K_LSHIFT and self.player.shape == PENTAGON:
                    if self.player.facingSide == RIGHT:
                        bullet = Bullet(self.player.rect.x + self.player.rect.width +1, self.player.rect.centery, self.player.facingSide)
                    else:
                        bullet = Bullet(self.player.rect.x -1, self.player.rect.centery, self.player.facingSide)
                    self.mapData.camera.add(bullet)
                    self.mapData.allSprites.add(bullet)
                    self.mapData.friendlyBullet.add(bullet)
                if event.key == pygame.K_BACKSPACE:
                    self.menuPause.mainLoop()
                if event.key == pygame.K_ESCAPE:
                    self.menuPause.mainLoop()

            if event.type == pygame.KEYUP:
                self.eventHandlerPlayer.handleKeyup(event.key)
            if event.type == pygame.QUIT:
                self.handleQuit()

        self.eventHandlerPlayer.handle()

    def newMap(self, mapData):
        self.mapData = mapData
