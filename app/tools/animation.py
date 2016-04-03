__author__ = 'Bobsleigh'

class Animation():
    def __init__(self, directionList, dictOfImageListForEachDirection):
        self.imageIndex = 0
        self.currentImage = None
        self.imageChangeTimer = 0
        self.imageChangeTimerMax = 5

        self.directionList = directionList
        self.nbOfDirections = len(directionList)
        self.dictOfImageListForEachDirection = dictOfImageListForEachDirection

    def update(self, direction):
        self.imageChangeTimer += 1
        if self.imageChangeTimer >= self.imageChangeTimerMax:
            self.imageIndex = (self.imageIndex+1) % self.nbOfDirections
            self.currentImage = self.dictOfImageListForEachDirection[direction][self.imageIndex]
            self.imageChangeTimer = 0