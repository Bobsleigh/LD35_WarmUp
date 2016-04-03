from app.enemy.enemy_noob import Enemy_noob
from app.enemy.enemyFlyingCircle import EnemyFlyingCircle
from app.enemy.enemyShooter import EnemyShooter

class EnemyFactory:
    def __init__(self):
        pass

    def create(self, enemy, theMap=None):
        if enemy.name == "enemy_noob":
            return self.createEnemyNoob(enemy)
        if enemy.name == "enemyFlyingCircle":
            return self.createEnemyFlyingCircle(enemy)
        if enemy.name == "enemyShooter":
            return self.createEnemyShooter(enemy, theMap)


    def createEnemyNoob(self, enemy):
        direction = self.seekAtt(enemy, "direction")
        distanceMax = self.seekAtt(enemy, "distanceMax")

        enemyCreated = Enemy_noob(enemy.x, enemy.y)

        if direction:
            enemyCreated.setDirection(direction)
        if distanceMax:
            enemyCreated.setDistanceMax(int(distanceMax))
        return enemyCreated

    def createEnemyShooter(self, enemy, theMap):
        direction = self.seekAtt(enemy, "direction")
        if direction is None:
            return EnemyShooter(enemy.x, enemy.y, theMap)
        else:
            return EnemyShooter(enemy.x, enemy.y, theMap, direction)

    def createEnemyFlyingCircle(self, enemy):

        radius = self.seekAtt(enemy, "radius")
        angleDir = self.seekAtt(enemy, "angleDirection")

        enemyCreated = EnemyFlyingCircle(enemy.x, enemy.y)

        if radius:
            enemyCreated.setRadius(int(radius))
        if angleDir:
            enemyCreated.setAngleDirection(int(angleDir))
        return enemyCreated



    def seekAtt(self, object, nameAtt):
        try:
            return getattr(object, nameAtt)
        except AttributeError:
            return None
