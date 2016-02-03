import pygame
import random
from Players import * 
from Tile import *
from Players import *
from WinningScreen import *
from Units import *
from GameAI import *

AmountPlayersDefault = 0

def game_loop():                                #GameLoop door Joost en Eljakim
    global AmountPlayersDefault     #Eljakim's code
    if AmountPlayersDefault == 0:
        Playerslist = ChoosePlayerScreen()
        copy_Playerslist = Playerslist
    print("aantal normale spelers: " + str(AmountPlayersDefault))
    
    tile_loop(Playerslist, copy_Playerslist, AmountPlayersDefault)                     #Joost


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
    

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        
        bg = pygame.image.load("content/background_chooseplayers.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))  

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
       
        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                AmountPlayersDefault = 2
                intro = False
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
                intro = False
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
                intro = False
                #game_loop()
        else:
            pygame.draw.rect(gameDisplay, red, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('4 Players', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

                #hier wordt een player lijst aangemaakt:  
        id = 1                                      #gemaakt door Joost
        pl_1_Biome = "niks"
        pl_2_Biome = "niks"
        pl_3_Biome = "niks"
        pl_4_Biome = "niks"
        #Playerslist = Node("Hoi", Empty)
        pygame.display.update()
        clock.tick(15)                      
    
    Playerslist = Empty
    for normalPlayers in range(AmountPlayersDefault):       #Deze eerste for loop zorgt er voor dat elke echte speler een naam kan invullen
        biomegenerator = Player1.GenerateRandomBiome()  
        Playername = "Player " + str(normalPlayers + 1) 
        Playerslist = Node(Player1(id, Playername, biomegenerator, biomegenerator, 500, 0, 0, 0, 0, 0), Playerslist)
        #Deze loop zorgt ervoor dat spelers niet dezelfde biome kunnen hebben:
        while Playerslist.Value.Biome == pl_1_Biome or Playerslist.Value.Biome == pl_2_Biome or Playerslist.Value.Biome == pl_3_Biome or Playerslist.Value.Biome == pl_4_Biome:
            biogenerator = Player1.GenerateRandomBiome()
            Playerslist.Value.Biome = biogenerator
            Playerslist.Value.Gamecard = biogenerator
        if id == 1:
            pl_1_Biome = Playerslist.Value.Biome
        elif id == 2:
            pl_2_Biome = Playerslist.Value.Biome
        elif id == 3:
            pl_3_Biome = Playerslist.Value.Biome
        elif id == 4:
            pl_4_Biome = Playerslist.Value.Biome

        id += 1
        print("id = " + str(Playerslist.Value.Pl_id))
        print("name = " + Playerslist.Value.Pl_name)
        print("gamecard = " + Playerslist.Value.Gamecard)
        print("biome = " + Playerslist.Value.Biome)
        print("currency = " + str(Playerslist.Value.Currency))
        if normalPlayers == AmountPlayersDefault - 1:       #moeten er nog PC spelers aangemaakt worden?
            if AmountPlayersDefault < 4:
                AmountComputerPlayers = 0
                AmountComputerPlayers = 4 - normalPlayers
                for computerPlayers in range(AmountComputerPlayers - 1):        #Deze tweede for loop zorgt ervoor dat als er niet genoeg spelers zijn er PC spelers worden aangemaakt
                    Playername = "PCplayer " + str(id)
                    biomegenerator = Player1.GenerateRandomBiome()
                    Playerslist = Node(Player1(id, Playername, biomegenerator, biomegenerator, 500, 0, 0, 0, 0, 0), Playerslist)
                    #Deze for loop is hetzelfde als de vorige, dus het zorgt ervoor dat spelers niet dezelfde biome kunnen hebben:
                    while Playerslist.Value.Biome == pl_1_Biome or Playerslist.Value.Biome == pl_2_Biome or Playerslist.Value.Biome == pl_3_Biome or Playerslist.Value.Biome == pl_4_Biome:
                        biogenerator = Player1.GenerateRandomBiome()
                        Playerslist.Value.Biome = biogenerator
                        Playerslist.Value.Gamecard = biogenerator
                    if id == 3:
                        pl_3_Biome = Playerslist.Value.Biome
                    elif id == 4:
                        pl_4_Biome = Playerslist.Value.Biome

                    id += 1
                    print("id = " + str(Playerslist.Value.Pl_id))
                    print("name = " + Playerslist.Value.Pl_name)
                    print("gamecard = " + Playerslist.Value.Gamecard)
                    print("biome = " + Playerslist.Value.Biome)
                    print("currency = " + str(Playerslist.Value.Currency))
                #head = Playerslist

                #for i in range(0, 5):
                    #if i == 4:
                        #Playerslist = Node(Playerslist.Value, Playerslist.Tail)

    last_player = Playerslist
    while not last_player.Tail.IsEmpty:
        last_player = last_player.Tail
    last_player.Tail = Playerslist
    return Playerslist

            
        #Einde code Joost en Eljakim

def NextTurn():
    print("Next turn Commencing")
    pygame.time.delay(100)