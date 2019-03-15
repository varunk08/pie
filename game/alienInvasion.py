import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import gameFunctions as gf
from alien import Alien

def runGame():
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(aiSettings, screen)
    bullets = Group()
    aliens = Group()
    gf.createFleet(aiSettings, screen, aliens, ship)
    
    while True:
        gf.checkEvents(aiSettings, screen, ship, bullets)
        ship.update()
        gf.updateBullets(aiSettings, bullets, aliens, screen, ship)
        gf.updateAliens(aiSettings, aliens)
        gf.updateScreen(aiSettings, screen, ship, bullets, aliens)

runGame()