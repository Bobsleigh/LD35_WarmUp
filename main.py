import pygame
import os

from app.game import Game
from app.menu import Menu
from app.gameOverScene import GameOverScene
from app.settings import *
from app.winScene import WinScene

if __name__ == '__main__':
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
    
        # Jeu
        menu = Menu(screen)
        menu.mainLoop()
        #screen = menu.screen
    
        game = Game(screen)
        game.mainLoop()


        if game.endState == GAME_OVER:
            gameOverScene = GameOverScene(screen)
            gameOverScene.mainLoop()
            pygame.mixer.music.stop()
        elif game.endState == WIN:
            winScene = WinScene(screen)
            winScene.mainLoop()
            pygame.mixer.music.stop()
