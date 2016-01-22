import pygame
import time
from Gameloop import *

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
       
        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                game_loop()                                                     #Einde Code Carlo
                    
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)                #Code van Eljakim
        textSurf, textRect = text_objects('Replay!', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        
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
winning_screen()