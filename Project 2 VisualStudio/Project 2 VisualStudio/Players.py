import pygame
from Node import *
import random

class Player1:
    def __init__(self, id, name, card, Biome, currency):              #Node gemaakt door Joost, aangepast door Eljakim
        self.Pl_id = id
        self.Pl_name = name
        self.Gamecard = card
        self.Biome = Biome
        self.currency = currency

    def GenerateRandomBiome(self):                              #Code door Eljakim, aangepast door Joost
        RandomBiome = random.randrange(0,4)
        if RandomBiome == 0:
            self.Biome = 'Swamp'
        elif RandomBiome ==  1:
            self.Biome =  'Ice'
        elif RandomBiome == 2:
            self.Biome = 'Desert'
        else:
            self.Biome = 'Forest'
        return self.Biome


class Player2:
    def __init__(self, id, name, card, Biome, currency):              #Node gemaakt door Joost, aangepast door Eljakim
        self.Pl_id = id
        self.Pl_name = name
        self.Gamecard = card
        self.Biome = Biome
        self.currency = currency

    def GenerateRandomBiome():                              #Code door Eljakim
        RandomBiome = random.randrange(0,4)
        if RandomBiome == 0:
            Player2.Biome = 'Forest'
            Player2.PL_id = 1
        elif RandomBiome ==  1:
            Player2.Biome =  'Ice'
            Player2.PL_id = 1
        elif RandomBiome == 2:
            Player2.Biome = 'Desert'
            Player2.PL_id = 1
        else:
            Player2.Biome = 'Swamp'
            Player2.PL_id = 1
        Player2.currency = 500
        print(Player2.currency)
        print(Player2.Biome)
        print(Player2.PL_id)

        
        



