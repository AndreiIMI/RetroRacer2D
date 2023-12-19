import pygame,sys
from pygame.locals import *


BLACK=pygame.color.THECOLORS["black"]
WHITE=pygame.color.THECOLORS["white"]
RED=pygame.color.THECOLORS["red"]
GREEN=pygame.color.THECOLORS["green"]
BLUE=(66, 200, 245)
YELLOW=pygame.color.THECOLORS["yellow"]
SCREEN_WIDTH=1280
SCREEN_HEIGHT=720
HALF_SCREEN_HEIGHT=int(SCREEN_HEIGHT/2)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('car_test.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

def init():
    global road_velocity
    global road_pos
    global font
    global all_sprites
    global car
    road_velocity = 0
    road_pos = 0
    font = pygame.font.SysFont('Arial', 30)
    car = Car()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(car)

