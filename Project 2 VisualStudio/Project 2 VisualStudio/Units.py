import pygame
from Gameloop import *
from Tile import *
from Node import *
from Players import *

# ------------------------------------------------------------------------------------testen door Joost
Texturesize = 42 * 2                       
soldier_texture = pygame.image.load('content/soldier.png')
soldier_texture = pygame.transform.scale(soldier_texture, (Texturesize, Texturesize))
robot_texture = pygame.image.load('content/robot.png')
robot_texture = pygame.transform.scale(robot_texture, (Texturesize, Texturesize))
tank_texture = pygame.image.load('content/tank.tif')
tank_texture = pygame.transform.scale(tank_texture, (Texturesize, Texturesize))
boat_texture = pygame.image.load('content/boat.png')
boat_texture = pygame.transform.scale(boat_texture, (Texturesize, Texturesize))
barrack_texture = pygame.image.load('content/barrack.png')
barrack_texture = pygame.transform.scale(barrack_texture, (Texturesize, Texturesize))      
 
soldier = 0
robot = 1
tank = 2
boat = 3
barrack = 4

unit_textures = {   
    soldier: soldier_texture,
    robot: robot_texture,
    tank: tank_texture,
    boat: boat_texture,
    barrack: barrack_texture,
                }

unit_text = {   
    soldier: "Soldier = f150",
    robot: "Robot = f300",
    tank: "Tank = f750",
    boat: "Boat = f1000",
    barrack: "Barrack = f500",
                }
#--------------------------------------------------------------------------------------------------t/m hier
                #Code van Eljakim

from Tile import *
from BuyScreen import *

                            #Code van Eljakim

id_counter = 0
Position_Unit = 0
AddUnit = Empty
class Units():
    def __init__(self, id, unittype, position, OwnerPlayer):
        self.id = id
        self.unittype = unittype
        self.position = position
        self.OwnerPlayer = OwnerPlayer

    def BuyTank():
<<<<<<< HEAD
        global id_counter
        global Position_Unit
        global CurrentPlayer
=======
>>>>>>> origin/master
        global AddUnit
        id_counter += 1
        AddUnit = Node(Units (id_counter, "Tank", 0, 0), AddUnit)
        print(AddUnit.Value.id)
<<<<<<< HEAD
        print(AddUnit.Value.OwnerPlayer)
=======
        print(AddUnit.Value.unittype)
>>>>>>> origin/master

    def BuySoldier():
        while Playerslist.Value.IsEmpty == False:
            print("nog niks")

        global id_counter
        global Position_Unit
        global CurrentPlayer
        global AddUnit
        id_counter += 1
        AddUnit = Node(Units (id_counter, "Soldier", CurrentPlayer, 1), AddUnit)
        print(AddUnit.Value.id)