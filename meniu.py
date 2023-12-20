import pygame
import time
from sandy_plains import *
from grassy_greens import *
from night_time_stroll import *

# Initialize Pygame
pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Retro Racer 2D')

background_image = pygame.image.load('images/retro2.png')
background_image1 = pygame.image.load('images/volume-mute.png')
background_image2 = pygame.image.load('images/volume.png')
background_image = pygame.transform.scale(background_image, (1280, 720))
background_image1 = pygame.transform.scale(background_image1,(30,30))
background_image2 = pygame.transform.scale(background_image2,(30,30))
correct = True
pygame.mixer.music.load('sound/FIFA World Cup 2002 All Goals.mp3')
pygame.mixer.music.set_volume(0.1)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (66, 200, 245)


# Define button properties
button_width, button_height = 400, 100
button_x, button_y = (width - button_width) // 2, (height - button_height) // 2
button1_x,button1_y = (width - button_width) // 2, (height + button_height) // 2 + 50
button_color = GREEN
button1_color = RED
button2_color = GREEN
hover_color = GREEN
hover1_color = GREEN
click_color = RED
click1_color = RED
button_text = "Start Game"
button1_text = "Exit Game"
button2_text = "Sandy Plains"
text_color = BLACK
text3 = "Time:"
font = pygame.font.Font(None, 36)
font1 = pygame.font.SysFont('arial',50)
font2 = pygame.font.Font(None,36)
font3 = pygame.font.SysFont('arial',30)
show_button = True
first = False
MUSIC_END = pygame.USEREVENT
pygame.mixer.music.set_endevent(MUSIC_END)
text1 = "Welcome to Retro Racer 2D"
visited = True
button_rect3 = pygame.Rect(1205,35,30,30)
center = (1220,50)
radius = 30
button_rect = pygame.Rect(200,630,200,50)
button_rect1 = pygame.Rect(1000, 630, 200, 50)
button_rect2 = pygame.Rect(600,630,200,50)
visited1 = False
show_button1 = False
nr = 0


# Function to draw text on button
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
    
def shadow_text(text,color,x,y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    shadow = text_rect.move(40,40)
    pygame.draw.rect(screen, GRAY, shadow)
    
def draw_text_general(text,x,y):
    text_surface = font1.render(text,True,RED)
    text_rect = text_surface.get_rect(center=(x,y))
    screen.blit(text_surface,text_rect)

def draw_text_general1(text,x,y):
    text_surface = font2.render(text,True,WHITE)
    text_rect = text_surface.get_rect(center=(x,y))
    screen.blit(text_surface,text_rect)



# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if visited == True:
            pygame.mixer.music.play()
            visited = False
       
        # Check for mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos) and visited1 == False:
                sound = pygame.mixer.Sound('sound/button-pressed-38129.mp3')
                sound.play()
                pygame.mixer.music.stop()
                button_text = "Grassy Greens"
                button_color = GREEN
                visited1 = True
                pygame.draw.rect(screen, button_color,(200,630,200,50))
                draw_text(button_text, text_color,300,660)
                button1_text = "Nightly Stroll"
                button1_color = GREEN
                pygame.draw.rect(screen, button1_color, (1000, 630, 200, 50))
                draw_text(button1_text, text_color, 1100,660)
                show_button1 = True
                visited = False
                   
            elif button_rect.collidepoint(mouse_pos) and visited1 == True:
               sound = pygame.mixer.Sound('sound/button-pressed-38129.mp3')
               sound.play()
               pygame.mixer.music.stop()   
               grassy_greens()  
            if button_rect1.collidepoint(mouse_pos) and visited1 == False:
                sound = pygame.mixer.Sound('sound/button-pressed-38129.mp3')
                sound.play()
                while pygame.mixer.get_busy():
                    pygame.time.Clock().tick(30)
                running = False
            elif button_rect1.collidepoint(mouse_pos) and visited1 == True:
               sound = pygame.mixer.Sound('sound/button-pressed-38129.mp3')
               sound.play()
               pygame.mixer.music.stop()   
               night_time()  
            if button_rect3.collidepoint(mouse_pos):
                show_button = not show_button
                if show_button == True:
                    pygame.mixer.music.set_volume(0.1)
                if show_button == False:
                    pygame.mixer.music.set_volume(0.0)
            if button_rect2.collidepoint(mouse_pos):
               sound = pygame.mixer.Sound('sound/button-pressed-38129.mp3')
               sound.play()
               pygame.mixer.music.stop()   
               sandy_plains()      
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
        elif event.type == pygame.USEREVENT:
            pygame.mixer.music.play() 
    
    current_time = time.strftime("%H:%M:%S")
    text2 = font.render(current_time, True, WHITE)
    screen.blit(background_image,(0,0))
    screen.blit(text2,(60,80))

    # Draw the button
    pygame.draw.rect(screen, button_color,(200,630,200,50))
    draw_text(button_text, text_color,300,660)
    draw_text_general(text1,650,100)
    draw_text_general1(text3,110,60)
    pygame.draw.rect(screen, button1_color, (1000, 630, 200, 50))
    draw_text(button1_text, text_color, 1100,660)   
    pygame.draw.circle(screen, GRAY, center, radius) 
    if show_button1:
        button2_text = "Sandy Plains"
        button2_color = GREEN
        pygame.draw.rect(screen, button2_color, (600, 630, 200, 50))
        draw_text(button2_text, text_color, 700,660) 
        
    if show_button:
        screen.blit(background_image2,(1205,35))
    else:
        screen.blit(background_image1,(1205,35))
            
    # Update the display
    pygame.display.update()

# Quit Pygame properly
pygame.quit()