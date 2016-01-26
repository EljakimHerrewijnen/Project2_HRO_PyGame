import pygame
import random
from Players import * 
from Tile import *
from Players import *
from WinningScreen import *
from Units import *

AmountPlayersDefault = 0
Playerslist = Empty
def game_loop():                                #GameLoop door Joost en Eljakim
    global AmountPlayersDefault     #Eljakim's code
    if AmountPlayersDefault == 0:
        ChoosePlayerScreen()
    print("aantal normale spelers: " + AmountPlayersDefault)
    #Player1.GenerateRandomBiome()

    tile_loop()                     #Joost

def ChoosePlayerScreen():               #ChoosePlayerScreen door Joost en Eljakim
    pygame.init() 
    global AmountPlayersDefault

 # Can be changed if needed
    display_width = 800
    display_height = 600

    #Colours, same as Carlo's code
    black = (0,0,0)
    white = (255,255,255)
    bright_blue = (0, 0, 255)
    red = (175,0,0)
    green = (0,175,0)
    blue = (30,144,255)
    bright_red = (255,0,0)
    bright_green = (0,255,0)
    block_color = (53,115,255)
    intro = True


    #Name Caption, set up display, set up time
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Frequency')
    clock = pygame.time.Clock()


    #properties of the objects
    
    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
    
    #Playerlist is Empty
    Playerslist = Empty

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        
        bg = pygame.image.load("content/background_chooseplayers.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))  

        #oude text "Choose your amount of players"
        """
        gameDisplay.fill(white)        #Pretty much the same as carlo's Menu screen
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects('Choose your amount of players.', largeText)
        TextRect.center = ((display_width/2), (display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        """

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
       
        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                AmountPlayersDefault = 2
                #game_loop()               
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))
        # Properties of buttons
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('2 Players', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        
        if 350+100 > mouse[0] > 350 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (350,500,100,50))
            if click[0] == 1:
                AmountPlayersDefault = 3
                #game_loop()
        else: 
            pygame.draw.rect(gameDisplay, blue, (350,500,100,50))
        
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('3 Players', smallText)
        textRect.center = ( (350+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        
        
        
        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:    
            pygame.draw.rect(gameDisplay, bright_red, (550,500,100,50))
            if click[0] == 1:
                AmountPlayersDefault = 4
                #game_loop()
        else:
            pygame.draw.rect(gameDisplay, red, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('4 Players', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        #player lijst:  
        id = 1          #Joost is hier bezig
        for normalPlayers in range(AmountPlayersDefault):
            biomegenerator = Player1.GenerateRandomBiome
            Playername = input("What's the name of player " + str(id) + " ?: ")
            Playerslist = Node(Player1(id, Playername, biomegenerator, str(biomegenerator), 500), Playerslist)
            id += 1
            print("id = " + str(Playerslist.Value.Pl_id))
            print("name = " + Playerslist.Value.Pl_name)
            #print("gamecard = " + Playerslist.Value.Gamecard)
            #print("biome = " + Playerslist.Value.Biome)
            print("currency = " + str(Playerslist.Value.currency))
            if normalPlayers == AmountPlayersDefault - 1:
                if AmountPlayersDefault < 4:
                    AmountComputerPlayers = 0
                    AmountComputerPlayers = 4 - normalPlayers
                    for computerPlayers in range(AmountComputerPlayers - 1):
                        Playername = "PCplayer " + str(id)
                        biomegenerator = Player1.GenerateRandomBiome
                        Playerslist = Node(Player1(id, Playername, biomegenerator, biomegenerator, 500), Playerslist)
                        id += 1
                        print("id = " + str(Playerslist.Value.Pl_id))
                        print("name = " + Playerslist.Value.Pl_name)
                        #print("gamecard = " + Playerslist.Value.Gamecard)
                        #print("biome = " + Playerslist.Value.Biome)
                        print("currency = " + str(Playerslist.Value.currency))
                game_loop()

            
        pygame.display.update()
        clock.tick(15)                      #Einde code Joost en Eljakim

