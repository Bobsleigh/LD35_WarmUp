from app.map.mapTemplate import MapTemplate

class GameMemory:
    def __init__(self):
        self.visitedMaps = []
        self.visitedMaps.append(MapTemplate())
        self.currentMapTemplate = None

    def enteringMap(self, map):
        isMapPresent = False
        for mapTemplate in self.visitedMaps:
            if mapTemplate.name == map.nameMap:
                isMapPresent = True
                self.currentMapTemplate = mapTemplate
        if not isMapPresent:
            self.currentMapTemplate = MapTemplate(map.nameMap)
            self.visitedMaps.append(self.currentMapTemplate)

            for powerUp in map.powerUpGroup:
                if powerUp.name == "powerUp_HealthMax":
                    self.currentMapTemplate.powerUpMaxHealthPresent = True

    def updateMap(self, map):
        template = self.findMapTemplate(map)
        if template == None:
            return
        for powerUp in map.powerUpGroup:
            if powerUp.name == "powerUp_HealthMax":
                if self.currentMapTemplate.powerUpMaxHealthPresent == False:
                    powerUp.kill()

    def registerPickedUpPowerUpHealth(self):
        self.currentMapTemplate.powerUpMaxHealthPresent = False

    def findMapTemplate(self, map):
        for template in self.visitedMaps:
            if template.name == map.nameMap:
                return template
        return None
