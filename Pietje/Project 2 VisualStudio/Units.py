import pygame
from Gameloop import *
from Tile import *
from Node import *
from Players import *

# ------------------------------------------------------------------------------------testen door Joost
Tilesize = 42 #* 2                       
soldier_texture = pygame.image.load('content/soldier.png')
soldier_texture = pygame.transform.scale(soldier_texture, (Tilesize, Tilesize))
robot_texture = pygame.image.load('content/robot.png')
robot_texture = pygame.transform.scale(robot_texture, (Tilesize, Tilesize))
tank_texture = pygame.image.load('content/tank.tif')
tank_texture = pygame.transform.scale(tank_texture, (Tilesize, Tilesize))
boat_texture = pygame.image.load('content/boat.png')
boat_texture = pygame.transform.scale(boat_texture, (Tilesize, Tilesize))
barrack_texture = pygame.image.load('content/barrack.png')
barrack_texture = pygame.transform.scale(barrack_texture, (Tilesize, Tilesize))      
 
soldier = 0
robot = 1
tank = 2
boat = 3
barrack = 4


#AmountBoats 
AmountBoatsPL1 = 0
AmountBoatsPL2 = 0
AmountBoatsPL3 = 0
AmountBoatsPL4 = 0
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

AddUnit = Empty

#To get the position, this is where in the 5 biomes the unit should spawn.
def GetBiomePosition(currentPL_biome, Type, currentPl_boats):
    if Type == "Boat":
        if currentPL_biome == "Desert":
            if currentPl_boats == 0:
                return [5, 11]
            elif currentPl_boats == 1:
                return [4, 10]
            elif currentPl_boats == 2:
                return [6, 12]
            else:
                return [7, 13]
        elif currentPL_biome == "Swamp":
            if currentPl_boats == 0:
                return [5, 6]
            elif currentPl_boats == 1:
                return [6, 5]
            elif currentPl_boats == 2:
                return [7, 4]
            else:
                return [4, 7]
        elif currentPL_biome == "Forest":
            if currentPl_boats == 0:
                return [13, 10]
            elif currentPl_boats == 1:
                return [11, 12]
            elif currentPl_boats == 2:
                return [12, 11]
            else:
                return [10, 13]
        elif currentPL_biome == "Ice":
            if currentPl_boats == 0:
                return [11, 5]
            elif currentPl_boats == 1:
                return [12, 6]
            elif currentPl_boats == 2:
                return [13, 7]
            else:
                return [10, 4]
    else:
        if currentPL_biome == "Desert":
            return [0, 17]
        elif currentPL_biome == "Swamp":
            return [0,0]
        elif currentPL_biome == "Forest":
            return [17, 17]
        elif currentPL_biome == "Ice":
            return [17, 0]

