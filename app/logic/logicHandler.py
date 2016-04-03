from app.map.gamedata import GameData
from app.bullet import *

class LogicHandler:
    def __init__(self):
        self.sceneRunning = True
        self.endState = None
        self.collisionChecker = CollisionPlayer()
        self.spawmPointPlayerx = 0
        self.spawmPointPlayery = 0
        self.newMap = None

    def handle(self, player,gameData, mapMemory):
        self.applyGravity(gameData.allSprites)
        self.applyFriction(gameData.allSprites)
        self.handleCollision(player, gameData, mapMemory)
        self.handleBullets(gameData, player)
        newMap = self.handleObjectCollision(player, gameData)
        self.gameOverCondition(player, gameData)

        gameData.allSprites.update()

        return newMap

    def handleCollision(self,player, gameData, mapMemory):
        self.collisionChecker.collisionAllSprites(player, gameData, mapMemory)

    def handleBottomCollision(self, sprites):
        for sprite in sprites:
            if sprite.rect.y + sprite.rect.height > SCREEN_HEIGHT:
                sprite.rect.y = SCREEN_HEIGHT - sprite.rect.height
                sprite.speedy = 0
                sprite.jumpState = GROUNDED

    def applyGravity(self, allSprites):
        for sprite in allSprites:
            if sprite.isPhysicsApplied == True or sprite.isGravityApplied == True:
                sprite.speedy += GRAVITY

    def applyFriction(self, allSprites):
        for sprite in allSprites:
            if sprite.isPhysicsApplied == True or sprite.isFrictionApplied == True:
                pass
                if sprite.speedx > 0 and sprite.speedx - FRICTION > 0:
                    sprite.speedx -= FRICTION
                elif sprite.speedx > 0:
                    sprite.speedx = 0

                if sprite.speedx < 0 and sprite.speedx + FRICTION < 0:
                    sprite.speedx += FRICTION
                elif sprite.speedx < 0:
                    sprite.speedx = 0

    def handleObjectCollision(self, player, map):

        for object in map.tmxData.objects:
            if self.isPlayerIsInObject(player, object) == True:
                if object.type == "out_zone":
                    tuple = map.reqNameAndPositionNewMap(object.name, player)

                    nameNewMap = tuple[0]

                    self.spawmPointPlayerx = tuple[1]
                    self.spawmPointPlayery = tuple[2]
                    self.newMap = GameData(nameNewMap)

                elif object.type == "finish_zone" and player.lifeMax == player.lifeMaxCap:
                    player.changeCircle()
                    self.sceneRunning = False
                    self.endState = WIN


    def isPlayerIsInObject(self, player, object):

        if player.rect.centerx  >= object.x and \
           player.rect.centerx <= object.x + object.width and \
           player.rect.centery >= object.y and \
           player.rect.centery <= object.y + object.height:
           return True
        else:
           return False

    def handleBullets(self, gameData, player):
        for bullet in gameData.friendlyBullet:
            if type(bullet) == Bullet:
                collisionBulletWall(bullet, gameData)
                collisionBulletEnemy(bullet, gameData)
        for bullet in gameData.enemyBullet:
            if type(bullet) == Bullet:
                collisionBulletWall(bullet, gameData)
        collisionBulletPlayer(gameData, player)

    def gameOverCondition(self, player, gameData):
        if player.life <= 0:
            self.gameOver(player, gameData)

    def gameOver(self, player, map):
        self.sceneRunning = False
        self.endState = GAME_OVER