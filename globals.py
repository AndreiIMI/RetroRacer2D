import pygame,sys
from pygame.locals import *


BLACK=pygame.color.THECOLORS["black"]
WHITE=pygame.color.THECOLORS["white"]
RED=pygame.color.THECOLORS["red"]
GREEN=pygame.color.THECOLORS["green"]
BLUE=pygame.color.THECOLORS["blue"]
YELLOW=pygame.color.THECOLORS["yellow"]
SCREEN_WIDTH=1280
SCREEN_HEIGHT=720
HALF_SCREEN_HEIGHT=int(SCREEN_HEIGHT/2)

def init():
    global road_velocity
    global road_pos
    road_velocity = 0
    road_pos = 0

