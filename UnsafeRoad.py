import pygame, sys, os
from pygame.locals import *

# To make pygame function works
pygame.init()

# As per road image dimension
screenSizeX = 800
screenSizeY = 419

# X and Y coordinates or starting coordinates for background image
roadPositionX = 0
roadPositionY = 0

# X and Y coordinates or starting coordinates for player
playerPositionX = 200
playerPositionY = 260

# X and Y coordinates or starting coordinates for car
carPositionX = 500
carPositionY = 280

# Initial value for player movement in X direction is set to 0
movePlayerX = 0

# Speed of player in X direction is 1 i.e., 10px
playerSpeedX = 1

# Surface object
displaySurface = pygame.display.set_mode((screenSizeX, screenSizeY))

# Title bar of window
pygame.display.set_caption('Unsafe Road')

roadImgPath = os.path.join('Images', 'road.png')
playerImgPath = os.path.join('Images', 'player.png')
carImgPath = os.path.join('Images', 'car.png')

roadImg = pygame.image.load(roadImgPath)
playerImg = pygame.image.load(playerImgPath)
carImg = pygame.image.load(carImgPath)

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

        if KEYDOWN == event.type:
            if K_LEFT == event.key:
                # On keydown event of left key, movePlayer value is changed to -1
                movePlayerX = -playerSpeedX
            elif K_RIGHT == event.key:
                # On keydown event of right key, movePlayer value is changed to +1
                movePlayerX = playerSpeedX

        if KEYUP == event.type:
            if K_LEFT == event.key:
                # On keyup event of left key, movePlayer value is changed to 0
                movePlayerX = 0
            elif K_RIGHT == event.key:
                # On keyup event of right key, movePlayer value is changed to 0
                movePlayerX = 0

    # For each of the changed value of movePlayer playerPositionX is updated
    playerPositionX += movePlayerX

    # Update the Surface object or [screen]
    pygame.display.update()