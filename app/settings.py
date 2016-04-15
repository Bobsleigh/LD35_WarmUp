# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BACKGROUND_COLOR = (255,255,255)

COLOR_MENU_1 = (79,243,255)
COLOR_MENU_2 = (10, 150, 150)

COLOR_MENU_SELECT_1 = (255, 100, 100)
COLOR_MENU_SELECT_2 = (255, 0, 0)


FPS = 60

GRAVITY = 1 # In pixels per frame
FRICTION = 0.5

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

# Dimension tile
TILEDIMX = 32
TILEDIMY = 32

# Le Sprite Layer
SPRITE_LAYER = 4

#Player jump states
GROUNDED = 0
JUMP = 1
DOUBLE_JUMP = 2

#Player sepcials states
IDLE = 0
DASH = 1
COOLDOWN = 2
WALL_HUGGING = 3

#Player shape
EDGE = 0
TRIANGLE = 1
SQUARE = 2
PENTAGON = 3
HEXAGON = 4
CIRCLE = 5

#Collisions
COLLISION_LAYER = 0
SOLID = 1 #Booléen de GID pour collision
SPIKE = 2

#Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

#Scenes self.nextScene commands, used to tell SceneHandler what next scene to run after this one ends
GAME = 0
GAME_OVER = 1
WIN = 2
TITLE_SCREEN = 3


# Development mode, DEV or OPT
DEV_MODE = 1
OPT_MODE = 0
MODE = DEV_MODE
