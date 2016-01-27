import pygame
import time
import random
from Gameloop import *



def Rules():
    white=(255,248,207)
    display_width = 800
    display_height = 600
    Mapwidth = 18
    Mapheight = 18 
    Texturesize = 40
    Tilesize = Texturesize + 2
    pygame.init()
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    black=(0,0,0)
    end_it=False
    bgmap = pygame.image.load("content/LoadingScreen.jpg")
    while (end_it==False):
        gameDisplay.fill(white)
     #   myfont=pygame.font.SysFont("Britannic Bold", 40)

     #   nlabel=myfont.render("Welcome  Start Screen", 1, (255, 0, 0))
        for event in pygame.event.get():
            if event.type==K_ESCAPE:
                end_it=True
        gameDisplay.blit(bgmap,(200,50))
        pygame.display.flip()

def IceRules():
    print("Nog Niks")
