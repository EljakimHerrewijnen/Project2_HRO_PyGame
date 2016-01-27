# input lib
from pygame.locals import *
import pygame, string

class ConfigError(KeyError): pass

class Config:
    """ A utility for configuration """
    def __init__(self, options, *look_for):
        assertions = []
        for key in look_for:
            if key[0] in options.keys(): exec('self.'+key[0]+' = options[\''+key[0]+'\']')
            else: exec('self.'+key[0]+' = '+key[1])
            assertions.append(key[0])
        for key in options.keys():
            if key not in assertions: raise ConfigError(key+' not expected as option')

class Input:
    """ A text input for pygame apps """
    def __init__(self, **options):
        """ Options: x, y, font, color, restricted, maxlength, prompt """
        self.options = Config(options, ['x', '0'], ['y', '0'], ['font', 'pygame.font.Font(None, 32)'],
                              ['color', '(0,0,0)'], ['restricted', '\'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\\\'()*+,-./:;<=>?@[\]^_`{|}~\''],
                              ['maxlength', '-1'], ['prompt', '\'\''])
        self.x = self.options.x; self.y = self.options.y
        self.font = self.options.font
        self.color = self.options.color
        self.restricted = self.options.restricted
        self.maxlength = self.options.maxlength
        self.prompt = self.options.prompt; self.value = ''
        self.shifted = False

    def set_pos(self, x, y):
        """ Set the position to x, y """
        self.x = x
        self.y = y

    def set_font(self, font):
        """ Set the font for the input """
        self.font = font

    def draw(self, surface):
        """ Draw the text input to a surface """
        text = self.font.render(self.prompt+self.value, 1, self.color)
        surface.blit(text, (self.x, self.y))

    def update(self, events):
        """ Update the input based on passed events """
        for event in events:
            if event.type == KEYUP:
                if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = False
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE: self.value = self.value[:-1]
                elif event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = True
                elif event.key == K_SPACE: self.value += ' '
                if not self.shifted:
                    if event.key == K_a and 'a' in self.restricted: self.value += 'a'
                    elif event.key == K_b and 'b' in self.restricted: self.value += 'b'
                    elif event.key == K_c and 'c' in self.restricted: self.value += 'c'
                    elif event.key == K_d and 'd' in self.restricted: self.value += 'd'
                    elif event.key == K_e and 'e' in self.restricted: self.value += 'e'
                    elif event.key == K_f and 'f' in self.restricted: self.value += 'f'
                    elif event.key == K_g and 'g' in self.restricted: self.value += 'g'
                    elif event.key == K_h and 'h' in self.restricted: self.value += 'h'
                    elif event.key == K_i and 'i' in self.restricted: self.value += 'i'
                    elif event.key == K_j and 'j' in self.restricted: self.value += 'j'
                    elif event.key == K_k and 'k' in self.restricted: self.value += 'k'
                    elif event.key == K_l and 'l' in self.restricted: self.value += 'l'
                    elif event.key == K_m and 'm' in self.restricted: self.value += 'm'
                    elif event.key == K_n and 'n' in self.restricted: self.value += 'n'
                    elif event.key == K_o and 'o' in self.restricted: self.value += 'o'
                    elif event.key == K_p and 'p' in self.restricted: self.value += 'p'
                    elif event.key == K_q and 'q' in self.restricted: self.value += 'q'
                    elif event.key == K_r and 'r' in self.restricted: self.value += 'r'
                    elif event.key == K_s and 's' in self.restricted: self.value += 's'
                    elif event.key == K_t and 't' in self.restricted: self.value += 't'
                    elif event.key == K_u and 'u' in self.restricted: self.value += 'u'
                    elif event.key == K_v and 'v' in self.restricted: self.value += 'v'
                    elif event.key == K_w and 'w' in self.restricted: self.value += 'w'
                    elif event.key == K_x and 'x' in self.restricted: self.value += 'x'
                    elif event.key == K_y and 'y' in self.restricted: self.value += 'y'
                    elif event.key == K_z and 'z' in self.restricted: self.value += 'z'
                    elif event.key == K_0 and '0' in self.restricted: self.value += '0'
                    elif event.key == K_1 and '1' in self.restricted: self.value += '1'
                    elif event.key == K_2 and '2' in self.restricted: self.value += '2'
                    elif event.key == K_3 and '3' in self.restricted: self.value += '3'
                    elif event.key == K_4 and '4' in self.restricted: self.value += '4'
                    elif event.key == K_5 and '5' in self.restricted: self.value += '5'
                    elif event.key == K_6 and '6' in self.restricted: self.value += '6'
                    elif event.key == K_7 and '7' in self.restricted: self.value += '7'
                    elif event.key == K_8 and '8' in self.restricted: self.value += '8'
                    elif event.key == K_9 and '9' in self.restricted: self.value += '9'
                    elif event.key == K_BACKQUOTE and '`' in self.restricted: self.value += '`'
                    elif event.key == K_MINUS and '-' in self.restricted: self.value += '-'
                    elif event.key == K_EQUALS and '=' in self.restricted: self.value += '='
                    elif event.key == K_LEFTBRACKET and '[' in self.restricted: self.value += '['
                    elif event.key == K_RIGHTBRACKET and ']' in self.restricted: self.value += ']'
                    elif event.key == K_BACKSLASH and '\\' in self.restricted: self.value += '\\'
                    elif event.key == K_SEMICOLON and ';' in self.restricted: self.value += ';'
                    elif event.key == K_QUOTE and '\'' in self.restricted: self.value += '\''
                    elif event.key == K_COMMA and ',' in self.restricted: self.value += ','
                    elif event.key == K_PERIOD and '.' in self.restricted: self.value += '.'
                    elif event.key == K_SLASH and '/' in self.restricted: self.value += '/'
                elif self.shifted:
                    if event.key == K_a and 'A' in self.restricted: self.value += 'A'
                    elif event.key == K_b and 'B' in self.restricted: self.value += 'B'
                    elif event.key == K_c and 'C' in self.restricted: self.value += 'C'
                    elif event.key == K_d and 'D' in self.restricted: self.value += 'D'
                    elif event.key == K_e and 'E' in self.restricted: self.value += 'E'
                    elif event.key == K_f and 'F' in self.restricted: self.value += 'F'
                    elif event.key == K_g and 'G' in self.restricted: self.value += 'G'
                    elif event.key == K_h and 'H' in self.restricted: self.value += 'H'
                    elif event.key == K_i and 'I' in self.restricted: self.value += 'I'
                    elif event.key == K_j and 'J' in self.restricted: self.value += 'J'
                    elif event.key == K_k and 'K' in self.restricted: self.value += 'K'
                    elif event.key == K_l and 'L' in self.restricted: self.value += 'L'
                    elif event.key == K_m and 'M' in self.restricted: self.value += 'M'
                    elif event.key == K_n and 'N' in self.restricted: self.value += 'N'
                    elif event.key == K_o and 'O' in self.restricted: self.value += 'O'
                    elif event.key == K_p and 'P' in self.restricted: self.value += 'P'
                    elif event.key == K_q and 'Q' in self.restricted: self.value += 'Q'
                    elif event.key == K_r and 'R' in self.restricted: self.value += 'R'
                    elif event.key == K_s and 'S' in self.restricted: self.value += 'S'
                    elif event.key == K_t and 'T' in self.restricted: self.value += 'T'
                    elif event.key == K_u and 'U' in self.restricted: self.value += 'U'
                    elif event.key == K_v and 'V' in self.restricted: self.value += 'V'
                    elif event.key == K_w and 'W' in self.restricted: self.value += 'W'
                    elif event.key == K_x and 'X' in self.restricted: self.value += 'X'
                    elif event.key == K_y and 'Y' in self.restricted: self.value += 'Y'
                    elif event.key == K_z and 'Z' in self.restricted: self.value += 'Z'
                    elif event.key == K_0 and ')' in self.restricted: self.value += ')'
                    elif event.key == K_1 and '!' in self.restricted: self.value += '!'
                    elif event.key == K_2 and '@' in self.restricted: self.value += '@'
                    elif event.key == K_3 and '#' in self.restricted: self.value += '#'
                    elif event.key == K_4 and '$' in self.restricted: self.value += '$'
                    elif event.key == K_5 and '%' in self.restricted: self.value += '%'
                    elif event.key == K_6 and '^' in self.restricted: self.value += '^'
                    elif event.key == K_7 and '&' in self.restricted: self.value += '&'
                    elif event.key == K_8 and '*' in self.restricted: self.value += '*'
                    elif event.key == K_9 and '(' in self.restricted: self.value += '('
                    elif event.key == K_BACKQUOTE and '~' in self.restricted: self.value += '~'
                    elif event.key == K_MINUS and '_' in self.restricted: self.value += '_'
                    elif event.key == K_EQUALS and '+' in self.restricted: self.value += '+'
                    elif event.key == K_LEFTBRACKET and '{' in self.restricted: self.value += '{'
                    elif event.key == K_RIGHTBRACKET and '}' in self.restricted: self.value += '}'
                    elif event.key == K_BACKSLASH and '|' in self.restricted: self.value += '|'
                    elif event.key == K_SEMICOLON and ':' in self.restricted: self.value += ':'
                    elif event.key == K_QUOTE and '"' in self.restricted: self.value += '"'
                    elif event.key == K_COMMA and '<' in self.restricted: self.value += '<'
                    elif event.key == K_PERIOD and '>' in self.restricted: self.value += '>'
                    elif event.key == K_SLASH and '?' in self.restricted: self.value += '?'

        if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]


