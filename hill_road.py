import pygame
import sys
from pygame.locals import *
from globals import *
import globals


def hill_road(road_acceleration, texture_position_threshold,screen,font, half_texture_position_threshold, light_road, dark_road, ddz, texture_position_acceleration,h_dir):
    texture_position = 0
    #those variables are used to increment texture_position
    dz = 0
    z = 0

    road_deacceleration = 1
    road_brake = 5

    hill_map=[0]*HALF_SCREEN_HEIGHT
    hill_map_lenght=len(hill_map)
    top_segment={'position':0,'dy':h_dir}  #dy=-0.005 for a downhill and dy=0.005 for an uphill
    bottom_segment={'position':HALF_SCREEN_HEIGHT,'dy':0}
    current_y=0
    dy=0
    ddy=0
    hill_velocity = 0
    hill_acceleration= 1  #this is the speed at witch we traverse the hill
    if h_dir > 0:
        hill_acceleration *= 4
    hill_deacceleration = 2
    hill_brake = 10
    old_y_hill_pos=SCREEN_HEIGHT
    current_y_hill_pos=SCREEN_HEIGHT
    y_hill_pos_difference=0    

    k=0
    while k < 2:
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
            if globals.road_velocity < 100:
                globals.road_velocity += road_acceleration
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
            
            ###
            ##if hill_velocity < 10:
            ##    hill_velocity += hill_acceleration
            top_segment['position']+=hill_acceleration
            #if we reach the hill's end we invert it's incrementation to exit it
            ##if top_segment['position']>=hill_map_lenght:
            ##   top_segment['position']=0
            ##   bottom_segment['dy']=top_segment['dy']
            ##   #top_segment['dy']+=0.005  #+0.005 to exit a downhill and -0.005 to exit an uphill
            ##   top_segment['dy']*=-1
            ##   k+=1
            ###

        elif keys[K_DOWN]:
            if globals.road_velocity > 0:
                globals.road_velocity -= road_brake
            if globals.road_velocity < 0:
                globals.road_velocity = 0
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
            ###
            #if hill_velocity > 0:
            #    hill_velocity -= hill_acceleration
            #if hill_velocity < 0:
            #    hill_velocity = 0
            #top_segment['position']+=hill_acceleration
            #if we reach the hill's end we invert it's incrementation to exit it
            ##if top_segment['position']>=hill_map_lenght:
            ##   top_segment['position']=0
            ##   bottom_segment['dy']=top_segment['dy']
            ##   #top_segment['dy']+=0.005  #+0.005 to exit a downhill and -0.005 to exit an uphill
            ##   top_segment['dy']*=-1
            ##   k+=1
            ###
        else:
            if globals.road_velocity > 0:
                globals.road_velocity -= road_deacceleration
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
            ###
            ##if hill_velocity > 0:
            ##    hill_velocity -= hill_deacceleration
            ##top_segment['position']+=hill_acceleration
            #if we reach the hill's end we invert it's incrementation to exit it
            ##if top_segment['position']>=hill_map_lenght:
            ##   top_segment['position']=0
            ##   bottom_segment['dy']=top_segment['dy']
            ##   #top_segment['dy']+=0.005  #+0.005 to exit a downhill and -0.005 to exit an uphill
            ##   top_segment['dy']*=-1
            ##   k+=1
            ###
        if top_segment['position']>=hill_map_lenght:
            top_segment['position']=0
            bottom_segment['dy']=top_segment['dy']
            top_segment['dy']-=h_dir  #+0.005 to exit a downhill and -0.005 to exit an uphill
            top_segment['dy']*=-1
            k+=1
            if h_dir < 0:
                hill_acceleration *= 2
            else:
                hill_acceleration /= 4
            #if k == 2:
            #    top_segment['dy']+=0.003
            
        #draw the road
        texture_position = globals.road_pos
        dz = 0
        z = 0
        dy=0
        ddy=0
        current_y=0
        old_y_hill_pos=SCREEN_HEIGHT
        current_y_hill_pos=SCREEN_HEIGHT
        screen.fill(BLUE)
        

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

        # Render the globals.road_velocity variable on the top right of the screen
        velocity_text = font.render(f"Speed: {globals.road_velocity}", True, WHITE)
        screen.blit(velocity_text, (SCREEN_WIDTH - velocity_text.get_width() - 10, 10))

        pygame.display.flip()


if __name__ == "__main__":
    main()
