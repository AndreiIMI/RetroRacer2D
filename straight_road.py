import pygame
import sys
from pygame.locals import *
from globals import *
import globals


def straight_road(road_acceleration, texture_position_threshold, screen,font, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration):
    road_deacceleration = 1
    road_brake = 5
    dz=0
    z=0
    for i in range(1,200,1):
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            if globals.road_velocity < 100:
                globals.road_velocity += road_acceleration
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
        elif keys[K_DOWN]:
            if globals.road_velocity > 0:
                globals.road_velocity -= road_brake
            if globals.road_velocity < 0:
                globals.road_velocity = 0
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
        else:
            if globals.road_velocity > 0:
                globals.road_velocity -= road_deacceleration
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0


        texture_position = globals.road_pos
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

        # Render the globals.road_velocity variable on the top right of the screen
        velocity_text = font.render(f"Speed: {globals.road_velocity}", True, WHITE)
        screen.blit(velocity_text, (SCREEN_WIDTH - velocity_text.get_width() - 10, 10))
        pygame.display.flip()