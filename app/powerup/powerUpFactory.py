from app.powerup.powerUp_HealthMax import PowerUp_HealthMax
from app.powerup.powerUp_Health import PowerUp_Health

class PowerUpFactory:
    def __init__(self):
        pass

    def create(self, powerUp):
        if powerUp.name == "powerUp_HealthMax":
            return self.createPowerUp_HealthMax(powerUp)
        if powerUp.name == "powerUp_Health":
            return self.createPowerUp_Health(powerUp)

    def createPowerUp_HealthMax(self, powerUp):
        return PowerUp_HealthMax(powerUp.x, powerUp.y)

    def createPowerUp_Health(self, powerUp):
        return PowerUp_Health(powerUp.x, powerUp.y)