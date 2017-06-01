import pygame, sys, os
from pygame.locals import *

# To make pygame function works
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 128, 0)

smallfont = pygame.font.SysFont('comicsansms', 30)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)

""" SCREEN """
# As per road image dimension
screenSizeX = 800
screenSizeY = 419

# Surface object
displaySurface = pygame.display.set_mode((screenSizeX, screenSizeY))

# Title bar of window
pygame.display.set_caption('Unsafe Road')

roadImgPath = os.path.join('Images', 'road.png')
playerImgPath = os.path.join('Images', 'player.png')
carImgPath = os.path.join('Images', 'car.png')
crashImgPath = os.path.join('Images', 'crash.png')

roadImg = pygame.image.load(roadImgPath)
playerImg = pygame.image.load(playerImgPath)
carImg = pygame.image.load(carImgPath)
crashImg = pygame.image.load(crashImgPath)


def pause():
    """ Pause the game """
    # Pause functionality: 'https://youtu.be/sDL7P2Jhlh8'
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    # Continue
                    paused = False

                elif event.key == K_q:
                    # Quit
                    # Deactivate pygame library
                    pygame.quit()
                    # Terminates program
                    sys.exit()

        # Fill screen with white background
        displaySurface.fill(white)

        # Display Paused in green color
        message_to_screen("Paused", green, -50, size="large")
        # Display how to continue or quit the game
        message_to_screen("Press C to continue or Q to quit", black, 25)

        # Update the screen
        pygame.display.update()


def message_to_screen(msg, color, y_displace=0, size="small"):
    """ Displays the message on screen """
    textSurfaceObj, textRectObj = text_objects(msg, color, size)
    textRectObj.center = (screenSizeX / 2), (screenSizeY / 2) + y_displace

    # textSurface is the object to be copied on displaySurface
    # textRectObj is the tuple of X and Y coordinate from topleft corner
    displaySurface.blit(textSurfaceObj, textRectObj)


def text_objects(text, color, size):
    """ Returns a surface and rect object

    Font size and color of text
    """
    if size == "small":
        textSurfaceObj = smallfont.render(text, True, color)
    elif size == "medium":
        textSurfaceObj = medfont.render(text, True, color)
    elif size == "large":
        textSurfaceObj = largefont.render(text, True, color)

    # 2nd object returned is a Rect object created from surface object
    # which will have height and width correctly set for text that was rendered
    return textSurfaceObj, textSurfaceObj.get_rect()


def gameover(playerPositionX, playerPositionY):
    """ Displays Game Over message along with how to restart """
    gameover = True

    while gameover:
        # Show crash image when accident occurs
        displaySurface.blit(crashImg, (playerPositionX - 30, playerPositionY + 50))

        # Display Game Over and Restart message
        message_to_screen("Game Over", green, -25, size="medium")
        message_to_screen("Press R to restart the game", black, 25)

        # Update the screen
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    # Restart
                    start_game()


def start_game():
    """ Start the game """

    """ 1. ROAD / BACKGROUND """
    # X and Y coordinates or starting coordinates for background image
    roadPositionX = 0
    roadPositionY = 0

    """ 2. PLAYER """
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

    """ 3. CAR """
    # X and Y coordinates or starting coordinates for car
    carPositionX = 800
    carPositionY = 280

    # setInitialCarPositionX is set to 800
    setInitialCarPositionX = carPositionX

    # carPositionMinX is set to -ve of car width
    carPositionMinX = -260

    # Car speed is set to 0.5 i.e., 5px
    carSpeedX = 0.5

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
                elif K_p == event.key:
                    pause()

            elif KEYUP == event.type:
                if K_LEFT == event.key:
                    # On keyup event of left key, movePlayer value is changed to 0
                    movePlayerX = 0
                elif K_RIGHT == event.key:
                    # On keyup event of right key, movePlayer value is changed to 0
                    movePlayerX = 0

        """ Player X and Y coordinate update """
        # For each of the changed value of movePlayerX, playerPositionX is updated
        playerPositionX += movePlayerX

        # For each of the changed value of movePlayerY, playerPositionY is updated
        # i.e., player Y coordinate started decreasing by 1 in each iteration [i.e., Jump]
        playerPositionY -= movePlayerY

        """ Player Jump functionality """
        # As the player Y coordinate reached 'playerJump(79)' player Y coordinate started increasing by 1 [i.e., Drop]
        if playerPositionY < playerJump:
            movePlayerY = -playerSpeedY

        # As the player Y coordinate reached its initial position
        # i.e., 'playerPositionY(260)' increment of playerPositionY is stopped
        elif playerPositionY >= 260:
            movePlayerY = 0

        """ Car X coordinate update & set car position to initial state """
        # carPositionX is updated with value -1 i.e., -10px in each iteration
        carPositionX -= carSpeedX

        # If carPositionX is decreased to less than carPositionMinX i.e., width of car
        if carPositionX < carPositionMinX:
            # Update carPositionX back to initial position
            carPositionX = setInitialCarPositionX

        """ Car crash / gameover functionality """
        # Distance between player and car
        distance = playerPositionX - carPositionX

        # If horizontal distance between player and car is between 0 and 240 and
        # vertical height of player is greater than 180 i.e., below car height then crash / gameover
        if 0 < distance < 240 and playerPositionY > 180:

            gameover(playerPositionX, playerPositionY)

        # Update the Surface object or [screen]
        pygame.display.update()

start_game()
