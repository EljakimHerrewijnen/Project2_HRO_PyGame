﻿import pygame
import time
import random
from Gameloop import *



white=(255,248,207)
display_width = 800
display_height = 600
Mapwidth = 18
Mapheight = 18 
Texturesize = 40
Tilesize = Texturesize + 2
gameDisplay = pygame.display.set_mode((display_width,display_height))
end_it=False


black = (0,0,0)
white = (255,255,255)
bright_blue = (0, 0, 255)
red = (175,0,0)
green = (0,175,0)
blue = (30,144,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

orange = (255,128,0)
bright_orange = (255,191,0)
yellow = (242, 242 ,13)
bright_yellow = (255, 255 , 0)
purple = (127 ,0 ,255)
bright_purple = (191,0,255)

clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()   


def Rules():

    pygame.init()
    rules = True

    while rules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rules = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/LoadingScreen.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------
    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                GameBoard()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Game Board', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Climates', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (550,400,100,50))
            if click[0] == 1:
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('The Game', smallText)
        textRect.center = ( (550+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 350+100 > mouse[0] > 350 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (350,400,100,50))
            if click[0] == 1:
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, green, (350,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Game Units', smallText)
        textRect.center = ( (350+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)   



def GameBoard():
    pygame.init()
    GameBoard = True

    while GameBoard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameBoard = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_3_the_playboard.jpg.")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Rules()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)   


def Climates():
    pygame.init()
    climates = True

    while climates:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                climates = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_4_climates.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
       
#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 50+50 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, bright_green, (550,50,100,50))
            if click[0] == 1:
                Desert()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,50,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Desert', smallText)
        textRect.center = ( (550+(100/2)), (50+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
           

#--------------------------------------------------------------------------

         
        if 550+100 > mouse[0] > 550 and 150+50 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay, bright_green, (550,150,100,50))
            if click[0] == 1:
                Swamp()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,150,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Swamp', smallText)
        textRect.center = ( (550+(100/2)), (150+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        

#--------------------------------------------------------------------------

          
        if 150+100 > mouse[0] > 150 and 150+50 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay, bright_green, (150,150,100,50))
            if click[0] == 1:
                Iceplains()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,150,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Ice plains', smallText)
        textRect.center = ( (150+(100/2)), (150+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
      

#--------------------------------------------------------------------------

          
        if 150+100 > mouse[0] > 150 and 50+50 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, bright_green, (150,50,100,50))
            if click[0] == 1:
                Forest()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,50,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Forest', smallText)
        textRect.center = ( (150+(100/2)), (50+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15) 


def Swamp():

    pygame.init()
    Swamp = True

    while Swamp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Swamp = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_7_swamp.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)   


def Forest():

    pygame.init()
    Forest = True

    while Forest:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Forest = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_9_forest.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------
        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------



        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)   


def Iceplains():

    pygame.init()
    Iceplains = True

    while Iceplains:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Iceplains = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_8_ice_plains.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------


        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)   


def Desert():

    pygame.init()
    Desert = True

    while Desert:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Desert = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_6_desert.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)   


def Thegame():

    pygame.init()
    thegame = True

    while thegame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                thegame = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/LoadingScreen.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Rules()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 50+50 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, bright_green, (550,50,100,50))
            if click[0] == 1:
                Beginninggame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,50,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Beginning game', smallText)
        textRect.center = ( (550+(100/2)), (50+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
          

#--------------------------------------------------------------------------

         
        if 550+100 > mouse[0] > 550 and 150+50 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay, bright_green, (550,150,100,50))
            if click[0] == 1:
                MovesandTurns()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,150,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Moves/Turns', smallText)
        textRect.center = ( (550+(100/2)), (150+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

          
        if 150+100 > mouse[0] > 150 and 150+50 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay, bright_green, (150,150,100,50))
            if click[0] == 1:
                Economy()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,150,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Economy', smallText)
        textRect.center = ( (150+(100/2)), (150+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
#--------------------------------------------------------------------------

          
        if 150+100 > mouse[0] > 150 and 50+50 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, bright_green, (150,50,100,50))
            if click[0] == 1:
                Capturingland()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,50,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 13)
        textSurf, textRect = text_objects('Capturing land', smallText)
        textRect.center = ( (150+(100/2)), (50+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        

#--------------------------------------------------------------------------


        if 150+100 > mouse[0] > 150 and 250+50 > mouse[1] > 250:
            pygame.draw.rect(gameDisplay, bright_green, (150,250,100,50))
            if click[0] == 1:
                Howtowin()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,250,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('How to win', smallText)
        textRect.center = ( (150+(100/2)), (250+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        pygame.display.update()
        clock.tick(15)   


def Beginninggame():

    pygame.init()
    beginninggame = True

    while beginninggame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beginninggame = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_10_start_of_the_game.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)  


def MovesandTurns():

    pygame.init()
    movesandturns = True

    while movesandturns:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                movesandturn = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_11_moves_and_turns.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Economy():

    pygame.init()
    economy = True

    while economy:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                economy = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_12_building_your_economy.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Capturingland():

    pygame.init()
    capturingland = True

    while capturingland:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                capturingland = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_13_capturing_land.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 

def Howtowin():

    pygame.init()
    howtowin = True

    while howtowin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                howtowin = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_14_how_do_you_win.jpg")
        bg= pygame.transform.scale(bg, (700, 430))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            if click[0] == 1:
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 

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
       
        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                game_loop()
                print("test")                 
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('Play!', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        if 350+100 > mouse[0] > 350 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (350,500,100,50))
            if click[0] == 1:
                Rules()                
        else: 
            pygame.draw.rect(gameDisplay, blue, (350,500,100,50))
        
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('Rules', smallText)
        textRect.center = ( (350+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        
        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:    
            pygame.draw.rect(gameDisplay, bright_red, (550,500,100,50))
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay, red, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('Quit!', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
            
        pygame.display.update()
        clock.tick(15)


def Gameunits():

    pygame.init()
    gameunits = True

    while gameunits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameunits = False
        
        gameDisplay.fill(white)
        #bg = pygame.image.load("content/LoadingScreen.jpg")
        #bg= pygame.transform.scale(bg, (display_width, display_height))
        #gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            #if click[0] == 1:
                #Rules()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 600+100 > mouse[0] > 600 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (600,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (600,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (600+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 600+100 > mouse[0] > 600 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (600,440,100,50))
            if click[0] == 1:
                Tank()
            
        else:
            pygame.draw.rect(gameDisplay, green, (600,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Tank', smallText)
        textRect.center = ( (600+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
          

#--------------------------------------------------------------------------

         
        if 262.5+100 > mouse[0] > 262.5 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (262.5,440,100,50))
            if click[0] == 1:
                Soldier()
            
        else:
            pygame.draw.rect(gameDisplay, green, (262.5,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Soldier', smallText)
        textRect.center = ( (262.5+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

          
        if 150+100 > mouse[0] > 150 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (150,440,100,50))
            if click[0] == 1:
                Base()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Base', smallText)
        textRect.center = ( (150+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
#--------------------------------------------------------------------------

          
        if 487.5+100 > mouse[0] > 487.5 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (487.5,440,100,50))
            if click[0] == 1:
                Barrack()
            
        else:
            pygame.draw.rect(gameDisplay, green, (487.5,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Barrack', smallText)
        textRect.center = ( (487.5+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        

#--------------------------------------------------------------------------


        if 375+100 > mouse[0] > 375 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (375,440,100,50))
            if click[0] == 1:
                Boat()
            
        else:
            pygame.draw.rect(gameDisplay, green, (375,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Boat', smallText)
        textRect.center = ( (375+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Soldier():

    pygame.init()
    soldier = True

    while soldier:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                soldier = False
        
        gameDisplay.fill(white)
        #bg = pygame.image.load("content/LoadingScreen.jpg")
        #bg= pygame.transform.scale(bg, (display_width, display_height))
        #gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 

def Tank():

    pygame.init()
    tank = True

    while tank:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tank = False
        
        gameDisplay.fill(white)
        #bg = pygame.image.load("content/LoadingScreen.jpg")
        #bg= pygame.transform.scale(bg, (display_width, display_height))
        #gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Base():

    pygame.init()
    base = True

    while base:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                base = False
        
        gameDisplay.fill(white)
        #bg = pygame.image.load("content/LoadingScreen.jpg")
        #bg= pygame.transform.scale(bg, (display_width, display_height))
        #gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)


def Barrack():

    pygame.init()
    barrack = True

    while barrack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                barrack = False
        
        gameDisplay.fill(white)
        #bg = pygame.image.load("content/LoadingScreen.jpg")
        #bg= pygame.transform.scale(bg, (display_width, display_height))
        #gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)


def Boat():

    pygame.init()
    boat = True

    while boat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boat = False
        
        gameDisplay.fill(white)
        #bg = pygame.image.load("content/LoadingScreen.jpg")
        #bg= pygame.transform.scale(bg, (display_width, display_height))
        #gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (550,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Home', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)















