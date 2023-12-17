import pygame
import sys
from pygame.locals import *
from globals import *

def straight_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration):
    road_deacceleration = 1
    road_brake = 5
    dz=0
    z=0
    road_pos =0
    road_velocity = 0
    for i in range(1,200,1):
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            if road_velocity < 100:
                road_velocity += road_acceleration
            road_pos += road_velocity
            if road_pos >= texture_position_threshold:
                road_pos = 0
        elif keys[K_DOWN]:
            if road_velocity > 0:
                road_velocity -= road_brake
            if road_velocity < 0:
                road_velocity = 0
            road_pos += road_velocity
            if road_pos >= texture_position_threshold:
                road_pos = 0
        else:
            if road_velocity > 0:
                road_velocity -= road_deacceleration
            road_pos += road_velocity
            if road_pos >= texture_position_threshold:
                road_pos = 0


        texture_position = road_pos
        dz = 0
        z = 0

        screen.fill(BLUE)

        for i in range(HALF_SCREEN_HEIGHT - 1, -1, -1):
            if texture_position < half_texture_position_threshold:
                screen.blit(light_road,(0, i + HALF_SCREEN_HEIGHT), (0, i, SCREEN_WIDTH, 1))   
            else:
                screen.blit(dark_road, (0, i + HALF_SCREEN_HEIGHT), (0, i, SCREEN_WIDTH, 1))

            dz += ddz
            z += dz

            texture_position += texture_position_acceleration + z

            if texture_position >= texture_position_threshold:
                texture_position = 0
        pygame.display.flip()