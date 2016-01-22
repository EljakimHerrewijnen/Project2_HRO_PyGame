import pygame
from Node import *
import random

class Player:
    def __init__(self, id, name, card, Biome, currency):              #Node gemaakt door Joost, aangepast door Eljakim
        self.Pl_id = id
        self.Pl_name = name
        self.Gamecard = card
        self.Biome = Biome
        self.currency = currency

    def GenerateRandomBiome():                              #Code door Eljakim
        RandomBiome = random.randrange(0,4)
        if RandomBiome == 0:
            Player.Biome = 'Forest'
            Player.PL_id = 1
        elif RandomBiome ==  1:
            Player.Biome =  'Ice'
            Player.PL_id = 1
        elif RandomBiome == 2:
            Player.Biome = 'Desert'
            Player.PL_id = 1
        else:
            Player.Biome = 'Swamp'
            Player.PL_id = 1
        Player.currency = 500
        print(Player.currency)
        print(Player.Biome)
        print(Player.PL_id)

        



