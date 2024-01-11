import pygame
import sys
from pygame.locals import *
from globals import *
import globals


def hill_road(road_acceleration, texture_position_threshold,screen, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration, hill_climb):
    texture_position = 0
    #those variables are used to increment texture_position
    dz = 0
    z = 0

    road_deacceleration = 1
    road_brake = 5

    hill_map=[0]*HALF_SCREEN_HEIGHT
    hill_map_lenght=len(hill_map)
    top_segment={'position':0,'dy':hill_climb}
    bottom_segment={'position':HALF_SCREEN_HEIGHT,'dy':0}
    current_y=0
    dy=0
    ddy=0
    hill_velocity = 0
    hill_acceleration = 6  #this is the speed at witch we traverse the hill
    hill_deacceleration = 2
    hill_brake = 10
    old_y_hill_pos=SCREEN_HEIGHT
    current_y_hill_pos=SCREEN_HEIGHT
    y_hill_pos_difference=0
    turn_speed = 15


    k=0
    while k < 2:
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():    #wait for events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #Movement controls
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            if globals.road_velocity < 200:
                globals.road_velocity += road_acceleration
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0

            if globals.road_velocity > 200:
                globals.road_velocity = 200
            
            top_segment['position']+=hill_acceleration

        elif keys[K_DOWN]:
            if globals.road_velocity > 0:
                globals.road_velocity -= road_brake
                top_segment['position']+=hill_acceleration
            if globals.road_velocity < 0:
                globals.road_velocity = 0
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
        else:
            if globals.road_velocity > 0:
                globals.road_velocity -= road_deacceleration
                top_segment['position']+=hill_acceleration
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
        if top_segment['position']>=hill_map_lenght:
            top_segment['position']=0
            bottom_segment['dy']=top_segment['dy']
            top_segment['dy']-=hill_climb
            top_segment['dy']*=-1
            k+=1

        if keys[K_LEFT] and globals.road_velocity > 0:
            globals.car.rect.x -= turn_speed
            globals.car.image = pygame.image.load('images/car_left.png').convert_alpha()
        elif keys[K_RIGHT] and globals.road_velocity > 0:
            globals.car.rect.x += turn_speed
            globals.car.image = pygame.image.load('images/car_right.png').convert_alpha()
        else:
            globals.car.image = pygame.image.load('images/car_test.png').convert_alpha()

        globals.car.rect.x = max(0, min(globals.car.rect.x, SCREEN_WIDTH - globals.car.rect.width))

        if globals.car.rect.x <= 100 or globals.car.rect.x >= SCREEN_WIDTH - globals.car.rect.width - 100:
            if globals.road_velocity > 50:
                globals.road_velocity -= 10
            
        #draw the road
        texture_position = globals.road_pos
        dz = 0
        z = 0
        dy=0
        ddy=0
        current_y=0
        old_y_hill_pos=SCREEN_HEIGHT
        current_y_hill_pos=SCREEN_HEIGHT
        screen.fill(globals.SKY)
        

        for i in range(HALF_SCREEN_HEIGHT - 1, -1, -1):
            ###
            if top_segment['position'] < i:
               dy = bottom_segment['dy']
            else:
               dy = top_segment['dy']
            ddy += dy
            current_y += ddy
            hill_map[i] = current_y
            current_y_hill_pos = int(i+HALF_SCREEN_HEIGHT-hill_map[i])
            ###
            if current_y_hill_pos<old_y_hill_pos:
                y_hill_pos_difference=old_y_hill_pos-current_y_hill_pos
                old_y_hill_pos=current_y_hill_pos
                if texture_position < half_texture_position_threshold:
                    if y_hill_pos_difference>1:
                        for j in range(y_hill_pos_difference):
                            screen.blit(light_road,(0,current_y_hill_pos+j),(0,i,SCREEN_WIDTH,1))
                    screen.blit(light_road,(0,current_y_hill_pos),(0,i,SCREEN_WIDTH,1))   
                else:
                    if y_hill_pos_difference>1:
                        for j in range(y_hill_pos_difference):
                            screen.blit(dark_road,(0,current_y_hill_pos+j),(0,i,SCREEN_WIDTH,1))
                    screen.blit(dark_road,(0,current_y_hill_pos),(0,i,SCREEN_WIDTH,1))

            dz += ddz
            z += dz
            texture_position += texture_position_acceleration + z
            if texture_position >= texture_position_threshold:
                texture_position = 0

        velocity_text = globals.create_text_with_outline(globals.font, f"Speed: {globals.road_velocity} mph", YELLOW, BLACK)
        screen.blit(velocity_text, (20, SCREEN_HEIGHT - 80))

        globals.all_sprites.update()
        globals.all_sprites.draw(screen)

        if globals.start_time != -1:
            elapsed_time_ms = pygame.time.get_ticks() - globals.start_time  # Elapsed time in milliseconds
            elapsed_time_sec = elapsed_time_ms // 1000  # Convert milliseconds to seconds
            minutes = elapsed_time_sec // 60
            seconds = elapsed_time_sec % 60
            milliseconds = elapsed_time_ms % 1000
            timer_text = globals.create_text_with_outline(globals.font, f"Time: {minutes:02}:{seconds:02}:{milliseconds:03}", RED, BLACK)
            screen.blit(timer_text, (10, 10))

        pygame.display.flip()
