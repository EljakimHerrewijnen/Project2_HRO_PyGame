import pygame
import time
import random
from Gameloop import *


white=(255,248,127)
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

orange = (255, 128, 0)
bright_orange = (255, 179, 102)
yellow = (255,255,0)
bright_yellow = (229,230,0)
purple = (128,0,127)
bright_purple = (230,0,229)

clock = pygame.time.Clock()

sound = 1


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()   


def game_intro():

    intro = True
    global sound

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
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_loop()
            if click[0] == 1 and sound == 0:
                game_loop()
                #print("test")                 
        else:
            pygame.draw.rect(gameDisplay, green, (25,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Play!', smallText)
        textRect.center = ( (25+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Rules()
            if click[0] == 1 and sound == 0:
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
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                pygame.quit()
                quit()
            if click[0] == 1 and sound == 0:
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
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Welcome()
            if click[0] == 1 and sound == 0:
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
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Background()
            if click[0] == 1 and sound == 0:
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
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Settings()
            if click[0] == 1 and sound == 0:
                Settings()
        else:
            pygame.draw.rect(gameDisplay, purple, (650,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Settings', smallText)
        textRect.center = ( (650+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
           
        pygame.display.update()
        clock.tick(15)


def Welcome():

    pygame.init()
    welkom = True
    global sound

    while welkom:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                welkom = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_1_welcome_by_frequency.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Background():

    pygame.init()
    background = True
    global sound

    while background:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                background = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_2_the_background_of_frequency.jpg")
        bg= pygame.transform.scale(bg, (700, 500))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 



def Settings():

    pygame.init()
    settings = True
    global sound

    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_settings.jpg")
        bg= pygame.transform.scale(bg, (400, 200))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (150,400,100,50))
            if click[0] == 1:
                sound = 1
               
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,400,100,50))
        
        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Sound on', smallText)
        textRect.center = ( (150+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (550,400,100,50))
            if click[0] == 1:
                sound = 0
               
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,400,100,50))
        
        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Sound off', smallText)
        textRect.center = ( (550+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
       

#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Rules():

    pygame.init()
    rules = True
    global sound

    while rules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rules = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_rules.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------
    
        if 100+100 > mouse[0] > 100 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (100,400,100,50))
            if click[0] == 1 and sound == 0:
                GameBoard()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                GameBoard()
            
        else:
            pygame.draw.rect(gameDisplay, green, (100,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Game Board', smallText)
        textRect.center = ( (100+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 225+100 > mouse[0] > 225 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (225,400,100,50))
            if click[0] == 1 and sound == 0:
                Climates()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, green, (225,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Climates', smallText)
        textRect.center = ( (225+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 350+100 > mouse[0] > 350 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (350,400,100,50))
            if click[0] == 1 and sound == 0:
                Thegame()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (350,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('The Game', smallText)
        textRect.center = ( (350+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 475+100 > mouse[0] > 475 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (475,400,100,50))
            if click[0] == 1 and sound == 0:
                Gameunits()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, green, (475,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Game units', smallText)
        textRect.center = ( (475+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)


#--------------------------------------------------------------------------


        if 600+100 > mouse[0] > 600 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (600,400,100,50))
            if click[0] == 1 and sound == 0:
                Gamesituations()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gamesituations()
            
        else:
            pygame.draw.rect(gameDisplay, green, (600,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Game situations', smallText)
        textRect.center = ( (600+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        #--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Rules()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Rules()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)


        pygame.display.update()
        clock.tick(15)   


def GameBoard():

    pygame.init()
    GameBoard = True
    global sound

    while GameBoard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameBoard = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_3_the_playboard.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Rules()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Rules()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)   

def Climates():

    pygame.init()
    climates = True
    global sound

    while climates:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                climates = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_4_climates.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (150,400,100,50))
            if click[0] == 1 and sound == 0:
                Climatecards()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Climatecards()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Climate cards', smallText)
        textRect.center = ( (150+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)


#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Climatecards():

    pygame.init()
    climatecards = True
    global sound

    while climatecards:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                climates = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_5_climate_cards.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
       
#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, bright_green, (550,450,100,50))
            if click[0] == 1 and sound == 0:
                Desert()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Desert()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,450,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Desert', smallText)
        textRect.center = ( (550+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
           

#--------------------------------------------------------------------------

         
        if 550+100 > mouse[0] > 550 and 150+50 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay, bright_green, (550,150,100,50))
            if click[0] == 1 and sound == 0:
                Swamp()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Swamp()
            
        else:
            pygame.draw.rect(gameDisplay, green, (550,150,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Swamp', smallText)
        textRect.center = ( (550+(100/2)), (150+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        

#--------------------------------------------------------------------------

          
        if 150+100 > mouse[0] > 150 and 150+50 > mouse[1] > 150:
            pygame.draw.rect(gameDisplay, bright_green, (150,150,100,50))
            if click[0] == 1 and sound == 0:
                Iceplains()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Iceplains()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,150,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Ice plains', smallText)
        textRect.center = ( (150+(100/2)), (150+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
      

#--------------------------------------------------------------------------

          
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 50:
            pygame.draw.rect(gameDisplay, bright_green, (150,450,100,50))
            if click[0] == 1 and sound == 0:
                Forest()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Forest()
        else:
            pygame.draw.rect(gameDisplay, green, (150,450,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Forest', smallText)
        textRect.center = ( (150+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

    
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Climates()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Swamp():

    pygame.init()
    Swamp = True
    global sound

    while Swamp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Swamp = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_7_swamp.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Climates()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)   


def Forest():

    pygame.init()
    forest = True
    global sound

    while forest:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Forest = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_9_forest.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------
        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Climates()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------



        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)   

def Iceplains():

    pygame.init()
    iceplains = True
    global sound

    while iceplains:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Iceplains = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_8_ice_plains.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------


        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Climates()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)   


def Desert():

    pygame.init()
    desert = True
    global sound

    while desert:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Desert = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_6_desert.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Climates()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Climates()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)   


def Thegame():

    pygame.init()
    thegame = True
    global sound

    while thegame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                thegame = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_the_game.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Rules()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Rules()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 225+100 > mouse[0] > 225 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (225,400,100,50))
            if click[0] == 1 and sound == 0:
                Beginninggame()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Beginninggame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (225,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Beginning game', smallText)
        textRect.center = ( (225+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
          

#--------------------------------------------------------------------------

         
        if 350+100 > mouse[0] > 350 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (350,400,100,50))
            if click[0] == 1 and sound == 0:
                MovesandTurns()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                MovesandTurns()
            
        else:
            pygame.draw.rect(gameDisplay, green, (350,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Moves/Turns', smallText)
        textRect.center = ( (350+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

          
        if 475+100 > mouse[0] > 475 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (475,400,100,50))
            if click[0] == 1 and sound == 0:
                Economy()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Economy()
            
        else:
            pygame.draw.rect(gameDisplay, green, (475,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Economy', smallText)
        textRect.center = ( (475+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
#--------------------------------------------------------------------------

          
        if 600+100 > mouse[0] > 600 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (600,400,100,50))
            if click[0] == 1 and sound == 0:
                Capturingland()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Capturingland()
            
        else:
            pygame.draw.rect(gameDisplay, green, (600,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 13)
        textSurf, textRect = text_objects('Capturing land', smallText)
        textRect.center = ( (600+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        

#--------------------------------------------------------------------------


        if 100+100 > mouse[0] > 100 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(gameDisplay, bright_green, (100,400,100,50))
            if click[0] == 1 and sound == 0:
                Howtowin()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Howtowin()
            
        else:
            pygame.draw.rect(gameDisplay, green, (100,400,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('How to win', smallText)
        textRect.center = ( (100+(100/2)), (400+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        pygame.display.update()
        clock.tick(15)   


def Beginninggame():

    pygame.init()
    beginninggame = True
    global sound

    while beginninggame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                beginninggame = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_10_start_of_the_game.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Thegame()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------


        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        pygame.display.update()
        clock.tick(15)  


def MovesandTurns():

    pygame.init()
    movesandturns = True
    global sound

    while movesandturns:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                movesandturns = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_11_moves_and_turns.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Thegame()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Economy():

    pygame.init()
    economy = True
    global sound

    while economy:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                economy = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_12_building_your_economy.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Thegame()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Capturingland():

    pygame.init()
    capturingland = True
    global sound

    while capturingland:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                capturingland = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_13_capturing_land.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Thegame()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 

def Howtowin():

    pygame.init()
    howtowin = True
    global sound

    while howtowin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                howtowin = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_12_how_do_you_win.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Thegame()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Thegame()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Gameunits():

    pygame.init()
    gameunits = True
    global sound

    while gameunits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameunits = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_game_units.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Rules()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Rules()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 600+100 > mouse[0] > 600 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (600,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (600,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (600+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 600+100 > mouse[0] > 600 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (600,440,100,50))
            if click[0] == 1 and sound == 0:
                Tank()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Tank()
            
        else:
            pygame.draw.rect(gameDisplay, green, (600,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Tank', smallText)
        textRect.center = ( (600+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
          

#--------------------------------------------------------------------------

         
        if 262.5+100 > mouse[0] > 262.5 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (262.5,440,100,50))
            if click[0] == 1 and sound == 0:
                Soldier()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Soldier()
            
        else:
            pygame.draw.rect(gameDisplay, green, (262.5,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Soldier', smallText)
        textRect.center = ( (262.5+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

          
        if 150+100 > mouse[0] > 150 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (150,440,100,50))
            if click[0] == 1 and sound == 0:
                Base()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Base()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Base', smallText)
        textRect.center = ( (150+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
#--------------------------------------------------------------------------

          
        if 487.5+100 > mouse[0] > 487.5 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (487.5,440,100,50))
            if click[0] == 1 and sound == 0:
                Barrack()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Barrack()
            
        else:
            pygame.draw.rect(gameDisplay, green, (487.5,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Barrack', smallText)
        textRect.center = ( (487.5+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        

#--------------------------------------------------------------------------


        if 375+100 > mouse[0] > 375 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (375,440,100,50))
            if click[0] == 1 and sound == 0:
                Boat()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Boat()
            
        else:
            pygame.draw.rect(gameDisplay, green, (375,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Boat', smallText)
        textRect.center = ( (375+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Soldier():

    pygame.init()
    soldier = True
    global sound

    while soldier:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                soldier = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_18_soldiers.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Gameunits()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 

def Tank():

    pygame.init()
    tank = True
    global sound

    while tank:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tank = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_20_tank.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Gameunits()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Base():

    pygame.init()
    base = True
    global sound

    while base:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                base = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_21_basis.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Gameunits()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)


def Barrack():

    pygame.init()
    barrack = True
    global sound

    while barrack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                barrack = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_22_barrack.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Gameunits()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)


def Boat():

    pygame.init()
    boat = True
    global sound

    while boat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boat = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_23_boat.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Gameunits()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        pygame.display.update()
        clock.tick(15)


def Gamesituations():

    pygame.init()
    gamesituations = True
    global sound

    while gamesituations:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameunits = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_game_situations.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Rules()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Rules()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 600+100 > mouse[0] > 600 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (600,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (600,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (600+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 600+100 > mouse[0] > 600 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (600,440,100,50))
            if click[0] == 1 and sound == 0:
                Tank()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Tank()
            
        else:
            pygame.draw.rect(gameDisplay, green, (600,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Conquer base', smallText)
        textRect.center = ( (600+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
          

#--------------------------------------------------------------------------

         
        if 375+100 > mouse[0] > 375 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (375,440,100,50))
            if click[0] == 1 and sound == 0:
                Fightingland()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Fightingland()
            
        else:
            pygame.draw.rect(gameDisplay, green, (375,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Fight on land', smallText)
        textRect.center = ( (375+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

          
        if 150+100 > mouse[0] > 150 and 440+50 > mouse[1] > 440:
            pygame.draw.rect(gameDisplay, bright_green, (150,440,100,50))
            if click[0] == 1 and sound == 0:
                Conquerbase()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Conquerbase()
            
        else:
            pygame.draw.rect(gameDisplay, green, (150,440,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('Conquer territory', smallText)
        textRect.center = ( (150+(100/2)), (440+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
#--------------------------------------------------------------------------



        pygame.display.update()
        clock.tick(15) 


def Conquerbase():

    pygame.init()
    conquerbase = True
    global sound

    while conquerbase:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                soldier = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_15_when_can_you_capture_a_basis.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Gameunits()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 

def Fightingland():

    pygame.init()
    fighting = True
    global sound

    while fighting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tank = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_12_fighting_to_capture_land.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Gameunits()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15) 


def Conquerterritory():

    pygame.init()
    conquerterritory = True
    global sound

    while conquerterritory:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                base = False
        
        gameDisplay.fill(white)
        bg = pygame.image.load("content/rules_17_capturing_enemy_territory.jpg")
        bg= pygame.transform.scale(bg, (600, 400))
        gameDisplay.blit(bg, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#--------------------------------------------------------------------------

        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (150,500,100,50))
            if click[0] == 1 and sound == 0:
                Gameunits()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                Gameunits()
            
        else:
            pygame.draw.rect(gameDisplay, red, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('BACK', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

#--------------------------------------------------------------------------

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_red, (550,500,100,50))
            if click[0] == 1 and sound == 0:
                game_intro()
            if click[0] == 1 and sound == 1:
                pygame.mixer.music.load('Button Click On Sound Effect.mp3')
                pygame.mixer.music.play(0)
                game_intro()
            
        else:
            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 12)
        textSurf, textRect = text_objects('HOME', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)
