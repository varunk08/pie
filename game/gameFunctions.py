import sys
import pygame

def checkEvents(ship):
    """ Respond to key presses and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = True
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.movingRight = False
            elif event.key == pygame.K_LEFT:
                ship.movingLeft = False

def updateScreen(aiSettings, screen, ship):
    """ Update images on the screen and flip to the new screen. """

    screen.fill(aiSettings.screenBgColor)
    ship.blitme()

    pygame.display.flip()
