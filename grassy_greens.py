import pygame
import sys
from pygame.locals import *
import globals
from globals import *
from curved_road import *
from straight_road import *
from hill_road import *
from S_curved_road import *

def grassy_greens():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RETRO RACER 2D")

    light_road = pygame.image.load('light_road.png').convert()
    dark_road = pygame.image.load('dark_road.png').convert()
    light_strip=pygame.Surface((SCREEN_WIDTH,1)).convert()
    dark_strip=pygame.Surface((SCREEN_WIDTH,1)).convert()
    light_strip.fill(light_road.get_at((0,0)))
    dark_strip.fill(dark_road.get_at((0,0)))
    texture_position = 0

    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.set_volume(0.1)

    pygame.mixer.music.play(-1)


    ddz = 0.0003
    dz = 0
    z = 0

    globals.init()

    road_acceleration = 4  # Adjust the acceleration value
    road_deacceleration = 1
    road_brake = 5
    texture_position_acceleration = 4
    texture_position_threshold = 640
    half_texture_position_threshold = int(texture_position_threshold / 2)

    while True:

        straight_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, -0.004, 7)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, 0.007, 5)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, -0.002, 2)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, -0.008, 4.5)
        straight_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, 0.005, 5.5)
        curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, -0.006, 6)
        straight_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration)
        # print(road_velocity, road_pos)
        # curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, 0.01, road_pos, road_velocity)



if __name__ == "__main__":
    grassy_greens()