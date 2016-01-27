import pygame
from Gameloop import *

currentid = 0


def changePlayer():
    global currentid
    currentid += 1
    if currentid > 4:
        currentid = 1
    while Playerslist.IsEmpty == False:
        if Playerslist.Value.Pl_id == currentid:
            currentPl_id = Playerslist.Value.Pl_id
            currentPL_biome = Playerslist.Value.Biome
            currentPL_currency = Playerslist.Value.Currency
            currentPl_soldiers = Playerslist.Value.Soldiers
            currentPl_robots = Playerslist.Value.Robots
            currentPl_tanks = Playerslist.Value.Tanks
            currentPl_barracks = Playerslist.Value.Barracks
            currentPl_boats = Playerslist.Value.Boats
            return currentPl_id, currentPL_biome, currentPL_currency, currentPl_soldiers, currentPl_robots, currentPl_tanks, currentPl_barracks, currentPl_boats
        else:
            Playerslist = Playerslist.Tail