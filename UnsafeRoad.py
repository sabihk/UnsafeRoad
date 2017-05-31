import pygame, sys, os
from pygame.locals import *

# To make pygame function works
pygame.init()

''' 1. SCREEN '''
# As per road image dimension
screenSizeX = 800
screenSizeY = 419

''' 2. ROAD / BACKGROUND '''
# X and Y coordinates or starting coordinates for background image
roadPositionX = 0
roadPositionY = 0

''' 3. PLAYER '''
# X and Y coordinates or starting coordinates for player
playerPositionX = 200
playerPositionY = 260

# Initial value for player movement in X and Y direction is set to 0
movePlayerX = 0
movePlayerY = 0

# Speed of player in X and Y direction is 1 i.e., 10px
playerSpeedX = 1
playerSpeedY = 1

# Player can jump upto this height from top of screen
playerJump = 80

''' 4. CAR '''
# X and Y coordinates or starting coordinates for car
carPositionX = 800
carPositionY = 280

# setInitialCarPositionX is set to 800
setInitialCarPositionX = carPositionX

# carPositionMinX is set to -ve of car width
carPositionMinX = -260

# Car speed is set to 0.5 i.e., 5px
carSpeedX = 0.5

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
            if K_UP == event.key:
                # On keydown event of up key, movePlayerY value is changed to 1
                movePlayerY = playerSpeedY
            if K_LEFT == event.key:
                # On keydown event of left key, movePlayerX value is changed to -1
                movePlayerX = -playerSpeedX
            elif K_RIGHT == event.key:
                # On keydown event of right key, movePlayerX value is changed to +1
                movePlayerX = playerSpeedX

        elif KEYUP == event.type:
            if K_LEFT == event.key:
                # On keyup event of left key, movePlayer value is changed to 0
                movePlayerX = 0
            elif K_RIGHT == event.key:
                # On keyup event of right key, movePlayer value is changed to 0
                movePlayerX = 0

    # For each of the changed value of movePlayerX, playerPositionX is updated
    playerPositionX += movePlayerX

    # For each of the changed value of movePlayerY, playerPositionY is updated
    # i.e., player Y coordinate started decreasing by 1 in each iteration [i.e., Jump]
    playerPositionY -= movePlayerY

    # As the player Y coordinate reached 'playerJump(79)' player Y coordinate started increasing by 1 [i.e., Drop]
    if playerPositionY < playerJump:
        movePlayerY = -playerSpeedY

    # As the player Y coordinate reached its initial position
    # i.e., 'playerPositionY(260)' increment of playerPositionY is stopped
    elif playerPositionY >= 260:
        movePlayerY = 0

    # carPositionX is updated with value -1 i.e., -10px in each iteration
    carPositionX -= carSpeedX

    # If carPositionX is decreased to less than carPositionMinX i.e., width of car
    if carPositionX < carPositionMinX:
        # Update carPositionX back to initial position
        carPositionX = setInitialCarPositionX

    # Update the Surface object or [screen]
    pygame.display.update()