class Units():
    def __init__(self, id, unittype, position, OwnerPlayer, texture, AttackValue, DefenceValue):
        self.id = id
        self.unittype = unittype
        self.position = position
        self.OwnerPlayer = OwnerPlayer
        self.Texture = texture
        self.AttackValue = AttackValue
        self.DefenceValue = DefenceValue

    def BuyTank(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats):  
        AmountBoats = 0
        global id_counter
        Type = "Tank"
        Position_Unit = GetBiomePosition(currentPL_biome, Type, currentPl_boats)
        global AddUnit
        id_counter += 1
        AddUnit = Node(Units(id_counter, "Tank", Position_Unit, currentPl_id, tank_texture, 2, 2), AddUnit)
        
        print("Unitid = " + str(AddUnit.Value.id))
        print("Unittype = " + str(AddUnit.Value.unittype))
        print("UnitOwnerid = " + str(AddUnit.Value.OwnerPlayer))
        print("Unit Position = "+ str(AddUnit.Value.position))
        print(currentPL_biome)
        print(currentPL_currency)
        return AddUnit

    def BuySoldier(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats):
        AmountBoats = 0
        global id_counter
        Type = "Soldier"
        Position_Unit = GetBiomePosition(currentPL_biome, Type, currentPl_boats)
        global AddUnit
        id_counter += 1
        AddUnit = Node(Units(id_counter, "Soldier", Position_Unit, currentPl_id, soldier_texture,1 ,1), AddUnit)
        
        print("Unitid = " + str(AddUnit.Value.id))
        print("Unittype = " + str(AddUnit.Value.unittype))
        print("UnitOwnerid = " + str(AddUnit.Value.OwnerPlayer))
        print("Unit Position = "+ str(AddUnit.Value.position))
        print(currentPL_biome)
        print(currentPL_currency)
        return AddUnit

    def BuyRobot(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats):
        AmountBoats = 0
        global id_counter
        Type = "Robot"
        Position_Unit = GetBiomePosition(currentPL_biome, Type, currentPl_boats)
        global AddUnit
        id_counter += 1
        AddUnit = Node(Units(id_counter, "Robot", Position_Unit, currentPl_id, robot_texture, 2, 2), AddUnit)
        
        print("Unitid = " + str(AddUnit.Value.id))
        print("Unittype = " + str(AddUnit.Value.unittype))
        print("UnitOwnerid = " + str(AddUnit.Value.OwnerPlayer))
        print("Unit Position = "+ str(AddUnit.Value.position))
        print(currentPL_biome)
        print(currentPL_currency)
        return AddUnit

    def BuyBoat(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats):
        global id_counter
        global AddUnit
        #global AmountBoatsPL1 
        #global AmountBoatsPL2 
        #global AmountBoatsPL3 
        #global AmountBoatsPL4 
        #AmountBoats = 0

        #if currentPl_id == 1:
        #    if AmountBoatsPL1 >= 4:
        #        print("You cant buy more!")
        #    else:
        #        AmountBoatsPL1 += 1
        #        AmountBoats = AmountBoatsPL1
        #if currentPl_id == 2:
        #    if AmountBoatsPL2 >= 4:
        #        print("You cant buy more!")
        #    else:
        #        AmountBoatsPL2 += 1
        #        AmountBoats = AmountBoatsPL2
        #if currentPl_id == 3:
        #    if AmountBoatsPL3 >= 4:
        #        print("You cant buy more!")
        #    else:
        #        AmountBoatsPL3 += 1
        #        AmountBoats = AmountBoatsPL3
        #if currentPl_id == 4:
        #    if AmountBoatsPL4 >= 4:
        #        print("You cant buy more!")
        #    else:
        #        AmountBoatsPL4 += 1
        #        AmountBoats = AmountBoatsPL4
        Type = "Boat"
        Position_Unit = GetBiomePosition(currentPL_biome, Type, currentPl_boats)
        id_counter += 1
        AddUnit = Node(Units(id_counter, "Boat", Position_Unit, currentPl_id, boat_texture, 0, 6), AddUnit)
        
        print("Unitid = " + str(AddUnit.Value.id))
        print("Unittype = " + str(AddUnit.Value.unittype))
        print("UnitOwnerid = " + str(AddUnit.Value.OwnerPlayer))
        print("Unit Position = "+ str(AddUnit.Value.position))
        print(currentPL_biome)
        print(currentPL_currency)
        return AddUnit

    def BuyBarrack(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats):
        AmountBoats = 0
        global id_counter
        Type = "Barrack"
        Position_Unit = GetBiomePosition(currentPL_biome, Type, currentPl_boats)
        global AddUnit
        id_counter += 1
        AddUnit = Node(Units(id_counter, "Barrack", Position_Unit, currentPl_id, barrack_texture, 0, 6), AddUnit)
        
        print("Unitid = " + str(AddUnit.Value.id))
        print("Unittype = " + str(AddUnit.Value.unittype))
        print("UnitOwnerid = " + str(AddUnit.Value.OwnerPlayer))
        print("Unit Position = "+ str(AddUnit.Value.position))
        print(currentPL_biome)
        print(currentPL_currency)
        return AddUnit

'''
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
                '''