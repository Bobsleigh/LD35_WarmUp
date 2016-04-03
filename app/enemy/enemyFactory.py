from app.enemy.enemy_noob import Enemy_noob
from app.enemy.enemyFlyingCircle import EnemyFlyingCircle
from app.enemy.enemyShooter import EnemyShooter
from app.tools.functionTools import *


class EnemyFactory:
    def __init__(self):
        pass

    def create(self, enemy, theMap=None):
        eName = seekAtt(enemy, "name")
        if eName == "enemy_noob":
            return self.createEnemyNoob(enemy)
        if eName == "enemyFlyingCircle":
            return self.createEnemyFlyingCircle(enemy)
        if eName == "enemyShooter":
            return self.createEnemyShooter(enemy, theMap)


    def createEnemyNoob(self, enemy):
        direction = seekAtt(enemy, "direction")
        distanceMax = seekAtt(enemy, "distanceMax")

        enemyCreated = Enemy_noob(enemy.x, enemy.y)

        if direction:
            enemyCreated.setDirection(direction)
        if distanceMax:
            enemyCreated.setDistanceMax(int(distanceMax))
        return enemyCreated

    def createEnemyShooter(self, enemy, theMap):
        direction = seekAtt(enemy, "direction")
        if direction is None:
            return EnemyShooter(enemy.x, enemy.y, theMap)
        else:
            return EnemyShooter(enemy.x, enemy.y, theMap, direction)

    def createEnemyFlyingCircle(self, enemy):

        radius = seekAtt(enemy, "radius")
        angleDir = seekAtt(enemy, "angleDirection")

        enemyCreated = EnemyFlyingCircle(enemy.x, enemy.y)

        if radius:
            enemyCreated.setRadius(int(radius))
        if angleDir:
            enemyCreated.setAngleDirection(int(angleDir))
        return enemyCreated

