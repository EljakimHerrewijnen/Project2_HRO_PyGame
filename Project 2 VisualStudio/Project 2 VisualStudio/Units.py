import pygame
from Gameloop import *
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


    