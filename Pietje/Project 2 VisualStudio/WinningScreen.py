import pygame
import time
from Gameloop import *
import sys
import os
#from Project_2_VisualStudio import *

RestartValue = 0

def winning_screen():
    pygame.init()
 
    display_width = 800      #Code door Eljakim
    display_height = 600
 
    black = (0,0,0)
    white = (255,255,255)
    bright_blue = (0, 0, 255)
    red = (175,0,0)
    green = (0,175,0)
    blue = (30,144,255)
    bright_red = (255,0,0)
    bright_green = (0,255,0)

 
    block_color = (53,115,255)
    
    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
 
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Frequency')
    clock = pygame.time.Clock()

    pygame.mixer.music.load('Solid Snake Victory Theme - Super Smash Bros. Brawl Music.mp3')
    pygame.mixer.music.play(0)

    winning = True

    while winning is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winning = False        
         
        bg = pygame.image.load("content/youwin.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))                                    # Einde Eljakim's code

        #gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)           #Stukje code van Carlo
        #TextSurf, TextRect = text_objects('Frequency', largeText)
        #TextRect.center = ((display_width/2), (display_height/4))
        #gameDisplay.blit(TextSurf, TextRect)
        
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
       
        
        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:    
            pygame.draw.rect(gameDisplay, bright_red, (550,500,100,50))
            if click[0] == 1:
                winning = False
        else:
            pygame.draw.rect(gameDisplay, red, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('Quit!', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
            
        pygame.display.update()
        clock.tick(15)                                      # Einde code Eljakim


'''
    GenerateRandomText = "blieb"
    sleep(0.05)
    GenerateRandomText = "blab"
    sleep(0.05)
    GenerateRandomText = "Lorem ipsum dolor et ameth"
    sleep(0.05)
    GenerateRandomText = "Generating Players........"
    sleep(0.05)
    GenerateRandomText = "blab"
    sleep(0.05)
    GenerateRandomText = "Lorem ipsum dolor et ameth"
    sleep(0.05)
    sleep(0.05)
    GenerateRandomText = "blab"
    sleep(0.05)
    GenerateRandomText = "Lorem ipsum dolor et ameth"
    sleep(0.05)
    GenerateRandomText = "Generating Players........"
    '''

def LoadingScreen():  #Door Eljakim, werkt
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
        myfont=pygame.font.SysFont("Britannic Bold", 40)
        nlabel=myfont.render("Welcome  Start Screen", 1, (255, 0, 0))
        LoadingFont = pygame.font.SysFont("Britannic Bold", 10)
        LoadingText = LoadingFont.render("balajblablajlasdjfka", 10, (0,0,0))
        for event in pygame.event.get():
            if event.type==K_ESCAPE:
                end_it=True
        gameDisplay.blit(bgmap,(200,50))
        pygame.display.flip()
        time.sleep(1)
        end_it = True
        game_loop()
