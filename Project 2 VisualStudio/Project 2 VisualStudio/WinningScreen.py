import pygame
import time


#Voor Carlo

pygame.intit()

display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
bright_blue = (0, 0, 255)
red = (175,0,0)
green = (0,175,0)
blue = (30,144,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

 
block_color = (53,115,255)

 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Frequency')
clock = pygame.time.Clock()



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def winning_screen():
    winning = True
    while winning is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winning = False
        gameDisplay.fill(white)
        LargeText = pygame.font.Font('freesandsbold.tff', 70)
        TextSurf, TextRect = text_objects('Congratulations, you won!', LargeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gamedisplay.blit(TextSurf, TextRect)

winning_screen()