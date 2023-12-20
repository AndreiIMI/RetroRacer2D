import pygame,sys
from pygame.locals import *


BLACK=pygame.color.THECOLORS["black"]
WHITE=pygame.color.THECOLORS["white"]
RED=pygame.color.THECOLORS["red"]
GREEN=pygame.color.THECOLORS["green"]
global SKY
SKY = (66, 200, 245)
YELLOW=pygame.color.THECOLORS["yellow"]
SCREEN_WIDTH=1280
SCREEN_HEIGHT=720
HALF_SCREEN_HEIGHT=int(SCREEN_HEIGHT/2)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/car_test.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

def init():
    global road_velocity
    global road_pos
    global font
    global all_sprites
    global car
    global start_time
    road_velocity = 0
    road_pos = 0
    font = pygame.font.SysFont('Arial', 50)
    car = Car()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(car)
    start_time = pygame.time.get_ticks()


def create_text_with_outline(font, text, color, outline_color):
    # Render the main text
    text_surface = font.render(text, True, color)

    # Create a larger surface for the text with outline
    outline_surface = font.render(text, True, outline_color)
    outline_surface.blit(text_surface, (2, 2))  # Offset the main text to create the outline effect

    return outline_surface

