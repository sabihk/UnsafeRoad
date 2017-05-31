import pygame, sys, os
from pygame.locals import *

# To make pygame function works
pygame.init()

# Surface object
displaySurface = pygame.display.set_mode((800, 419))

# Title bar of window
pygame.display.set_caption('Unsafe Road')

roadImgPath = os.path.join('Images', 'road.png')
playerImgPath = os.path.join('Images', 'player.png')
carImgPath = os.path.join('Images', 'car.png')

roadImg = pygame.image.load(roadImgPath)
playerImg = pygame.image.load(playerImgPath)
carImg = pygame.image.load(carImgPath)

# X and Y coordinates or starting coordinates for background image
roadPositionX = 0
roadPositionY = 0

# X and Y coordinates or starting coordinates for player
playerPositionX = 200
playerPositionY = 260

# X and Y coordinates or starting coordinates for car
carPositionX = 500
carPositionY = 280

while True:  # main game loop

    # Copy road image on displaySurface
    displaySurface.blit(roadImg, (roadPositionX, roadPositionY))

    # Copy road image on displaySurface
    displaySurface.blit(playerImg, (playerPositionX, playerPositionY))

    # Copy road image on displaySurface
    displaySurface.blit(carImg, (carPositionX, carPositionY))

    # Loop for each event that occurred e.g., keypress or mouse movement
    for event in pygame.event.get():
        if event.type == QUIT:
            # Deactivate pygame library
            pygame.quit()
            # Terminates program
            sys.exit()
    pygame.display.update()