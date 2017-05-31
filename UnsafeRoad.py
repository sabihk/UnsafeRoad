import pygame, sys
from pygame.locals import *

# To make pygame function works
pygame.init()

# Surface object
displaySurface = pygame.display.set_mode((800, 419))

# Title bar of window
pygame.display.set_caption('Unsafe Road')

while True: # main game loop
    # Loop for each event in that occurred e.g., keypress or mouse movement
    for event in pygame.event.get():
        if event.type == QUIT:
            # Deactivate pygame library
            pygame.quit()
            # Terminates program
            sys.exit()
    pygame.display.update()