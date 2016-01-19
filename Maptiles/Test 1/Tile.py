import pygame
from Node import *

#colours
blue = (132, 112, 255)
white = (255, 250, 250)
green = (34, 139, 34)

#elements
Water = 0
Land = 1
Goldmine = 2

#elements linked to colours
colours =   {
                Water: blue
                Land: Green
                Goldmine: white
            }

#game dimensions
Tilesize = 40
Mapwidth = 3
Mapheight = 5

class Point:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

class Tile:
  def __init__(self, position, texture, offset, properties):    
