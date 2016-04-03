# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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

#End States of Game
GAME_OVER = 1
WIN = 2