# EzText example
from pygame.locals import *
import pygame, sys
import EzText
'''
def main():
    # initialize pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((640,240))
    # fill the screen w/ white
    screen.fill((255,255,255))
    # here is the magic: making the text input
    # create an input with a max length of 45,
    # and a red color and a prompt saying 'type here: '
    txtbx = EzText.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
    # create the pygame clock
    clock = pygame.time.Clock()
    # main loop!

    while 1:
        # make sure the program is running at 30 fps
        clock.tick(30)

        # events for txtbx
        events = pygame.event.get()
        # process other events
        for event in events:
            # close it x button si pressed
            if event.type == QUIT: return

        # clear the screen
        screen.fill((255,255,255))
        # update txtbx
        txtbx.update(events)
        # blit txtbx on the sceen
        txtbx.draw(screen)
        # refresh the display
        pygame.display.flip()

if __name__ == '__main__': main()
'''

def ChoosePlayerScreen():               #ChoosePlayerScreen door Joost en Eljakim
    pygame.init() 
    global AmountPlayersDefault

    display_width = 800
    display_height = 600
    #Colours, same as Carlo's code
    black = (0,0,0)
    white = (255,255,255)
    bright_blue = (0, 0, 255)
    red = (175,0,0)
    green = (0,175,0)
    blue = (30,144,255)         #Get Colors from kulur.adobe.com
    bright_red = (255,0,0)
    bright_green = (0,255,0)
    block_color = (53,115,255)
    intro = True

    #Name Caption, set up display, set up time
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Frequency')
    clock = pygame.time.Clock()
    #properties of the objects

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    #EzText, for typing in pygame GUI
    txtbx = EzText.Input(maxlength=45, color=(255,0,0), prompt='type here: ')
    event = pygame.event.get()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        
        bg = pygame.image.load("content/background_chooseplayers.jpg")
        bg= pygame.transform.scale(bg, (display_width, display_height))
        gameDisplay.blit(bg, (0, 0))  
        txtbx.update(event)
        txtbx.draw(gameDisplay)


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 150+100 > mouse[0] > 150 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_green, (150,500,100,50))
            if click[0] == 1:
                AmountPlayersDefault = 2
                #game_loop()               
        else:
            pygame.draw.rect(gameDisplay, green, (150,500,100,50))
        # Properties of buttons
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('2 Players', smallText)
        textRect.center = ( (150+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        
        if 350+100 > mouse[0] > 350 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(gameDisplay, bright_blue, (350,500,100,50))
            if click[0] == 1:
                AmountPlayersDefault = 3
                #game_loop()
        else: 
            pygame.draw.rect(gameDisplay, blue, (350,500,100,50))
        
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('3 Players', smallText)
        textRect.center = ( (350+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        txtbx.draw(800)    
        pygame.display.flip()
        if 550+100 > mouse[0] > 550 and 500+50 > mouse[1] > 500:    
            pygame.draw.rect(gameDisplay, bright_red, (550,500,100,50))
            if click[0] == 1:
                AmountPlayersDefault = 4
                #game_loop()
        else:
            pygame.draw.rect(gameDisplay, red, (550,500,100,50))

        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = text_objects('4 Players', smallText)
        textRect.center = ( (550+(100/2)), (500+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

if __name__ == '__main__': ChoosePlayerScreen()