import pygame
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
        
        #bg = pygame.image.load("content/LoadingScreen.jpg")
        #bg= pygame.transform.scale(bg, (display_width, display_height))
        #gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

    
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

        pygame.display.update()
        clock.tick(15)   


def GameBoard():
    pygame.init()
    GameBoard = True

    while GameBoard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameBoard = False
        
        #bg = pygame.image.load("content/LoadingScreen.jpg")
        #bg= pygame.transform.scale(bg, (display_width, display_height))
        #gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)


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

def Climates():
    pygame.init()
    climates = True

    while climates:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                climates = False
        
        #bg = pygame.image.load("content/LoadingScreen.jpg")
        #bg= pygame.transform.scale(bg, (display_width, display_height))
        #gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)


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
        pygame.display.update()
        clock.tick(15)   

         
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
        pygame.display.update()

          
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
        pygame.display.update()

          
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

def Swamp():

    pygame.init()
    Swamp = True

    while Swamp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Swamp = False
        
        bg = pygame.image.load("content/LoadingScreen.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)


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


def Forest():

    pygame.init()
    Forest = True

    while Forest:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Forest = False
        
        bg = pygame.image.load("content/LoadingScreen.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)


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

def Iceplains():

    pygame.init()
    Iceplains = True

    while Iceplains:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Iceplains = False
        
        bg = pygame.image.load("content/LoadingScreen.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)


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


def Desert():

    pygame.init()
    Desert = True

    while Desert:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Desert = False
        
        bg = pygame.image.load("content/LoadingScreen.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            #if click[0] == 1:
                #game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 16)
        textSurf, textRect = text_objects('Back', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)


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





