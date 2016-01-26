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

    def GenerateRandomBiome():                              #Code door Eljakim, aangepast door Joost
        RandomBiome = random.randrange(0,4)
        if RandomBiome == 0:
            return 'Swamp'
        elif RandomBiome ==  1:
            return 'Ice'
        elif RandomBiome == 2:
            return 'Desert'
        else:
            return 'Forest'
        



