
import pygame
from app.settings import *

class EventHandlerPlayer():
    def __init__(self, player, soundControllerPlayer):
        self.player = player
        self.soundControllerPlayer = soundControllerPlayer

        self.leftPressed = False
        self.rightPressed = False
        self.upPressed = False
        self.downPressed = False

    def handleKeydown(self, key):

        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.player.updateSpeedRight()
            self.rightPressed = True
        if key == pygame.K_LEFT or key == pygame.K_a:
            self.player.updateSpeedLeft()
            self.leftPressed = True
        if key == pygame.K_UP or key == pygame.K_w:
            self.player.updateSpeedUp()
            self.upPressed = True
        if key == pygame.K_DOWN or key == pygame.K_s:
            self.player.updateSpeedDown()
            self.downPressed = True
        if key == pygame.K_SPACE:
            if not self.player.shape == SQUARE:
                jumpState1 = self.player.jumpState
                self.player.jump()
                jumpState2 = self.player.jumpState
                if jumpState1 != jumpState2:
                    self.soundControllerPlayer.jump()
            elif self.player.shape == SQUARE:
                if self.player.jumpState != GROUNDED:
                    if (self.player.specialWallSide == LEFT and self.player.wallJumpLeftAllowed and not self.player.jumpState == GROUNDED) or (self.player.specialWallSide == RIGHT and self.player.wallJumpRightAllowed and not self.player.jumpState == GROUNDED):
                        self.soundControllerPlayer.jump()
                    self.player.wallJump()
                jumpState1 = self.player.jumpState
                self.player.jump()
                jumpState2 = self.player.jumpState
                if jumpState1 != jumpState2:
                    self.soundControllerPlayer.jump()

        if key == pygame.K_LSHIFT:
            self.player.special()
            if self.player.shape == PENTAGON:
                self.soundControllerPlayer.shoot()
        if key == pygame.K_1:
            self.player.changeTriangle()
        elif key == pygame.K_2:
            self.player.changeSquare()
        elif key == pygame.K_3:
            self.player.changePentagon()
        elif key == pygame.K_4:
            self.player.changeHexagon()
        elif key == pygame.K_5:
            self.player.changeCircle()

    def handleKeyup(self, key):
        if key == pygame.K_RIGHT or key == pygame.K_d:
            self.rightPressed = False
        if key == pygame.K_LEFT or key == pygame.K_a:
            self.leftPressed = False

    def handle(self):
        if self.rightPressed:
            self.player.updateSpeedRight()
        if self.leftPressed:
            self.player.updateSpeedLeft()