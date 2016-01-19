import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()
_image_library = {}

def get_image(path):                                # 
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                #if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                #        x += 3
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        if is_blue: 
            color = (0, 128, 255)
        else: 
            color = (255, 100, 0)
        screen.fill((0, 128, 255))
        screen.blit(get_image('ball1.png'), (20, 20))
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 120, 60))
        
        pygame.display.flip()
        clock.tick(60)