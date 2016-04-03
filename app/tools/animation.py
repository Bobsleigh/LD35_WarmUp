__author__ = 'Bobsleigh'

class Animation():
    def __init__(self, image, directionDict):
        self.imageIndex = 0
        self.currentImage = image
        self.imageChangeTimer = 0
        self.imageChangeTimerMax = 5

        self.directionDict = directionDict
        self.nbOfDirections = len(directionDict)

    def update(self, sprite):
        self.imageChangeTimer += 1
        if self.imageChangeTimer >= self.imageChangeTimerMax:
            self.imageIndex = (self.imageIndex+1) % self.nbOfDirections
            self.currentImage = self.directionDict[sprite.direction][self.imageIndex]
            self.imageChangeTimer = 0
            sprite.image = self.currentImage