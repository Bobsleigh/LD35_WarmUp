from pygame import event,QUIT,KEYDOWN,K_ESCAPE,K_RIGHT,K_LEFT,K_UP,K_DOWN,K_SPACE,K_RETURN,K_BACKSPACE,KEYUP

from app.settings import *
from sys import exit

class EventHandlerPauseMenu():
    def __init__(self):
        pass

    def eventHandle(self,optionList,selector,close):
        self.optionList = optionList
        self.selector = selector
        self.close = close
        for dummyEv in event.get():
            if dummyEv.type == QUIT:
                exit()
            elif dummyEv.type == KEYDOWN:
                if dummyEv.key == K_UP:
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
                elif dummyEv.key == K_BACKSPACE:
                    self.close()
                elif dummyEv.key == K_ESCAPE:
                    self.close()

