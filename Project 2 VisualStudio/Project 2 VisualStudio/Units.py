import pygame
from Gameloop import *
from Tile import *
from BuyScreen import *

                            #Code van Eljakim

class Units():
    def __init__(self, id, unittype, position):
        self.id = id
        self.unittype = unittype
        self.position = position

    def BuyTank():
        global Clicks
        global currentTile
        if currentTile == 5:
            Units.unittype = "Tank"
            Units.id = Clicks
            Player.currency -= 600
            print(Units.id)
            print(Units.unittype)
        else:
            Units.unittype = "Tank"
            Units.id = Clicks
            Player.currency -= 750
            print(Units.id)
            print(Units.unittype)

    def BuySoldier():
        global Clicks
        global currentTile
        if currentTile == 2:
            Units.unittype = "Soldier"
            Units.id = Clicks
            Player.currency -= 120
            print(Units.id)
            print(Units.unittype)
        else:
            Units.unittype = "Soldier"
            Units.id = Clicks
            Player.currency -= 150
            print(Units.id)
            print(Units.unittype)
    