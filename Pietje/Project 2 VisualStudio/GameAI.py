import pygame
import sys
from pygame.locals import *
from Tile import *
from Units import *
from Node import *
from Gameloop import *

def RandomMovementsAI():
    RandomNumber1 = random.randrange(0,5)
    

def MovementGenerator(currentPl_id, currentPL_currency, currentPL_biome, currentPl_boats, AmountPlayersDefault):
    global SoldierPos
    RandomNumber1 = random.randrange(0, 4)
    if RandomNumber1 == 0:
        if currentPL_biome == "Swamp":
            SoldierPos[0] += 1
            SoldierPos[1] += 1
            return SoldierPos
        elif currentPL_biome == "Desert":
            SoldierPos[0] += 1
            SoldierPos[1] -= 1
            return SoldierPos  
        elif currentPL_biome == "Ice":
             SoldierPos[0] -= 1
             SoldierPos[1] += 1
             return SoldierPos
        elif currentPL_biome == "Forest":
            SoldierPos[0] -= 1
            SoldierPos[1] -= 1
            return SoldierPos
    elif RandomNumber1 == 1:
        if currentPL_biome == "Swamp":
            SoldierPos[0] += 1
            return SoldierPos
        elif currentPL_biome == "Desert":
            SoldierPos[0] += 1
            return SoldierPos  
        elif currentPL_biome == "Ice":
             SoldierPos[0] -= 1
             return SoldierPos
        elif currentPL_biome == "Forest":
            SoldierPos[0] -= 1
            return SoldierPos
    elif RandomNumber1 == 2:
        if currentPL_biome == "Swamp":
            SoldierPos[1] += 1
            return SoldierPos
        elif currentPL_biome == "Desert":
            SoldierPos[1] -= 1
            return SoldierPos  
        elif currentPL_biome == "Ice":
             SoldierPos[1] += 1
             return SoldierPos
        elif currentPL_biome == "Forest":
            SoldierPos[1] -= 1
            return SoldierPos
    elif RandomNumber1 == 3:
        AddUnit = Units.BuySoldier(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats)
        return AddUnit

def GameAI(currentPl_id, currentPL_currency, currentPL_biome, currentPl_boats, AmountPlayersDefault):
    global SoldierPos
    global TankPos
    global Tilesize
    if AmountPlayersDefault == 4:
        if currentPl_id == 4:  # Check if it is AI 3's turn.
            print("no AI this game")
    elif AmountPlayersDefault == 3:
        if currentPl_id == 4:  # Check if it is AI 3's turn.
            print("Playing the AI")
            if currentPL_currency >= 200:
                AddUnit = Units.BuySoldier(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats)
                currentPL_currency -= 750
                SoldierPos = AddUnit.Value.position
                SoldierPos = MovementGenerator(currentPL_biome, currentPl_id, currentPL_currency, currentPl_boats, AmountPlayersDefault)
                return AddUnit, SoldierPos
            elif currentPL_currency >= 800:
                AddUnit = Units.BuyTank(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats)
                currentPL_currency -= 750
                TankPos = AddUnit.Value.position
                TankPos = MovementGenerator(currentPL_biome, currentPl_id, currentPL_currency, currentPl_boats, AmountPlayersDefault)
                return AddUnit, TankPos
    elif AmountPlayersDefault == 2:
        if currentPl_id == 3:  #Checks if there is an AI needed.
            if currentPL_currency >= 200:
                print("Playing the AI")
                AddUnit = Units.BuySoldier(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats)
                currentPL_currency -= 750
                SoldierPos = AddUnit.Value.position
                SoldierPos = MovementGenerator(currentPL_biome, currentPl_id, currentPL_currency, currentPl_boats, AmountPlayersDefault)
                return AddUnit, SoldierPos
            elif currentPL_currency >= 800:
                AddUnit = Units.BuyTank(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats)
                currentPL_currency -= 750
                TankPos = AddUnit.Value.position
                TankPos = MovementGenerator(currentPL_biome, currentPl_id, currentPL_currency, currentPl_boats, AmountPlayersDefault)
                return AddUnit, TankPos
        if currentPl_id == 4:  # Check if it is AI 3's turn.
            if currentPL_currency >= 200:
                AddUnit = Units.BuySoldier(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats)
                currentPL_currency -= 750
                SoldierPos = AddUnit.Value.position
                return AddUnit, SoldierPos
            elif currentPL_currency >= 800:
                AddUnit = Units.BuyTank(currentPl_id, currentPL_biome, currentPL_currency, currentPl_boats)
                currentPL_currency -= 750
                TankPos = AddUnit.Value.position
                return AddUnit, TankPos