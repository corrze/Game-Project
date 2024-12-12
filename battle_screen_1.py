import pygame
import tkinter as tk

root = tk.Tk()
user_screen_width = root.winfo_screenwidth()
user_screen_height = root.winfo_screenheight()

clock = pygame.time.Clock()
fps = 60

pygame.init()

#window for game
bottom_panel1 = (user_screen_height * 0.3)
screen_width = (user_screen_width * 0.8)
screen_height = (user_screen_height * 0.8) + bottom_panel1

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption('Battle 1')


#Loading an image
#Background image
background_img = pygame.image.load('img/Background/FreeBackground.png').convert_alpha()
#Panel Image
panel_img = pygame.image.load('img/Icons/FreePanel.png').convert_alpha()


#Function for drawingBackgound 

def draw_background():
    screen.blit(background_img,(0,0))
    
    
#Function for drawing panel
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel1))
    
run = True
while run:

    clock.tick(fps)
    
    #Draw background
    draw_background()
    
    #Draw Panel
    draw_panel()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()
    
pygame.quit()
