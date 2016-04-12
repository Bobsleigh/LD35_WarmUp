import pygame
import os
from menu.Menu import Menu
import sys

from app.game import Game
from menu.Menu import Menu
from app.gameOverScene import GameOverScene
from app.settings import *
from app.winScene import WinScene

from app.TitleScreen import TitleScreen



def startGame():
    menu.close() #TODO: Define menu and game in this function.
    game.mainLoop()

if __name__ == '__main__':
    #Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)

    running = True
    while running:
    # Init
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.font.init()

        # Écran
        screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
        screen = pygame.display.set_mode(screenSize)

        #icon = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_triangle_v1.png')), (TILEDIMX, TILEDIMY))
        #pygame.display.set_icon(icon)
        pygame.display.set_caption("A Striangle journey")

        game = Game(screen)

        #Menu
        titleScreen = TitleScreen(screen)
        titleScreen.mainLoop()

        game.mainLoop()

        if game.endState == GAME_OVER:
            gameOverScene = GameOverScene(screen)
            gameOverScene.mainLoop()
            pygame.mixer.music.stop()
        elif game.endState == WIN:
            winScene = WinScene(screen)
            winScene.mainLoop()
            pygame.mixer.music.stop()
