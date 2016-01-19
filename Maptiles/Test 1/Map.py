import pygame
#from Node import *

pygame.init()
Tilesize = 40
Mapwidth = 5
Mapheight = 5
screen = pygame.display.set_mode((Mapwidth*Tilesize, Mapheight * Tilesize))
done = False
clock = pygame.time.Clock()

#colours
blue = (132, 112, 255)
white = (255, 250, 250)
green = (34, 139, 34)

#elements
Water = 0
Land = 1
Goldmine = 2

#elements linked to colours
colours = {Water: blue, Land: green, Goldmine: white}

tilelist = [[Land, Land, Water, Land, Land],
            [Land, Land, Water, Land, Land],
            [Water, Water, Goldmine, Water, Water],
            [Land, Land, Water, Land, Land],
            [Land, Land, Water, Land, Land]]

while not done:
    for event in pygame.event.get():    #get all user events
        if event.type == pygame.QUIT:   #Option to quit
            done = True
    for row in range(Mapheight):
        for column in range(Mapwidth):
                pygame.draw.rect(screen, colours[tilelist[row][column]], (column * Tilesize, row * Tilesize, Tilesize, Tilesize))


    pygame.display.flip()
    clock.tick(60)





"""
check_if_true = True
while check_if_true == True:
    x = 0
    y = 0
    for i in range(0, 5):
        for i in range(0,5):
            pygame.draw.rect(screen, blue, pygame.Rect(x, y, 40, 40))
            x += 41
        y -= 41
    if i == 4:
        check_if_true = False
        """