import pygame
import sys
from pygame.locals import *
from globals import *
import globals


def straight_road(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration):
    road_deacceleration = 1
    road_brake = 5
    dz=0
    turn_speed = 15
    z=0
    for i in range(1,100,1):
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            if globals.road_velocity < 200:
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

        if keys[K_LEFT] and globals.road_velocity > 0:
            globals.car.rect.x -= turn_speed
            globals.car.image = pygame.image.load('car_left.png').convert_alpha()
        elif keys[K_RIGHT] and globals.road_velocity > 0:
            globals.car.rect.x += turn_speed
            globals.car.image = pygame.image.load('car_right.png').convert_alpha()
        else:
            globals.car.image = pygame.image.load('car_test.png').convert_alpha()

        globals.car.rect.x = max(0, min(globals.car.rect.x, SCREEN_WIDTH - globals.car.rect.width))

        if globals.car.rect.x <= 100 or globals.car.rect.x >= SCREEN_WIDTH - globals.car.rect.width - 100:
            if globals.road_velocity > 50:
                globals.road_velocity -= 10


        texture_position = globals.road_pos
        dz = 0
        z = 0

        screen.fill(globals.SKY)

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

        velocity_text = globals.create_text_with_outline(globals.font, f"Speed: {globals.road_velocity} mph", YELLOW, BLACK)
        screen.blit(velocity_text, (20, SCREEN_HEIGHT - 80))

        globals.all_sprites.update()
        globals.all_sprites.draw(screen)

        pygame.display.flip()