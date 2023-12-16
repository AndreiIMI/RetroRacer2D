import pygame
import sys
from pygame.locals import *

BLACK = pygame.color.THECOLORS["black"]
WHITE = pygame.color.THECOLORS["white"]
RED = pygame.color.THECOLORS["red"]
GREEN = pygame.color.THECOLORS["green"]
BLUE = (66, 200, 245)
YELLOW = pygame.color.THECOLORS["yellow"]
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
HALF_SCREEN_HEIGHT = int(SCREEN_HEIGHT / 2)

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RETRO RACER 2D")
    font = pygame.font.SysFont('Arial', 30)

    light_road = pygame.image.load('light_road.png').convert()
    dark_road = pygame.image.load('dark_road.png').convert()

    texture_position = 0

    ddz = 0.0003
    dz = 0
    z = 0

    road_pos = 0
    road_velocity = 0
    road_acceleration = 2  # Adjust the acceleration value
    road_deacceleration = 1
    road_brake = 5
    texture_position_acceleration = 4
    texture_position_threshold = 640
    half_texture_position_threshold = int(texture_position_threshold / 2)

    while True:
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

        # Render the road_velocity variable on the top right of the screen
        velocity_text = font.render(f"Speed: {road_velocity}", True, WHITE)
        screen.blit(velocity_text, (SCREEN_WIDTH - velocity_text.get_width() - 10, 10))

        pygame.display.flip()


if __name__ == "__main__":
    main()
