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


#Knight Class
class Knight():
    def __init__(self, x, y, name, max_hp, str, int, dex, potions):
         self.name = name
         self.max_hp = max_hp
         self.hp = max_hp
         self.atk = str
         self.start_potions = potions
         self.alive = True
         #self.image = pygame.image.load("img/Classes/Knight/Idle/____.png")
         #self.rect = self.image.get_rect()
         self.rect.center = (x, y)


class Mage():
    def __init__(self, x, y, name, max_hp, str, int, dex, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = int
        self.start_potions = potions
        self.alive = True
        #self.image = pygame.image.load("img/Classes/Mage/Idle/____.png")
        #self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Archer():
    def __init__(self, x, y, name, max_hp, str, int, dex, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = dex
        self.start_potions = potions
        self.alive = True
        #self.image = pygame.image.load("img/Classes/Mage/Idle/____.png")
        #self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        
        
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
