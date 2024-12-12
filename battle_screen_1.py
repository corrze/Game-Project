import pygame

clock = pygame.time.Clock()
fps = 60

pygame.init()

#window for game
bottom_panel1 = 300
screen_width = 1600
screen_height = 700 + bottom_panel1

screen = pygame.display.set_mode((screen_width, screen_height))
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
