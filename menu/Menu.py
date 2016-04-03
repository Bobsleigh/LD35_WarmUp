from pygame import init,display,draw

from menu.Option import *
from menu.EventHandlerMenu import *
from menu.Selector import *
from app.settings import *

class Menu():
    def __init__(self,screen,dimension):
        self.screen = screen

        # Menu center
        self.x = dimension.left
        self.y = dimension.top

        # Menu dimension
        self.menuWidth = dimension.width
        self.menuHeight = dimension.height

        # Menu list
        self.optionList = []
        self.eventHandler = EventHandlerMenu()

    def mainLoop(self):
        self.menuRunning = True
        while self.menuRunning:
            self.draw()
            self.eventHandler.eventHandle(self.optionList, self.selector)

    def draw(self):

        count = 0
        while count < self.optNum:
            option = self.optionList[count]

            draw.rect(self.screen, option.color1,
                      (option.button.left, option.button.top, option.button.width, option.button.height))
            draw.rect(self.screen, option.color2,
                      (option.button.left, option.button.top, option.button.width, option.button.height), 7)
            self.screen.blit(option.name, option.textPos)

            count += 1

        display.flip()

    def addOption(self,name,method):
        self.optionList.append(Option(name,method))
        self.createMenu()

    def createMenu(self):

        # Default select opt. 1
        self.optionList[0].isSelected = True
        self.optionList[0].setOptionStyle()

        # Mecanics.
        self.optNum = len(self.optionList)
        self.setOptionSize()
        self.selector = Selector(self.optNum)

    def setOptionSize(self):
        # Button real space
        spaceWidth = self.menuWidth
        spaceHeight = self.menuHeight / (self.optNum)

        for option in self.optionList:
            option.button.width = spaceWidth*0.9
            option.button.height = spaceHeight*0.7

            count = self.optionList.index(option)
            option.button.left = self.x-spaceWidth*0.45
            option.button.top = self.y+self.menuHeight*(2*count-self.optNum)/(2*self.optNum)+spaceHeight*0.15
            option.textPos =[self.x-option.name.get_width()*0.5,self.y+self.menuHeight*(2*count-self.optNum)/(2*self.optNum)+spaceHeight*0.45-option.name.get_height()*0.5]

    def close(self):
        self.menuRunning = False
