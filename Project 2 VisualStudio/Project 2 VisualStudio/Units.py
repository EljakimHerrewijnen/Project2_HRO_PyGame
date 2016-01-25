import pygame
from Gameloop import *

# ------------------------------------------------------------------------------------testen door Joost
Texturesize = 42 * 2                       
soldier_texture = pygame.image.load('content/soldier.png')
soldier_texture = pygame.transform.scale(soldier_texture, (Texturesize, Texturesize))
robot_texture = pygame.image.load('content/robot.png')
robot_texture = pygame.transform.scale(robot_texture, (Texturesize, Texturesize))
tank_texture = pygame.image.load('content/tank.png')
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
class Units():
    def __init__(self, id, unittype, position):
        self.id = id
        self.unittype = unittype
        self.position = position

    def UnitPrice():
        if Player.Biome is "Desert":
            print("Desert")
        elif Player.Biome is "Swamp":
            print("Swamp")
        else:
            print("Iets anders")


    