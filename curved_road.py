from pygame.locals import *
import globals
from globals import *
import pygame,sys


def curve_function(road_acceleration, texture_position_threshold, screen,font, half_texture_position_threshold, light_strip, light_road, dark_strip, dark_road, ddz, texture_position_acceleration, c_dir):
    dz=0
    z=0
    texture_position=0
    curve_map=[0]*HALF_SCREEN_HEIGHT
    curve_map_lenght=len(curve_map)
    top_segment={'position':0,'dx':c_dir}  #dx=-0.01 for left curve and dx=0.01 for right curve
    bottom_segment={'position':HALF_SCREEN_HEIGHT,'dx':0}
    current_x=0
    dx=0
    ddx=0
    curve_speed=2  #this is the speed at witch we traverse the curve
    curve_value=0
    road_deacceleration = 1
    road_brake = 5
    
    #pygame.key.set_repeat(400, 30)
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
            if globals.road_velocity < 100:
                globals.road_velocity += road_acceleration
            globals.road_pos += globals.road_velocity
            if globals.road_pos >= texture_position_threshold:
                globals.road_pos = 0
            top_segment['position']+=curve_speed
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
           #if we reach the curve's end we invert it's incrementation to exit it
        if top_segment['position']>=curve_map_lenght:
            top_segment['position']=0
            bottom_segment['dx']=top_segment['dx']
            top_segment['dx']-=c_dir  #+0.01 to exit a left curve and -0.01 to exit a right curve
            top_segment['dx']*=-1
            k+=1


        #draw the road
        texture_position = globals.road_pos
        dz=0
        z=0
        dx=0
        ddx=0
        current_x=0
        screen.fill(BLUE)
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
        # Render the globals.road_velocity variable on the top right of the screen
        velocity_text = font.render(f"Speed: {globals.road_velocity}", True, WHITE)
        screen.blit(velocity_text, (SCREEN_WIDTH - velocity_text.get_width() - 10, 10))
        pygame.display.flip()
    

