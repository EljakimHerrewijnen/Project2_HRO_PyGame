import pygame, sys, random, math
from Players import * 
from Node import *
from pygame.locals import *
from Units import *
from GameAI import *
#from Change_Player import *

#colors
black = (0,0,0)
white = (255,255,255)
poepkleur = (139, 69, 19)
cyan = (0, 255, 255)
currentPL_currency = 0
currentid = 0
Playerlist4 = Empty
currentPl_id = 0
AddUnit = Empty
mouse_Pos = [0, 0]

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

      
def changePlayer(Playerslist3):
    global currentid
    global Playerlist4
    currentid += 1
    if currentid > 4:
        currentid = 1
    while Playerslist3.IsEmpty == False:
        if Playerslist3.Value.Pl_id == currentid:
            currentPl_id = Playerslist3.Value.Pl_id
            currentPL_name = Playerslist3.Value.Pl_name
            currentPL_card = Playerslist3.Value.Gamecard
            currentPL_biome = Playerslist3.Value.Biome
            currentPL_currency = Playerslist3.Value.Currency
            currentPl_soldiers = Playerslist3.Value.Soldiers
            currentPl_robots = Playerslist3.Value.Robots
            currentPl_tanks = Playerslist3.Value.Tanks
            currentPl_barracks = Playerslist3.Value.Barracks
            currentPl_boats = Playerslist3.Value.Boats
            Playerlist4 = Node(Player1(Playerslist3.Value.Pl_id, Playerslist3.Value.Pl_name, Playerslist3.Value.Gamecard, Playerslist3.Value.Biome, Playerslist3.Value.Currency, Playerslist3.Value.Soldiers, Playerslist3.Value.Robots, Playerslist3.Value.Tanks, Playerslist3.Value.Barracks, Playerslist3.Value.Boats), Playerlist4)                     #currentPl_id, currentPL_name, currentPL_card, currentPL_biome, currentPL_currency, currentPl_soldiers, currentPl_robots, currentPl_tanks, currentPl_barracks, currentPl_boats), Playerlist4)
            return Playerlist4  #currentPl_id, currentPL_biome, currentPL_currency, currentPl_soldiers, currentPl_robots, currentPl_tanks, currentPl_barracks, currentPl_boats
        else:
            Playerslist3 = Playerslist3.Tail
            
    

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

currentTile = 0
Movements = 0
CurrentPlayer = 1
"""
def check_For_Other_Units_On_Tile(currentUnitPos, AddUnit):
    nr_Units_On_Tile = 0
    while AddUnit.IsEmpty == False:
        AddUnit = AddUnit.Tail
        if currentUnitPos == AddUnit.Value.position:
            nr_Units_On_Tile += 1
            newTexture = pygame.transform.scale(AddUnit.Value.Texture, (Tilesize * 0.5, Tilesize * 0.5))
            DrawUnits = Node(newTexture, DrawUnits)
        else:
            DrawUnits = Node(AddUnit.Value.Texture, DrawUnits)
            """
def draw2(AddUnit, screen):
    while AddUnit.IsEmpty == False:
        screen.blit(AddUnit.Value.Texture, (AddUnit.Value.position[0] * Tilesize, AddUnit.Value.position[1] * Tilesize))
        
        AddUnit = AddUnit.Tail

    pygame.display.flip()

def draw1(AddUnit, screen, bgmap, soldierPos, font1, transparent_texture, Mapwidth, buy_background):     #simpele draw functie voor units   
    buy_background_2 = pygame.image.load('content/wood_2.jpg')
    buy_background_2 = pygame.transform.scale(buy_background_2, (260, int(260 / 3)))
    screen.blit(buy_background_2, (Mapwidth * Tilesize - 4, 260 + math.floor((260 / 3) * 2)))

    #print map
    screen.blit(bgmap, (0,0))
    pygame.display.update()
    #print buyscreen items
    placePositionY = 10
    placePositionX = Tilesize * 2 + 5
    for i in range(0, 5):
        screen.blit(unit_textures[i], (Mapwidth * Tilesize + 20, placePositionY))
        #Text = font1.render(str(unit_text[i]), True, black, kots)
        #screen.blit(Text, (Mapwidth * Tilesize + 20 + placePositionX, placePositionY + 0.5 * Tilesize))
        placePositionY += Tilesize * 2

    #print wie er aan de beurt is
    Text = font1.render("Player " + str(currentPl_id) + "'s turn", True, black, transparent_texture)
    screen.blit(Text, (Mapwidth * Tilesize + 20, placePositionY + 20))
    Text2 = font1.render("Player " + str(currentPl_id) + "'s gold: " + str(currentPL_currency), True, black, transparent_texture)
    screen.blit(Text2, (Mapwidth * Tilesize + 20, placePositionY + 40))
    
    pygame.display.flip()
    


