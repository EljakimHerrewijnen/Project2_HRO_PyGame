import pygame
import random
from Players import * 

AmountPlayersDefault = 0

def game_loop():
    global AmountPlayersDefault
    if AmountPlayersDefault == 0:
        ChoosePlayerScreen()
    print(AmountPlayersDefault)
    pygame.init()
    Texuresize = 40
    Tilesize = Texuresize + 2
    Mapwidth = 18
    Mapheight = 18
    screen = pygame.display.set_mode((Mapwidth * Tilesize, Mapheight * Tilesize))
    done = False
    clock = pygame.time.Clock()
    pygame.mixer.music.load('Cipher2.mp3')
    pygame.mixer.music.play(0)

    bgmap = pygame.image.load("content/map895.jpg")
    bgmap = pygame.transform.scale(bgmap, (Mapwidth * Tilesize, Mapheight * Tilesize))
    screen.blit(bgmap, (0, 0)) 

    """
    pl_id = 1
    countdown = AmountPlayersDefault
    for i in range(0, AmountPlayersDefault):
        random_nr = random.randint(0, countdown)
        if random_nr == 0:
            Playerlist = Node(Player(pl_id, Naam1, SwampCard), Playerlist)
        elif random_nr == 1:
            Playerlist = Node(Player(pl_id, Naam2, IceCard), Playerlist)
        elif random_nr == 2:
            Playerlist = Node(Player(pl_id, Naam3, DesertCard), Playerlist)
        elif random_nr == 3:
            Playerlist = Node(Player(pl_id, Naam4, ForestCard), Playerlist)
        if Playerlist
        countdown -= 1
        playerid += 1
        """

    #colours
    blue = (132, 112, 255)
    white = (255, 250, 250)
    green = (34, 139, 34)
    #textures
    transparent_texture = pygame.image.load('content/transparent_tile.png')
    Water_texture = pygame.image.load('content/water_texture.png')
    Water_texture = pygame.transform.scale(Water_texture, (Texuresize, Texuresize))
    Goldmine_texture = pygame.image.load('content/goldmine_texture.png')
    Goldmine_texture = pygame.transform.scale(Goldmine_texture, (Texuresize, Texuresize))
    Forest_texture = pygame.image.load('content/forest_texture.png')
    Forest_texture = pygame.transform.scale(Forest_texture, (Texuresize, Texuresize))
    Ice_texture = pygame.image.load('content/ice_texture.png')
    Ice_texture = pygame.transform.scale(Ice_texture, (Texuresize, Texuresize))
    Swamp_texture = pygame.image.load('content/swamp_texture.png')
    Swamp_texture = pygame.transform.scale(Swamp_texture, (Texuresize, Texuresize))
    Desert_texture = pygame.image.load('content/desert_texture.png')
    Desert_texture = pygame.transform.scale(Desert_texture, (Texuresize, Texuresize))

    #elements
    Water = 0
    Goldmine = 1
    Forest = 2
    Ice = 3
    Swamp = 4
    Desert = 5

    #elements linked to textures
    textures = {Water: pygame.transform.scale(transparent_texture, (Texuresize, Texuresize)), 
               Goldmine: pygame.transform.scale(transparent_texture, (Texuresize, Texuresize)), 
               Forest: pygame.transform.scale(transparent_texture, (Texuresize, Texuresize)),
               Ice: pygame.transform.scale(transparent_texture, (Texuresize, Texuresize)), 
               Swamp: pygame.transform.scale(transparent_texture, (Texuresize, Texuresize)), 
               Desert: pygame.transform.scale(transparent_texture, (Texuresize, Texuresize))}


    tilelist = [                        #[Water for r in range(Mapwidth)] for c in range(Mapheight)] #Water for r in range(0, 4)

                [Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Water, Water, Water, Water, Ice, Ice, Ice, Ice, Ice, Ice, Ice],
                [Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Water, Water, Water, Water, Ice, Ice, Ice, Ice, Ice, Ice, Ice],
                [Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Water, Water, Water, Water, Ice, Ice, Ice, Ice, Ice, Ice, Ice],
                [Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Water, Water, Water, Water, Ice, Ice, Ice, Ice, Ice, Ice, Ice],
                [Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Water, Water, Water, Water, Ice, Ice, Ice, Ice, Ice, Ice, Ice],
                [Swamp, Swamp, Swamp, Swamp, Swamp, Swamp, Water, Water, Water, Water, Water, Water, Ice, Ice, Ice, Ice, Ice, Ice],
                [Swamp, Swamp, Swamp, Swamp, Swamp, Water, Water, Water, Water, Water, Water, Water, Water, Ice, Ice, Ice, Ice, Ice],
                [Water, Water, Water, Water, Water, Water, Water, Goldmine, Goldmine, Goldmine, Goldmine, Water, Water, Water, Water, Water, Water, Water],
                [Water, Water, Water, Water, Water, Water, Water, Goldmine, Goldmine, Goldmine, Goldmine, Water, Water, Water, Water, Water, Water, Water],
                [Water, Water, Water, Water, Water, Water, Water, Goldmine, Goldmine, Goldmine, Goldmine, Water, Water, Water, Water, Water, Water, Water],
                [Water, Water, Water, Water, Water, Water, Water, Goldmine, Goldmine, Goldmine, Goldmine, Water, Water, Water, Water, Water, Water, Water],
                [Desert, Desert, Desert, Desert, Desert, Water, Water, Water, Water, Water, Water, Water, Water, Forest, Forest, Forest, Forest, Forest],
                [Desert, Desert, Desert, Desert, Desert, Desert, Water, Water, Water, Water, Water, Water, Forest, Forest, Forest, Forest, Forest, Forest],
                [Desert, Desert, Desert, Desert, Desert, Desert, Desert, Water, Water, Water, Water, Forest, Forest, Forest, Forest, Forest, Forest, Forest],
                [Desert, Desert, Desert, Desert, Desert, Desert, Desert, Water, Water, Water, Water, Forest, Forest, Forest, Forest, Forest, Forest, Forest],
                [Desert, Desert, Desert, Desert, Desert, Desert, Desert, Water, Water, Water, Water, Forest, Forest, Forest, Forest, Forest, Forest, Forest],
                [Desert, Desert, Desert, Desert, Desert, Desert, Desert, Water, Water, Water, Water, Forest, Forest, Forest, Forest, Forest, Forest, Forest],
                [Desert, Desert, Desert, Desert, Desert, Desert, Desert, Water, Water, Water, Water, Forest, Forest, Forest, Forest, Forest, Forest, Forest],]

    """
    for c in range(Mapheight):
        if c < 7:
            for r in range(Mapwidth):
                if r > -1 and r < 7:
                    tile = Swamp 
                elif r > 10 and r < 18: 
                    tile = Desert 
                elif r > 6 and r < 11: 
                    tile = Water 
                tilelist[r][c] = tile
        elif c > 10:
            for r in range(Mapwidth):
                if r > -1 and r < 7:
                    tile = Ice 
                elif r > 10 and r < 18: 
                    tile = Forest 
                elif r > 6 and r < 11: 
                    tile = Water 
                tilelist[r][c] = tile
        elif c > 6 and c < 11:
            for r in range(Mapwidth):
                if r > -1 and r < 7:
                    tile = Water 
                elif r > 10 and r < 18: 
                    tile = Water 
                elif r > 6 and r < 11: 
                    tile = Goldmine
                tilelist[r][c] = tile
               """

    while not done:
        for event in pygame.event.get():    #get all user events
            if event.type == pygame.QUIT:   #Option to quit
                done = True

        for row in range(Mapheight):
            for column in range(Mapwidth):
                    screen.blit(textures[tilelist[row][column]], (column * Tilesize, row * Tilesize))  #, Tilesize, Tilesize))

        pygame.display.flip()
        clock.tick(60)

def ChoosePlayerScreen():
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

        gameDisplay.fill(white)        #Pretty much the same as carlo's Menu screen
        largeText = pygame.font.Font('freesansbold.ttf', 40)
        TextSurf, TextRect = text_objects('Choose your amount of players.', largeText)
        TextRect.center = ((display_width/2), (display_height/4))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
       
        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                AmountPlayersDefault = 2
                game_loop()               
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
                game_loop()
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
                game_loop()
        else:
            pygame.draw.rect(gameDisplay, red, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('4 Players', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
            
        pygame.display.update()
        clock.tick(15)

