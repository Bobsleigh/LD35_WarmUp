from pygame import event,QUIT,KEYDOWN,K_RIGHT,K_LEFT,K_UP,K_DOWN,K_SPACE,K_RETURN
from sys import exit

class EventHandlerTitleScreen():
    def __init__(self):
        pass

    def eventHandle(self,optionList,selector):
        self.optionList = optionList
        self.selector = selector
        for dummyEv in event.get():
            if dummyEv.type == QUIT:
                exit()
            elif dummyEv.type == KEYDOWN:
                if dummyEv.key == K_RIGHT: #Does nothing for now...
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveRight()
                    self.optionList[self.selector.vPos].select()
                elif dummyEv.key == K_LEFT: #Does nothing for now...
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveLeft()
                    self.optionList[self.selector.vPos].select()
                elif dummyEv.key == K_UP:
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveUp()
                    self.optionList[self.selector.vPos].select()
                elif dummyEv.key == K_DOWN:
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveDown()
                    self.optionList[self.selector.vPos].select()
                elif dummyEv.key == K_SPACE:
                    self.optionList[self.selector.vPos].doOption()
                elif dummyEv.key == K_RETURN:
                    self.optionList[self.selector.vPos].doOption()
