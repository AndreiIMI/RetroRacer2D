import pygame
import sys
from pygame.locals import *
import globals
from globals import *
from curved_road import *
from straight_road import *
from hill_road import *
from finish import *

def sandy_plains():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RETRO RACER 2D")

    light_road = pygame.image.load('images/light_road_sand.png').convert()
    dark_road = pygame.image.load('images/dark_road_sand.png').convert()
    light_strip=pygame.Surface((SCREEN_WIDTH,1)).convert()
    dark_strip=pygame.Surface((SCREEN_WIDTH,1)).convert()
    light_strip.fill(light_road.get_at((0,0)))
    dark_strip.fill(dark_road.get_at((0,0)))

    pygame.mixer.music.load('sound/music_02.mp3')
    pygame.mixer.music.set_volume(0.1)

    pygame.mixer.music.play(-1)


    ddz = 0.0003

    globals.init()
    globals.SKY = (230, 125, 14)

    road_acceleration = 4  # Adjust the acceleration value
    texture_position_acceleration = 4
    texture_position_threshold = 640
    half_texture_position_threshold = int(texture_position_threshold / 2)

    while True:

        straight_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration)
        hill_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration, 0.003)
        hill_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration, -0.003)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, -0.005, 5.5)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, 0.01, 5.5)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, -0.01, 5.5)
        straight_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration)
        hill_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration, 0.003)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, 0.01, 6)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, -0.01, 5)
        straight_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration)
        hill_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration, -0.002)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, -0.008, 8)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, 0.008, 8)
        hill_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration, 0.004)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, 0.005, 6)
        straight_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration)
        hill_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration, 0.003)
        hill_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration, -0.003)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, -0.01, 4.5)
        finish(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration)

        pygame.mixer.music.stop()
        pygame.mixer.music.load('sound/FIFA World Cup 2002 All Goals.mp3')
        return



if __name__ == "__main__":
    sandy_plains()