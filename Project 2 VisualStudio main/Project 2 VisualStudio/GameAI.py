import pygame
import sys
from pygame.locals import *
from Tile import *
from Units import *
from Node import *
from Gameloop import *

def GameAI(currentPl_id, currentPL_currency, currentPL_biome):
    if currentPl_id == 2:  #Checks if there is an AI needed.
        if currentPL_currency >= 200:
            AddUnit = Units.BuySoldier(currentPl_id, currentPL_biome, currentPL_currency)
            currentPL_currency -= 750
            SoldierPos = AddUnit.Value.position
            return AddUnit, SoldierPos
        elif currentPL_currency >= 800:
            AddUnit = Units.BuyTank(currentPl_id, currentPL_biome, currentPL_currency)
            currentPL_currency -= 750
            SoldierPos = AddUnit.Value.position
            return AddUnit, SoldierPos
    if currentPl_id == 3:  # Check if it is AI 3's turn.
        if currentPL_currency >= 200:
            AddUnit = Units.BuySoldier(currentPl_id, currentPL_biome, currentPL_currency)
            currentPL_currency -= 750
            SoldierPos = AddUnit.Value.position
            return AddUnit, SoldierPos
        elif currentPL_currency >= 800:
            AddUnit = Units.BuyTank(currentPl_id, currentPL_biome, currentPL_currency)
            currentPL_currency -= 750
            SoldierPos = AddUnit.Value.position
            return AddUnit, SoldierPos
    elif currentPl_id == 3:
        if currentPL_currency >= 200:
            AddUnit = Units.BuySoldier(currentPl_id, currentPL_biome, currentPL_currency)
            currentPL_currency -= 750
            SoldierPos = AddUnit.Value.position
            return AddUnit, SoldierPos
        elif currentPL_currency >= 800:
            AddUnit = Units.BuyTank(currentPl_id, currentPL_biome, currentPL_currency)
            currentPL_currency -= 750
            SoldierPos = AddUnit.Value.position
            return AddUnit, SoldierPos