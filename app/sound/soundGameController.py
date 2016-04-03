import pygame
import os

class soundGameController():
    def __init__(self):
        pygame.mixer.music.load(os.path.join('sample', 'theme1.wav'))
        pygame.mixer.music.play(-1)
