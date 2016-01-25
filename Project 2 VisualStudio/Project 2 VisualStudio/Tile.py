import pygame, sys, random, math
from Players import * 
from Node import *
from pygame.locals import *


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

currentTile = 0

def tile_loop():
    global currentTile
    pygame.init()
    Texuresize = 40
    Tilesize = Texuresize + 2
    Mapwidth = 18
    Mapheight = 18
    screen = pygame.display.set_mode((Mapwidth * Tilesize + 100, Mapheight * Tilesize))
    done = False
    clock = pygame.time.Clock()
    pygame.mixer.music.load('Cipher2.mp3')
    pygame.mixer.music.play(0)

    bgmap = pygame.image.load("content/map895.jpg")
    bgmap = pygame.transform.scale(bgmap, (Mapwidth * Tilesize, Mapheight * Tilesize))
    screen.blit(bgmap, (0, 0)) 

    Soldier = pygame.image.load("content/soldier_texture.tif").convert_alpha()
    Soldier = pygame.transform.scale(Soldier, (Tilesize, Tilesize))
    soldierPos = [0, 0]

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
            # if a key is pressed move the soldier
            if event.type == KEYDOWN and soldierPos[0] < Mapwidth - 1:
                if (event.key == K_RIGHT):
                    soldierPos[0] += 1
            if event.type == KEYDOWN and soldierPos[0] > 0:
                if (event.key == K_LEFT):
                    soldierPos[0] -= 1
            if event.type == KEYDOWN and soldierPos[1] > 0:
                if (event.key == K_UP):
                    soldierPos[1] -= 1
            if event.type == KEYDOWN and soldierPos[1] < Mapheight - 1:
                if (event.key == K_DOWN):
                    soldierPos[1] += 1
            #als spatie is ingedrukt: print het klimaat of water
            if pygame.key.get_pressed()[K_SPACE] == 1:
                    currentTile = tilelist[mouse_x][mouse_y]
                    print("Water = 0/Goldmine = 1/Forest = 2/Ice = 3/Swamp = 4/Desert = 5: ", currentTile)
        

        if pygame.mouse.get_pressed()[0]:
            mouse_x = math.floor(pygame.mouse.get_pos()[0] / Tilesize) * Tilesize
            mouse_y = math.floor(pygame.mouse.get_pos()[1] / Tilesize) * Tilesize
            soldierPos = [mouse_x, mouse_y]
            mouse_x = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
            mouse_y = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
            
        #print map
        for row in range(Mapheight):
            for column in range(Mapwidth):
                    screen.blit(textures[tilelist[row][column]], (column * Tilesize, row * Tilesize))  #, Tilesize, Tilesize))
        
        #print de soldier
        screen.blit(Soldier,(soldierPos[0], soldierPos[1]))
        #print soldier-coordinaten in console
        print("x = ", soldierPos[0], "y = ", soldierPos[1])





        pygame.display.flip()
        clock.tick(60)