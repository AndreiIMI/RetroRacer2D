from pygame.locals import *
import globals
from globals import *
import pygame,sys


def curve_function(road_acceleration, texture_position_threshold, screen, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, dx, curve_speed):
    dz=0
    z=0
    texture_position=0
    curve_map=[0]*HALF_SCREEN_HEIGHT
    curve_map_lenght=len(curve_map)
    curve_dx = dx
    top_segment={'position':0,'dx':dx}
    bottom_segment={'position':240,'dx':0}
    current_x=0
    curve_distance = 0
    dx=0
    ddx=0
    curve_value=0
    road_deacceleration = 1
    road_brake = 5
    turn_speed = 15
    
    k=0

    while k<2:
        #loop speed limitation
        #30 frames per second is enought
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
            if curve_distance > 60:
                globals.car.rect.x += curve_speed * curve_dx * (-100) * (globals.road_velocity / 100)
            top_segment['position']+=curve_speed
            curve_distance += globals.road_velocity / 30
        elif keys[K_DOWN]:
            if globals.road_velocity > 0:
                globals.road_velocity -= road_brake
                if curve_distance > 60:
                    globals.car.rect.x += curve_speed * curve_dx * (-100) * (globals.road_velocity / 100)
                top_segment['position']+=curve_speed
            if globals.road_velocity < 0:
                globals.road_velocity = 0
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
            curve_distance += globals.road_velocity / 30
        else:
            if globals.road_velocity > 0:
                globals.road_velocity -= road_deacceleration
                if curve_distance > 60:
                    globals.car.rect.x += curve_speed * curve_dx * (-100) * (globals.road_velocity / 100)
                top_segment['position']+=curve_speed
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
            curve_distance += globals.road_velocity / 30

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

           #if we reach the curve's end we invert it's incrementation to exit it
        if top_segment['position']>=curve_map_lenght:
            top_segment['position']=0
            bottom_segment['dx']=top_segment['dx']
            top_segment['dx']-=dx  #+0.01 to exit a left curve and -0.01 to exit a right curve
            top_segment['dx']*=-1
            k+=1


        #draw the road
        texture_position = globals.road_pos
        dz=0
        z=0
        dx=0
        ddx=0
        current_x=0
        screen.fill(globals.SKY)

        for i in range(HALF_SCREEN_HEIGHT-1,-1,-1):
            if top_segment['position'] < i:
               dx = bottom_segment['dx']
            else:
               dx = top_segment['dx']
            ddx += dx
            current_x += ddx
            curve_map[i] = current_x
            curve_value = curve_map[i]
            if texture_position<half_texture_position_threshold:
               screen.blit(light_strip,(0,i+HALF_SCREEN_HEIGHT)) 
               screen.blit(light_road,(curve_value,i+HALF_SCREEN_HEIGHT),(0,i,SCREEN_WIDTH,1))
            else:
               screen.blit(dark_strip,(0,i+HALF_SCREEN_HEIGHT))
               screen.blit(dark_road,(curve_value,i+HALF_SCREEN_HEIGHT),(0,i,SCREEN_WIDTH,1))
            dz+=ddz
            z+=dz
            texture_position+=texture_position_acceleration+z
            if texture_position>=texture_position_threshold:
               texture_position=0
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
    

