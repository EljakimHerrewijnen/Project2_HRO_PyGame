import pygame, sys, random, math
from Players import * 
from Node import *
from pygame.locals import *
from Units import *

#colors
black = (0,0,0)
white = (255,255,255)
poepkleur = (139, 69, 19)
cyan = (0, 255, 255)
currentid = 0

class Point:
  def __init__(self, x, y):
    self.X = x
    self.Y = y
    
class Tile:
  def __init__(self, position, texture, offset, properties):
      self.Position = position
      self.Texture = texture
      self.Offset = offset
      self.Properties = properties

def changePlayer():
    global currentid
    global Playerslist
    currentid += 1
    if currentid > 4:
        currentid = 1
    while Playerslist.IsEmpty == False:
        if Playerslist.Value.Pl_id == id:
            currentPl_id = Playerslist.Value.Pl_id
            currentPL_biome = Playerslist.Value.Biome
            currentPL_currency = Playerslist.Value.Currency
            currentPl_soldiers = Playerslist.Value.Units.Soldiers
            currentPl_robots = Playerslist.Value.Units.Robots
            currentPl_tanks = Playerslist.Value.Units.Tanks
            currentPl_barracks = Playerslist.Value.Units.Barracks
            currentPl_boats = Playerslist.Value.Units.Boats
            return currentPl_id, currentPL_biome, currentPL_currency, currentPl_soldiers, currentPl_robots, currentPl_tanks, currentPl_barracks, currentPl_boats
        else:
            Playerslist = Playerslist.Tail

    

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

currentTile = 0
Movements = 0
CurrentPlayer = 1


