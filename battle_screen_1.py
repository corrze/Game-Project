import pygame

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
#panel_img = pygame.image.load('img/)