def draw(AddUnit, screen, soldierPos):      #draw functie voor units
    while AddUnit.IsEmpty == False:
        currentUnitPos = [AddUnit.Value.position[0], AddUnit.Value.position[1]]
        nr_Units_On_Tile = 0
        while AddUnit.IsEmpty == False:
            AddUnit = AddUnit.Tail
            if currentUnitPos == AddUnit.Value.position:
                nr_Units_On_Tile += 1
                newTexture = pygame.transform.scale(AddUnit.Value.Texture, (Tilesize * 0.5, Tilesize * 0.5))
                if nr_Units_On_Tile == 1:
                    screen.blit(AddUnit.Value.Texture, (AddUnit.Value.position[0] * Tilesize, AddUnit.Value.position[1] * Tilesize))
                if nr_Units_On_Tile == 2:
                    screen.blit(AddUnit.Value.Texture, (AddUnit.Value.position[0] * Tilesize + Tilesize * 0.5, AddUnit.Value.position[1] * Tilesize))
                if nr_Units_On_Tile == 3:
                    screen.blit(AddUnit.Value.Texture, (AddUnit.Value.position[0] * Tilesize + Tilesize, AddUnit.Value.position[1] * Tilesize + Tilesize * 0.5))
                #DrawUnits = Node(newTexture, DrawUnits)
            else:
                #DrawUnits = Node(AddUnit.Value.Texture, DrawUnits)
                screen.blit(AddUnit.Value.Texture, (AddUnit.Value.position[0] * Tilesize, AddUnit.Value.position[1] * Tilesize))
        screen.blit(AddUnit.Value.Texture, (AddUnit.Value.position[0] * Tilesize, AddUnit.Value.position[1] * Tilesize))
        if nr_Units_On_Tile == 1:
            screen.blit(AddUnit.Value.Texture, (AddUnit.Value.position[0] * Tilesize, AddUnit.Value.position[1] * Tilesize))
        if nr_Units_On_Tile == 2:
            screen.blit(AddUnit.Value.Texture, (AddUnit.Value.position[0] * Tilesize + Tilesize * 0.5, AddUnit.Value.position[1] * Tilesize))
        if nr_Units_On_Tile == 3:
            screen.blit(AddUnit.Value.Texture, (AddUnit.Value.position[0] * Tilesize + Tilesize, AddUnit.Value.position[1] * Tilesize + Tilesize * 0.5))

        pygame.display.flip()
        #AddUnit = AddUnit.Tail

def wait(Mapwidth):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #if event.type == KEYDOWN and event.key == K_f:
            if pygame.mouse.get_pressed()[2] and pygame.mouse.get_pos()[0] < (Mapwidth * Tilesize):
                mouse_x_new = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
                mouse_y_new = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
                mouse_Pos_New = [mouse_x_new, mouse_y_new]
                return mouse_Pos_New

