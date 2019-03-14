import pygame

from settings import Settings
from ship import Ship
import gameFunctions as gf

def runGame():
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    while True:
        gf.checkEvents(ship)
        ship.update()
        gf.updateScreen(aiSettings, screen, ship)

runGame()