import pygame
import time
from test_main import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Retro Racer 2D')

# Load the background image
background_image = pygame.image.load('retro2.png')
# Replace 'background.jpg' with your image path
background_image1 = pygame.image.load('volume-mute.png')
background_image2 = pygame.image.load('volume.png')
background_image = pygame.transform.scale(background_image, (1280, 720))
background_image1 = pygame.transform.scale(background_image1,(30,30))
background_image2 = pygame.transform.scale(background_image2,(30,30))
correct = True
pygame.mixer.music.load('FIFA World Cup 2002 All Goals.mp3')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Define button properties
button_width, button_height = 400, 100
button_x, button_y = (width - button_width) // 2, (height - button_height) // 2
button1_x,button1_y = (width - button_width) // 2, (height + button_height) // 2 + 50
button_color = GREEN
button1_color = RED
hover_color = GREEN
hover1_color = GREEN
click_color = RED
click1_color = RED
button_text = "Start Game"
button1_text = "Exit Game"
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
button_rect2 = pygame.Rect(1205,35,30,30)
center = (1220,50)
radius = 30
button_rect = pygame.Rect(200,630,200,50)
button_rect1 = pygame.Rect(1000, 630, 200, 50)


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
    text_surface = font1.render(text,True,BLACK)
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
            if button_rect.collidepoint(mouse_pos):
                #print("Button Clicked!")  # Replace with your desired functionality
                sound = pygame.mixer.Sound('button-pressed-38129.mp3')
                sound.play()
                pygame.mixer.music.stop()
                main()
            if button_rect1.collidepoint(mouse_pos):
                sound = pygame.mixer.Sound('button-pressed-38129.mp3')
                sound.play()
                while pygame.mixer.get_busy():
                    pygame.time.Clock().tick(30)
                running = False
            if button_rect2.collidepoint(mouse_pos):
                show_button = not show_button
                if show_button == True:
                    pygame.mixer.music.set_volume(1.0)
                if show_button == False:
                    pygame.mixer.music.set_volume(0.0)
                
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            #button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            #button_rect1 = pygame.Rect(button1_x,button1_y,button_width,button_height)
        elif event.type == pygame.USEREVENT:
            pygame.mixer.music.play() 
    
    current_time = time.strftime("%H:%M:%S")
    # Render time as text
    text2 = font.render(current_time, True, WHITE)  # Rendering text in white color
    # Draw the background image
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
    if show_button:
        screen.blit(background_image2,(1205,35))
    else:
        screen.blit(background_image1,(1205,35))
            
    # Update the display
    pygame.display.update()

# Quit Pygame properly
pygame.quit()