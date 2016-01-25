import pygame
import random
from Node import *
from Players import *
from Gameloop import *
from Units import *

Clicks = 0
def BuyScreen():
    global Clicks
    pygame.init()
    Unit = Empty
    display_width = 800
    display_height = 600
    black = (0,0,0)
    white = (255,255,255)
    bright_blue = (0, 0, 255)
    red = (175,0,0)
    green = (0,175,0)
    blue = (30,144,255)
    bright_red = (255,0,0)
    bright_green = (0,255,0)
    
    def text_objects(text, font):
        TextSurface = font.render(text, True, black)
        return TextSurface, TextSurface.get_rect()
 
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Frequency')
    clock = pygame.time.Clock()

    Rules = True

    while Rules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Rules = False        
     
        gameDisplay.fill(white)
        smallText = pygame.font.Font('freesansbold.ttf', 14)

        #Text/Rules
        TextSurf, TextRect = text_objects('These are the game rules', smallText)
        TextRect.center = ((display_width/3), (display_height/3))
        gameDisplay.blit(TextSurf, TextRect)


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:    
            pygame.draw.rect(gameDisplay, bright_red, (550,500,100,50))
        if click[0] == 1:
               Clicks += 1
               Units.BuyTank()
               Unit = Node(Units (3, "Tank",Clicks), Unit)
               Player.GenerateRandomBiome()
               print(Player.Biome)
               print(Unit.Value.unittype)
               print(Unit.Value.position)
        else:
            pygame.draw.rect(gameDisplay, red, (550,500,100,50))
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('Buy soldier', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
  
            
        pygame.display.update()
        clock.tick(15)
