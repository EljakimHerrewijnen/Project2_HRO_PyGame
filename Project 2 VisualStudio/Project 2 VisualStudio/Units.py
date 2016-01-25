import pygame
from Gameloop import *
from Tile import *
from BuyScreen import *

                            #Code van Eljakim
AddUnit = Empty
class Units():
    def __init__(self, id, unittype, position):
        self.id = id
        self.unittype = unittype
        self.position = position

    def BuyTank():
        global AddUnit
        global Clicks
        global currentTile
        Clicks += 1
        if currentTile == 5:
            AddUnit = Node(Units (Clicks, "Tank", 11), AddUnit)
            Player.currency -= 600
            print(AddUnit.Value.id)
            print(AddUnit.Value.unittype)
        else:
            AddUnit = Node(Units (Clicks, "Tank", 11), AddUnit)
            Player.currency -= 750
            print(AddUnit.Value.id)
            print(AddUnit.Value.unittype)

    def BuySoldier():
        global AddUnit
        global Clicks
        Clicks += 1
        global currentTile
        if currentTile == 2:
            AddUnit = Node(Units (Clicks, "Soldier", 11), AddUnit)
            Player.currency -= 120
            print(AddUnit.Value.id)
            print(AddUnit.Value.unittype)
        else:
            AddUnit = Node(Units (Clicks, "Soldier", 11), AddUnit)
            Player.currency -= 150
            print(AddUnit.Value.id)
            print(AddUnit.Value.unittype)
    