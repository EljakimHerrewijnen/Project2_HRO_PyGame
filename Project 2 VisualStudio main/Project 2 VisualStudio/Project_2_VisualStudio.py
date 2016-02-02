import pygame
import time
import random
from Gameloop import *
from Rules import *


 
pygame.init()
 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
bright_blue = (0, 0, 255)
red = (175,0,0)
green = (0,175,0)
blue = (30,124,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

orange = (255, 128, 0)
bright_orange = (255, 179, 102)
yellow = (255,255,0)
bright_yellow = (229,230,0)
purple = (128,0,127)
bright_purple = (230,0,229)

 
block_color = (53,115,255)

 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Frequency')
clock = pygame.time.Clock()



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        bg = pygame.image.load("content/background_menu1.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))         

        largeText = pygame.font.Font('freesansbold.ttf', 115)

    
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------       
        
        if 25+100 > mouse[0] > 25 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (25,500,100,50))
            if click[0] == 1:
                game_loop()
                print("test")                 
        else:
            pygame.draw.rect(gameDisplay, green, (25,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Play!', smallText)
        textRect.center = ( (25+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1:
                Rules()                
        else: 
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))
        
        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Rules', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 275+100 > mouse[0] > 275 and 500+50 > mouse[1] > 500:    
            pygame.draw.rect(gameDisplay, bright_red, (275,500,100,50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, red, (275,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Quit!', smallText)
        textRect.center = ( (275+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------        
 

        if 400+100 > mouse[0] > 400 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_orange, (400,500,100,50))
            if click[0] == 1:
                Welcome()
                               
        else:
            pygame.draw.rect(gameDisplay, orange, (400,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Welcome', smallText)
        textRect.center = ( (400+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 525+100 > mouse[0] > 525 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_yellow, (525,500,100,50))
            if click[0] == 1:
                Background()                
        else: 
            pygame.draw.rect(gameDisplay, yellow, (525,500,100,50))
        
        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Background', smallText)
        textRect.center = ( (525+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 650+100 > mouse[0] > 650 and 500+50 > mouse[1] > 500:    
            pygame.draw.rect(gameDisplay, bright_purple, (650,500,100,50))
            if click[0] == 1:
                Settings()
        else:
            pygame.draw.rect(gameDisplay, purple, (650,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Settings', smallText)
        textRect.center = ( (650+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
           
        pygame.display.update()
        clock.tick(15)

game_intro()


