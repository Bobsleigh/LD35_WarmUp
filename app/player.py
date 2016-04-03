import pygame
import os

from app.settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.name = "player"

        self.imageEdge_v1 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_edge_v1.png')), (TILEDIMX, TILEDIMY))
        self.imageEdge_v2 = self.imageEdge_v1
        self.imageTriangle_v1 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_triangle_v1.png')), (TILEDIMX, TILEDIMY))
        self.imageTriangle_v2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_triangle_v2.png')), (TILEDIMX, TILEDIMY))
        self.imageSquare_v1 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_square_v1.png')), (TILEDIMX, TILEDIMY))
        self.imageSquare_v2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_square_v2.png')), (TILEDIMX, TILEDIMY))
        self.imagePentagon_v1 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_pentagon_v1.png')), (TILEDIMX, TILEDIMY))
        self.imagePentagon_v2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_pentagon_v2.png')), (TILEDIMX, TILEDIMY))
        self.imageHexagon_v1 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_hexagon_v1.png')), (TILEDIMX, TILEDIMY))
        self.imageHexagon_v2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_hexagon_v2.png')), (TILEDIMX, TILEDIMY))
        self.imageCircle_v1 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_circle_v1.png')), (TILEDIMX, TILEDIMY))
        self.imageCircle_v2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_circle_v2.png')), (TILEDIMX, TILEDIMY))
        self.imageTransparent = pygame.image.load(os.path.join('img', 'player_transparent.png'))

        self.image = self.imageTriangle_v1

        self.imageShapeRight = self.imageTriangle_v1
        self.imageShapeLeft = self.imageTriangle_v2

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #To dodge rounding problems with rect
        self.x = x
        self.y = y
        self.pastFrameX = x
        self.pastFrameY = y

        self.speedx = 0
        self.speedy = 0
        self.maxSpeedx = 8
        self.maxSpeedyUp = 40
        self.maxSpeedyDown = 10
        self.accx = 2
        self.accy = 2
        self.jumpSpeed = -15

        self.isPhysicsApplied = True
        self.jumpState = JUMP
        self.specialState = IDLE
        self.facingSide = RIGHT
        self.specialWallSide = IDLE
        self.wallJumpLeftAllowed = True
        self.wallJumpRightAllowed = True

        self.shape = TRIANGLE

        self.life = 1
        self.lifeMax = 1
        self.lifeMaxCap = 5
        self.isInvincible = False
        self.invincibleFrameCounter = 0
        self.invincibleFrameDuration = 60

    def update(self):
        self.capSpeed()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.speedx > 0:
            self.image = self.imageShapeRight
            self.facingSide = RIGHT
        if self.speedx < 0:
            self.image = self.imageShapeLeft
            self.facingSide = LEFT

        self.invincibleUpdate()

    def capSpeed(self):
        if self.speedx > 0 and self.speedx > self.maxSpeedx:
            self.speedx = self.maxSpeedx
        if self.speedx < 0 and self.speedx < -self.maxSpeedx:
            self.speedx = -self.maxSpeedx
        if self.speedy > 0 and self.speedy > self.maxSpeedyDown:
            self.speedy = self.maxSpeedyDown
        if self.speedy < 0 and self.speedy < -self.maxSpeedyUp:
            self.speedy = -self.maxSpeedyUp

        if self.specialState == DASH and self.facingSide == RIGHT:
                self.speedx = +100
                if self.jumpState == JUMP or self.jumpState == DOUBLE_JUMP:
                    self.specialState = COOLDOWN
                else:
                    self.specialState = IDLE
        if self.specialState == DASH and self.facingSide == LEFT:
                self.speedx = -100
                self.specialState = COOLDOWN
                if self.jumpState == JUMP:
                    self.specialState = COOLDOWN
                else:
                    self.specialState = IDLE

    def jump(self):
        if self.jumpState == GROUNDED:
            self.speedy = self.jumpSpeed
            self.jumpState = JUMP
        elif self.jumpState == JUMP and self.shape == CIRCLE:
            self.speedy = self.jumpSpeed
            self.jumpState = DOUBLE_JUMP

    def special(self):
        if self.shape == HEXAGON and not self.specialState == COOLDOWN:
            self.specialState = DASH
            if self.facingSide == RIGHT:
                self.speedx = +100
            elif self.facingSide == LEFT:
                self.speedx = -100
        elif self.shape == HEXAGON:
            pass

    def updateSpeedRight(self):
        self.speedx += self.accx

    def updateSpeedLeft(self):
        self.speedx -= self.accx

    def updateSpeedUp(self):
        self.speedy -= self.accy

    def updateSpeedDown(self):
        self.speedy += self.accy

    def changeImageShape(self):
            if self.facingSide == RIGHT:
                self.image = self.imageShapeRight
            else:
                self.image = self.imageShapeLeft

    def changeEdge(self):
        if self.life >= 0:
            self.shape = EDGE
            self.imageShapeRight = self.imageEdge_v1
            self.imageShapeLeft = self.imageEdge_v2
            self.changeImageShape()

    def changeTriangle(self):
        if self.life >= 1:
            self.shape = TRIANGLE
            self.imageShapeRight = self.imageTriangle_v1
            self.imageShapeLeft = self.imageTriangle_v2
            self.changeImageShape()

    def changeSquare(self):
        if self.life >= 2:
            self.shape = SQUARE
            self.imageShapeRight = self.imageSquare_v1
            self.imageShapeLeft = self.imageSquare_v2
            self.changeImageShape()

    def changePentagon(self):
        if self.life >= 3:
            self.shape = PENTAGON
            self.imageShapeRight = self.imagePentagon_v1
            self.imageShapeLeft = self.imagePentagon_v2
            self.changeImageShape()

    def changeHexagon(self):
        if self.life >= 4:
            self.shape = HEXAGON
            self.imageShapeRight = self.imageHexagon_v1
            self.imageShapeLeft = self.imageHexagon_v2
            self.changeImageShape()

    def changeCircle(self):
        if self.life >= 5:
            self.shape = CIRCLE
            self.imageShapeRight = self.imageCircle_v1
            self.imageShapeLeft = self.imageCircle_v2
            self.changeImageShape()

    def downOneShape(self):
        if self.shape == TRIANGLE:
            self.changeEdge()
        elif self.shape == SQUARE:
            self.changeTriangle()
        elif self.shape == PENTAGON:
            self.changeSquare()
        elif self.shape == HEXAGON:
            self.changePentagon()
        elif self.shape == CIRCLE:
            self.changeHexagon()

    def setShapeImage(self):
        if self.shape == EDGE:
            self.changeEdge()
        elif self.shape == TRIANGLE:
            self.changeTriangle()
        elif self.shape == SQUARE:
            self.changeSquare()
        elif self.shape == PENTAGON:
            self.changePentagon()
        elif self.shape == HEXAGON:
            self.changeHexagon()
        elif self.shape == CIRCLE:
            self.changeCircle()

    def upOneShape(self):
        if self.shape == TRIANGLE:
            self.changeSquare()
        elif self.shape == SQUARE:
            self.changePentagon()
        elif self.shape == PENTAGON:
            self.changeHexagon()
        elif self.shape == HEXAGON:
            self.changeCircle()
        elif self.shape == CIRCLE:
            pass

    def setShapeMax(self):
        if self.lifeMax == 0:
            self.changeEdge()
        if self.lifeMax == 1:
            self.changeTriangle()
        elif self.lifeMax == 2:
            self.changeSquare()
        elif self.lifeMax == 3:
            self.changePentagon()
        elif self.lifeMax == 4:
            self.changeHexagon()
        elif self.lifeMax == 5:
            self.changeCircle()

    def loseLifeChangeShape(self):
        if self.shape == self.life:
            self.downOneShape()

    def gainLife(self):
        if self.life < self.lifeMax:
            self.life = self.lifeMax
            self.setShapeMax()

    def loseLife(self):
        if not self.isInvincible:
            if self.life > 1:
                self.loseLifeChangeShape()
                self.life -= 1
                self.invincibleOnHit()
                self.visualFlash()
            elif self.life > 0:
                self.loseLifeChangeShape()
                self.life -= 1


    def gainLifeMax(self):
        if self.lifeMax < self.lifeMaxCap:
            self.lifeMax += 1
            self.life = self.lifeMax
            self.setShapeMax()
        else:
            self.lifeMax = self.lifeMaxCap
            self.life = self.lifeMax
            self.setShapeMax()


    def knockedback(self):
        #Can break collision ATM
        if self.speedx == 0:
            self.speedx = self.maxSpeedx

        self.speedx = (-self.speedx/abs(self.speedx)) * self.maxSpeedx
        self.speedy = (-self.speedy/abs(self.speedx)) * self.maxSpeedx

    def invincibleOnHit(self):
        self.isInvincible = True
        self.invincibleFrameCounter = 1
        # self.visualFlash()

    def invincibleUpdate(self):
        if self.invincibleFrameCounter > 0 and self.invincibleFrameCounter < self.invincibleFrameDuration:
            self.invincibleFrameCounter += 1
        elif self.invincibleFrameCounter == self.invincibleFrameDuration:
            self.isInvincible = False
            self.invincibleFrameCounter = 0
        self.visualFlash()

    def dead(self):
        self.life = 0
        self.changeEdge()

    def pickedPowerUpMaxHealth(self):
        self.gainLifeMax()

    def pickedPowerUpHealth(self):
        self.gainLife()

    def visualFlash(self):
        if self.invincibleFrameCounter == 1:
            self.imageShapeRight = self.imageTransparent
            self.imageShapeLeft = self.imageTransparent
            self.image = self.imageTransparent
        elif self.invincibleFrameCounter == 5:
            self.setShapeImage()
        elif self.invincibleFrameCounter == 15:
            self.imageShapeRight = self.imageTransparent
            self.imageShapeLeft = self.imageTransparent
            self.image = self.imageTransparent
        elif self.invincibleFrameCounter == 20:
            self.setShapeImage()
        elif self.invincibleFrameCounter == 30:
            self.imageShapeRight = self.imageTransparent
            self.imageShapeLeft = self.imageTransparent
            self.image = self.imageTransparent
        elif self.invincibleFrameCounter == 35:
            self.setShapeImage()
        elif self.invincibleFrameCounter == 45:
            self.imageShapeRight = self.imageTransparent
            self.imageShapeLeft = self.imageTransparent
            self.image = self.imageTransparent
        elif self.invincibleFrameCounter == 50:
            self.setShapeImage()

    def wallJump(self):
        if self.shape == SQUARE and self.specialState == WALL_HUGGING:
            if self.specialWallSide == LEFT and self.wallJumpLeftAllowed and not self.jumpState == GROUNDED:
                self.speedy = self.jumpSpeed
                self.speedx = 8
                self.jumpState = JUMP
                self.wallJumpLeftAllowed = False
                self.wallJumpRightAllowed = True
            elif self.specialWallSide == RIGHT and self.wallJumpRightAllowed and not self.jumpState == GROUNDED:
                self.speedy = self.jumpSpeed
                self.speedx = -8
                self.jumpState = JUMP
                self.wallJumpRightAllowed = False
                self.wallJumpLeftAllowed = True