def tile_loop():
    global currentTile
    global Movements
    global CurrentPlayer

    pygame.init()
    Texturesize = 40
    Tilesize = Texturesize + 2
    Mapwidth = 18
    Mapheight = 18 
    screen = pygame.display.set_mode((Mapwidth * Tilesize + 250, Mapheight * Tilesize))
    done = False
    clock = pygame.time.Clock()
    pygame.mixer.music.load('Cipher2.mp3')
    pygame.mixer.music.play(0)

    bgmap = pygame.image.load("content/map895.jpg")
    bgmap = pygame.transform.scale(bgmap, (Mapwidth * Tilesize, Mapheight * Tilesize))
    screen.blit(bgmap, (0, 0)) 
    buy_background = pygame.image.load("content/wood.jpg")
    buy_background = pygame.transform.scale(buy_background, (250, 260))

    Soldier = pygame.image.load("content/soldier.png").convert_alpha()
    Soldier = pygame.transform.scale(Soldier, (Tilesize, Tilesize))
    soldierPos = [0, 0]
    Tank = pygame.image.load("content/tank.tif")
    Tank = pygame.transform.scale(Tank, (Tilesize, Tilesize))
    TankPos = [0, 0]

    #colours
    blue = (132, 112, 255)
    white = (255, 250, 250)
    green = (34, 139, 34)
    #textures
    transparent_texture = pygame.image.load('content/transparent_tile.png')
    Water_texture = pygame.image.load('content/water_texture.png')
    Water_texture = pygame.transform.scale(Water_texture, (Texturesize, Texturesize))
    Goldmine_texture = pygame.image.load('content/goldmine_texture.png')
    Goldmine_texture = pygame.transform.scale(Goldmine_texture, (Texturesize, Texturesize))
    Forest_texture = pygame.image.load('content/forest_texture.png')
    Forest_texture = pygame.transform.scale(Forest_texture, (Texturesize, Texturesize))
    Ice_texture = pygame.image.load('content/ice_texture.png')
    Ice_texture = pygame.transform.scale(Ice_texture, (Texturesize, Texturesize))
    Swamp_texture = pygame.image.load('content/swamp_texture.png')
    Swamp_texture = pygame.transform.scale(Swamp_texture, (Texturesize, Texturesize))
    Desert_texture = pygame.image.load('content/desert_texture.png')
    Desert_texture = pygame.transform.scale(Desert_texture, (Texturesize, Texturesize))

    #elements
    Water = 0
    Goldmine = 1
    Forest = 2
    Ice = 3
    Swamp = 4
    Desert = 5
    

    #elements linked to textures
    textures = {Water: pygame.transform.scale(transparent_texture, (Texturesize, Texturesize)), 
               Goldmine: pygame.transform.scale(transparent_texture, (Texturesize, Texturesize)), 
               Forest: pygame.transform.scale(transparent_texture, (Texturesize, Texturesize)),
               Ice: pygame.transform.scale(transparent_texture, (Texturesize, Texturesize)), 
               Swamp: pygame.transform.scale(transparent_texture, (Texturesize, Texturesize)), 
               Desert: pygame.transform.scale(transparent_texture, (Texturesize, Texturesize))}


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


    #fonts voor de text
    font1 = pygame.font.Font("freesansbold.ttf", 16)
    click = pygame.mouse.get_pressed()

    while not done:
        for event in pygame.event.get():    #get all user events
            if event.type == pygame.QUIT:   #Option to quit
                done = True

            # if a key is pressed move the soldier
            if event.type == KEYDOWN and soldierPos[0] < Mapwidth * Tilesize - Tilesize:
                if (event.key == K_RIGHT):
                    soldierPos[0] += 1 * Tilesize
            if event.type == KEYDOWN and soldierPos[0] > 0:
                if (event.key == K_LEFT):
                    soldierPos[0] -= 1 * Tilesize
            if event.type == KEYDOWN and soldierPos[1] > 0:
                if (event.key == K_UP):
                    soldierPos[1] -= 1 * Tilesize
            if event.type == KEYDOWN and soldierPos[1] < Mapheight * Tilesize - Tilesize:
                if (event.key == K_DOWN):
                    soldierPos[1] += 1 * Tilesize
            #als spatie is ingedrukt: print het klimaat of water
            if pygame.key.get_pressed()[K_SPACE] == 1:
                    currentTile = tilelist[mouse_x][mouse_y]
                    print("Water = 0/Goldmine = 1/Forest = 2/Ice = 3/Swamp = 4/Desert = 5: ", currentTile)
      
        
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] < (Mapwidth * Tilesize):
            mouse_x = math.floor(pygame.mouse.get_pos()[0] / Tilesize) * Tilesize
            mouse_y = math.floor(pygame.mouse.get_pos()[1] / Tilesize) * Tilesize
            soldierPos = [mouse_x, mouse_y]
            mouse_x = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
            mouse_y = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
        #print map
        for row in range(Mapheight):
            for column in range(Mapwidth):
                    screen.blit(textures[tilelist[row][column]], (column * Tilesize, row * Tilesize))  #, Tilesize, Tilesize))
        #Background buyscreen
        placeBackground = 0
        for i in range(0, 3):
            screen.blit(buy_background, (Mapwidth * Tilesize, placeBackground))
            placeBackground += 260
        #als de muis over tekst heen gaat verkleurt de achtergrond van de text
        
        mouse = pygame.mouse.get_pos()  
        click = pygame.mouse.get_pressed()
        if 865 + 124 > mouse[0] > 865 and 31 + 19 > mouse[1] > 31:          #soldier
            pygame.draw.rect(screen, cyan, (865,31,124,19))    
        else:
            pygame.draw.rect(screen, white, (865,31,124,19))
        textSurf, textRect = text_objects('Soldier = f150', font1)
        textRect.center = ( (865+(124/2)), (34+(7.5)) )
        screen.blit(textSurf, textRect)
        
        if 865 + 124 > mouse[0] > 865 and 115 + 19 > mouse[1] > 115:        #robot
            pygame.draw.rect(screen, cyan, (865,115,124,19))    
        else:
            pygame.draw.rect(screen, white, (865,115,124,19))
        textSurf, textRect = text_objects('Robot = f300', font1)
        textRect.center = ( (865+(124/2)), (115+(9)) )
        screen.blit(textSurf, textRect)

        if 865 + 124 > mouse[0] > 865 and 199 + 19 > mouse[1] > 199:        #tank
            pygame.draw.rect(screen, cyan, (865,199,124,19))    
            if click[0] == 1:
                Units.BuyTank()
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, white, (865,199,124,19))
        textSurf, textRect = text_objects('Tank = f750', font1)
        textRect.center = ( (865+(124/2)), (199+(9)) )
        screen.blit(textSurf, textRect)
        
        if 865 + 124 > mouse[0] > 865 and 283 + 19 > mouse[1] > 283:        #boat
            pygame.draw.rect(screen, cyan, (865,283,124,19))    
        else:
            pygame.draw.rect(screen, white, (865,283,124,19))
        textSurf, textRect = text_objects('Boat = f1000', font1)
        textRect.center = ( (865+(124/2)), (283+(9)) )
        screen.blit(textSurf, textRect)
        
        if 865 + 124 > mouse[0] > 865 and 367 + 19 > mouse[1] > 367:        #barrack
            pygame.draw.rect(screen, cyan, (865,367,124,19))    
        else:
            pygame.draw.rect(screen, white, (865,367,124,19))
        textSurf, textRect = text_objects('Barrack = f500', font1)
        textRect.center = ( (865+(124/2)), (367+(9)) )
        screen.blit(textSurf, textRect)   
        
        if 865 + 124 > mouse[0] > 865 and 700 + 19 > mouse[1] > 700:        #end turn
            pygame.draw.rect(screen, cyan, (865,700,124,19)) 
            if click[0] == 1:
                changePlayer()
                global currentPl_id
                pygame.time.delay(100)
                print(currentPl_id)
        else:
            pygame.draw.rect(screen, white, (865,700,124,19))
        textSurf, textRect = text_objects('End Turn!', font1)
        textRect.center = ( (865+(124/2)), (700+(9)) )
        screen.blit(textSurf, textRect) 

        """
        #Clickable Buttons. Code voor het click Event               Door Eljakim
        if 865 + 124 > mouse[0] > 865 and 700 + 19 > mouse[1] > 700 and pygame.mouse.get_pressed()[0]: #Turn Code
            print("def for player turn") 
        elif 865 + 124 > mouse[0] > 865 and 31 + 19 > mouse[1] > 31 and pygame.mouse.get_pressed()[0]:
            print("soldier")                        #Soldier f150 code
        elif 865 + 124 > mouse[0] > 865 and 115 + 19 > mouse[1] > 115 and pygame.mouse.get_pressed()[0]:
            print("Robot")   #Robot f300
        elif 865 + 124 > mouse[0] > 865 and 199 + 19 > mouse[1] > 199 and pygame.mouse.get_pressed()[0]:  #Tank f750      
            Units.BuyTank() 
            pygame.time.delay(100)
            screen.blit(Tank, (TankPos[0], TankPos[1]))
        elif 865 + 124 > mouse[0] > 865 and 283 + 19 > mouse[1] > 283 and pygame.mouse.get_pressed()[0]:        
            print("Boat")  #Boat
        elif 865 + 124 > mouse[0] > 865 and 367 + 19 > mouse[1] > 367 and pygame.mouse.get_pressed()[0]:        
            print("Barrack")  #Barrack
                """
        #print BuyScreen
        placePositionY = 10
        placePositionX = Tilesize * 2 + 5
        for i in range(0, 5):
            screen.blit(unit_textures[i], (Mapwidth * Tilesize + 20, placePositionY))
            #Text = font1.render(str(unit_text[i]), True, black, kots)
            #screen.blit(Text, (Mapwidth * Tilesize + 20 + placePositionX, placePositionY + 0.5 * Tilesize))
            placePositionY += Tilesize * 2
        
        #print wie er aan de beurt is
        Text = font1.render("Player " + "1" + "'s turn", True, black, transparent_texture)
        screen.blit(Text, (Mapwidth * Tilesize + 20, placePositionY + 20))

        #print de soldier
        screen.blit(Soldier,(soldierPos[0], soldierPos[1]))
        #print soldier-coordinaten in console
        #print("x = ", soldierPos[0], "y = ", soldierPos[1])


        pygame.display.flip()
        clock.tick(60)