def tile_loop(Playerslist2):
    global currentTile
    global Movements
    global CurrentPlayer
    global currentPl_id
    global currentPL_currency
    global AddUnit
    global mouse_Pos
    
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
    #screen.blit(bgmap, (0, 0)) 
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
    MaxMovement_texture = pygame.image.load('content/soldier_texture.tif')
    MaxMovement_texture = pygame.transform.scale(MaxMovement_texture, (Texturesize, Texturesize))

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

    # dit zet de tiles op de goede plek
    for row in range(Mapheight):
        for column in range(Mapwidth):
                screen.blit(textures[tilelist[row][column]], (column * Tilesize, row * Tilesize))  #, Tilesize, Tilesize))
    
    #Background buyscreen
    placeBackground = 0
    for i in range(0, 3):
        screen.blit(buy_background, (Mapwidth * Tilesize, placeBackground))
        placeBackground += 260
        #als de muis over tekst heen gaat verkleurt de achtergrond van de text
            
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

            #Battle Code
            if AddUnit.IsEmpty is False:
                APlayersPosition = AddUnit.Value
                print("Searching for a battle...")
                if APlayersPosition == AddUnit.Value.position:
                    APlayersPosition2 = AddUnit.Value
                    APlayersPosition2.Value.DefenceValue - APlayersPosition.Value.AttackValue
                    APlayersPosition.Value.DefenceValue - APlayersPosition2.Value.AttackValue
                    BattleCounter = 0
                    if APlayersPosition.DefenceValue >= 1:
                        AddUnit.Value -= APlayersPosition2
                    else: 
                        AddUnit.Value -= APlayersPosition
                elif APlayersPosition is not AddUnit.Value.position:
                        APlayersPosition = AddUnit.Tail
            # if a key is pressed move the soldier
            if event.type == KEYDOWN: #and soldierPos[0] < Mapwidth * Tilesize - Tilesize:
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
                currentTile = tilelist[mouse_y][mouse_x]
                print("Water = 0/Goldmine = 1/Forest = 2/Ice = 3/Swamp = 4/Desert = 5: ", currentTile)
        
            copy_AddUnit = Empty
            if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] < (Mapwidth * Tilesize):
                mouse_x = math.floor(pygame.mouse.get_pos()[0] / Tilesize) * Tilesize
                mouse_y = math.floor(pygame.mouse.get_pos()[1] / Tilesize) * Tilesize
                soldierPos = [mouse_x, mouse_y]
                mouse_x = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
                mouse_y = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
                mouse_Pos = [mouse_x, mouse_y]
            while AddUnit.IsEmpty == False:
                #if pygame.mouse.get_pressed()[0]: #and pygame.mouse.get_pos()[0] < (Mapwidth * Tilesize):
                    #mouse_x = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
                    #mouse_y = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
                    #mouse_Pos = [mouse_x, mouse_y]
                print(mouse_Pos[0], mouse_Pos[1])
                if mouse_Pos == AddUnit.Value.position:
                    print("Hier staat een unit: " + AddUnit.Value.unittype + " met id: " + str(AddUnit.Value.id))
                    mouse_Pos_New = wait(Mapwidth)
                    AddUnit.Value.position = mouse_Pos_New
                    #draw1(AddUnit, screen, bgmap, soldierPos, font1, transparent_texture, Mapwidth, buy_background)
                    #draw2(AddUnit, screen)
                    print("klaar met wachten")
                    #AddUnit.Value.position[0] += 1
                    #if pygame.mouse.get_pressed()[2] and pygame.mouse.get_pos()[0] < (Mapwidth * Tilesize):
                    #    mouse_x_new = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
                    #    mouse_y_new = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
                    #    AddUnit.Value.position = [mouse_x_new, mouse_y_new]
                copy_AddUnit = Node(AddUnit.Value, copy_AddUnit)
                draw1(AddUnit, screen, bgmap, soldierPos, font1, transparent_texture, Mapwidth, buy_background)
                draw2(copy_AddUnit, screen)
                AddUnit = AddUnit.Tail
                
        """
            #print(mouse_Pos[0], mouse_Pos[1])
            SeeMaxMovement = Empty
            
        while AddUnit.IsEmpty == False:
            #if pygame.mouse.get_pressed()[0]: #and pygame.mouse.get_pos()[0] < (Mapwidth * Tilesize):
                #mouse_x = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
                #mouse_y = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
                #mouse_Pos = [mouse_x, mouse_y]
            print(mouse_Pos[0], mouse_Pos[1])
            if mouse_Pos == AddUnit.Value.position:
                print("Hier staat een unit: " + AddUnit.Value.unittype)
                mouse_Pos_New = wait(Mapwidth)
                
                AddUnit.Value.position = mouse_Pos_New
                print("klaar met wachten")
                #AddUnit.Value.position[0] += 1
                if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] < (Mapwidth * Tilesize):
                    mouse_x_new = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
                    mouse_y_new = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
                    AddUnit.Value.position = [mouse_x_new, mouse_y_new]
            #if mouse_Pos == AddUnit.Value.position:
            #    mouse_x_new = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
            #    mouse_y_new = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
            #    SeeMaxMovement = mouse_x_new
            #    SeeMaxMovement = mouse_y_new
            #    screen.blit(MaxMovement_texture, (SeeMaxMovement[0] * Mapwidth * 2, SeeMaxMovement[1] * Mapwidth * 2))
            #    print("Wie dit leest is gek")
                #if pygame.mouse.get_pressed()[2] and pygame.mouse.get_pos()[0] < (Mapwidth * Tilesize):
                #    mouse_x_new = math.floor(pygame.mouse.get_pos()[0] / Tilesize)
                #    mouse_y_new = math.floor(pygame.mouse.get_pos()[1] / Tilesize)
                #    AddUnit.Value.position = [mouse_x_new, mouse_y_new]
            AddUnit = AddUnit.Tail
            """
        """
        for row in range(Mapheight):
            for column in range(Mapwidth):
                    screen.blit(textures[tilelist[row][column]], (column * Tilesize, row * Tilesize))  #, Tilesize, Tilesize))
                    
        #Background buyscreen
        placeBackground = 0
        for i in range(0, 3):
            screen.blit(buy_background, (Mapwidth * Tilesize, placeBackground))
            placeBackground += 260
        #als de muis over tekst heen gaat verkleurt de achtergrond van de text
                """
        mouse = pygame.mouse.get_pos()  
        click = pygame.mouse.get_pressed()

        if 865 + 124 > mouse[0] > 865 and 31 + 19 > mouse[1] > 31:          #soldier
            pygame.draw.rect(screen, cyan, (865,31,124,19))    
            if click[0] == 1:
                #screen.blit(bgmap, (0,0))
                pygame.time.delay(300)
                if currentPL_biome == "Ice" and currentPL_currency >= 120:
                    currentPL_currency -= 120
                    print(currentPL_currency)
                    AddUnit = Units.BuySoldier(currentPl_id, currentPL_biome, currentPL_currency)
                elif currentPL_currency >= 150:
                    currentPL_currency -= 150
                    AddUnit = Units.BuySoldier(currentPl_id, currentPL_biome, currentPL_currency)
                else:
                    print("You do not have enough gold!")
                pygame.time.delay(300)
        else:
            pygame.draw.rect(screen, white, (865,31,124,19))
        textSurf, textRect = text_objects('Soldier = f150', font1)
        textRect.center = ( (865+(124/2)), (34+(7.5)) )
        screen.blit(textSurf, textRect)
        
        if 865 + 124 > mouse[0] > 865 and 115 + 19 > mouse[1] > 115:        #robot
            pygame.draw.rect(screen, cyan, (865,115,124,19))    
            if click[0] == 1:
                if currentPL_biome == "Forest" and currentPL_currency >= 120:
                    currentPL_currency -= 240
                    AddUnit = Units.BuyRobot(currentPl_id, currentPL_biome, currentPL_currency)
                    RobotPos = AddUnit.Value.position
                    #screen.blit(robot_texture, (RobotPos[0] * Mapwidth * 2, RobotPos[1]* Mapheight * 2))
                elif currentPL_currency >= 150:
                    currentPL_currency -= 300
                    AddUnit = Units.BuyRobot(currentPl_id, currentPL_biome, currentPL_currency)
                    RobotPos = AddUnit.Value.position
                    #screen.blit(robot_texture, (RobotPos[0] * Mapwidth * 2, RobotPos[1]* Mapheight * 2))
                else:
                    print("You do not have enough gold!")
                pygame.time.delay(300)
        else:
            pygame.draw.rect(screen, white, (865,115,124,19))
        textSurf, textRect = text_objects('Robot = f300', font1)
        textRect.center = ( (865+(124/2)), (115+(9)) )
        screen.blit(textSurf, textRect)

        if 865 + 124 > mouse[0] > 865 and 199 + 19 > mouse[1] > 199:        #tank
            pygame.draw.rect(screen, cyan, (865,199,124,19))    
            if click[0] == 1:  
                if currentPL_biome == "Desert" and currentPL_currency >= 500:
                    AddUnit = Units.BuyTank(currentPl_id, currentPL_biome, currentPL_currency)   
                    currentPL_currency -= 500
                    TankPos = AddUnit.Value.position
                    #screen.blit(tank_texture, (TankPos[0] * Mapwidth * 2, TankPos[1]* Mapheight * 2))
                elif currentPL_currency >= 750:
                    AddUnit = Units.BuyTank(currentPl_id, currentPL_biome, currentPL_currency)   
                    currentPL_currency -= 750
                    TankPos = AddUnit.Value.position
                    #screen.blit(tank_texture, (TankPos[0] * Mapwidth * 2, TankPos[1]* Mapheight * 2))
                else:
                    print("You do not have enough gold!")        
                pygame.time.delay(300)        
        else:
            pygame.draw.rect(screen, white, (865,199,124,19))
        textSurf, textRect = text_objects('Tank = f750', font1)
        textRect.center = ( (865+(124/2)), (199+(9)) )
        screen.blit(textSurf, textRect)
        
        if 865 + 124 > mouse[0] > 865 and 283 + 19 > mouse[1] > 283:        #boat
            pygame.draw.rect(screen, cyan, (865,283,124,19))    
            if click[0] == 1:
                if currentPL_biome == "Swamp" and currentPL_currency >= 800:
                    currentPL_currency -= 800
                    AddUnit = Units.BuyBoat(currentPl_id, currentPL_biome, currentPL_currency)
                    BoatPos = AddUnit.Value.position
                    #screen.blit(boat_texture, (BoatPos[0] * Mapwidth * 2, BoatPos[1]* Mapheight * 2))
                elif currentPL_currency >= 1000:
                    currentPL_currency = currentPL_currency - 1000
                    AddUnit = Units.BuyBoat(currentPl_id, currentPL_biome, currentPL_currency)
                    BoatPos = AddUnit.Value.position
                    #screen.blit(boat_texture, (BoatPos[0] * Mapwidth * 2, BoatPos[1]* Mapheight * 2))
                else:
                    print("You do not have enough gold!")
                pygame.time.delay(300)
        else:
            pygame.draw.rect(screen, white, (865,283,124,19))
        textSurf, textRect = text_objects('Boat = f1000', font1)
        textRect.center = ( (865+(124/2)), (283+(9)) )
        screen.blit(textSurf, textRect)
        
        if 865 + 124 > mouse[0] > 865 and 367 + 19 > mouse[1] > 367:        #barrack
            pygame.draw.rect(screen, cyan, (865,367,124,19))  
            if click[0] == 1:
                AddUnit = Units.BuyBarrack(currentPl_id, currentPL_biome, currentPL_currency)
                #screen.blit(barrack_texture, (AddUnit.Value.position[0] * Tilesize, AddUnit.Value.position[1] * Tilesize)) 
                BarrackPos = AddUnit.Value.position    
                pygame.time.delay(300)
                if currentPL_currency >= 500:
                    currentPL_currency -= 500
                    AddUnit = Units.BuyBarrack(currentPl_id, currentPL_biome, currentPL_currency)
                    BarrackPos = AddUnit.Value.position
                    #screen.blit(barrack_texture, (TankPos[0] * Mapwidth * 2, TankPos[1]* Mapheight * 2))              
                else:
                    print("You do not have enough gold!")
                pygame.time.delay(300)
        else:
            pygame.draw.rect(screen, white, (865,367,124,19))
        textSurf, textRect = text_objects('Barrack = f500', font1)
        textRect.center = ( (865+(124/2)), (367+(9)) )
        screen.blit(textSurf, textRect)   
        
        copy2_AddUnit = AddUnit
        if 865 + 124 > mouse[0] > 865 and 700 + 19 > mouse[1] > 700:        #end turn, klik hier op om de volgende speler de beurt te geven
            pygame.draw.rect(screen, cyan, (865,700,124,19)) 
            if click[0] == 1:
                screen.blit(bgmap, (0,0))
                currentPlayerList = changePlayer(Playerslist2)
                currentPl_id = currentPlayerList.Value.Pl_id
                currentPL_name = currentPlayerList.Value.Pl_name
                currentPL_card = currentPlayerList.Value.Gamecard
                currentPL_biome = currentPlayerList.Value.Biome
                currentPL_currency = currentPlayerList.Value.Currency
                currentPl_soldiers = currentPlayerList.Value.Soldiers
                currentPl_robots = currentPlayerList.Value.Robots
                currentPl_tanks = currentPlayerList.Value.Tanks
                currentPl_barracks = currentPlayerList.Value.Barracks
                currentPl_boats = currentPlayerList.Value.Boats
                #global currentPl_id
                print("Player id = " + str(currentPl_id) + " Player name = " + currentPL_name)
                draw1(AddUnit, screen, bgmap, soldierPos, font1, transparent_texture, Mapwidth, buy_background)
                draw2(copy2_AddUnit, screen)
                pygame.time.delay(1000)
                GameAI(currentPl_id, currentPL_currency, currentPL_biome)
        else:
            pygame.draw.rect(screen, white, (865,700,124,19))
        textSurf, textRect = text_objects('End Turn!', font1)
        textRect.center = ( (865+(124/2)), (700+(9)) )
        screen.blit(textSurf, textRect) 
        #draw1(AddUnit, screen, bgmap, soldierPos, font1, transparent_texture, Mapwidth, buy_background)

        '''
        def Draw():
            Texturesize = 40
            Tilesize = Texturesize + 2
            Mapwidth = 18
            Mapheight = 18 
            screen = pygame.display.set_mode((Mapwidth * Tilesize + 250, Mapheight * Tilesize))
            bgmap = pygame.image.load("content/map895.jpg")
            bgmap = pygame.transform.scale(bgmap, (Mapwidth * Tilesize, Mapheight * Tilesize))
            screen.blit(bgmap, (0,0))
            if AddUnit.Value.unittype is "Tank":
                TankPos = AddUnit.Value.position
                screen.blit(soldier_texture, (AddUnit.Value.position[0] * Mapwidth * 2, AddUnit.Value.position[1] * Mapheight * 2))  
                while TankPos is [] is False:
                    screen.blit(soldier_texture, (TankPos[0] * Mapwidth * 2, TankPos[1] * Mapheight * 2))  
                    TankPos = AddUnit.Tail
            elif AddUnit.Value.unittype == "Soldier":
                SoldierPos = AddUnit.Value.position
                screen.blit(soldier_texture, (SoldierPos[0] * Mapwidth * 2, SoldierPos[1] * Mapheight * 2))  
            elif AddUnit.Value.unittype == "Boat":
                BoatPos = AddUnit.Value.position
                screen.blit(boat_texture, (BoatPos[0] * Mapwidth * 2, BoatPos[1] * Mapheight * 2))  
            elif AddUnit.Value.unittype == "Barrack":
                BarrackPos = AddUnit.Value.position
                screen.blit(barrack_texture, (BarrackPos[0] * Mapwidth * 2, BarrackPos[1] * Mapheight * 2))  
            elif AddUnit.Value.unittype == "Robot":
                RobotPos = AddUnit.Value.position
                screen.blit(robot_texture, (RobotPos[0] * Mapwidth * 2, RobotPos[1] * Mapheight * 2))
                '''

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
            unit_textures_buyScreen = pygame.transform.scale(unit_textures[i], (Tilesize * 2, Tilesize * 2))
            screen.blit(unit_textures[i], (Mapwidth * Tilesize + 20, placePositionY))
            #Text = font1.render(str(unit_text[i]), True, black, kots)
            #screen.blit(Text, (Mapwidth * Tilesize + 20 + placePositionX, placePositionY + 0.5 * Tilesize))
            placePositionY += Tilesize * 2

        """
        #print wie er aan de beurt is
        Text = font1.render("Player " + str(currentPl_id) + "'s turn", True, black, transparent_texture)
        screen.blit(Text, (Mapwidth * Tilesize + 20, placePositionY + 20))
        Text2 = font1.render("Player " + str(currentPl_id) + "'s gold: " + str(currentPL_currency), True, black, transparent_texture)
        screen.blit(Text2, (Mapwidth * Tilesize + 20, placePositionY + 40))
            """
        #print de soldier
        #screen.blit(Soldier,(soldierPos[0], soldierPos[1]))
        #print soldier-coordinaten in console
        #print("x = ", soldierPos[0], "y = ", soldierPos[1])

        #draw1(AddUnit, screen, bgmap, soldierPos, font1, transparent_texture, Mapwidth, buy_background)
        draw2(AddUnit, screen)
        pygame.display.flip()
        clock.tick(30)

    '''
            elif AddUnit.Value.unittype == "Soldier":
                SoldierPos = AddUnit.Value.position
                screen.blit(soldier_texture, (SoldierPos[0] * Mapwidth * 2, SoldierPos[1] * Mapheight * 2))  
            elif AddUnit.Value.unittype == "Boat":
                BoatPos = AddUnit.Value.position
                screen.blit(boat_texture, (BoatPos[0] * Mapwidth * 2, BoatPos[1] * Mapheight * 2))  
            elif AddUnit.Value.unittype == "Barrack":
                BarrackPos = AddUnit.Value.position
                screen.blit(barrack_texture, (BarrackPos[0] * Mapwidth * 2, BarrackPos[1] * Mapheight * 2))  
            elif AddUnit.Value.unittype == "Robot":
                RobotPos = AddUnit.Value.position
                screen.blit(robot_texture, (RobotPos[0] * Mapwidth * 2, RobotPos[1] * Mapheight * 2))
                '''