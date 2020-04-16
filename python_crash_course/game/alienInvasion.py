import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
import gameFunctions as gf
from alien import Alien
from gameStats import GameStats
from button import Button
from scoreboard import Scoreboard

def runGame():
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screenWidth, aiSettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(aiSettings)
    ship = Ship(aiSettings, screen)
    bullets = Group()
    aliens = Group()
    gf.createFleet(aiSettings, screen, aliens, ship)
    playButton = Button(aiSettings, screen, "Play")
    sb = Scoreboard(aiSettings, screen, stats)

    while True:
        gf.checkEvents(aiSettings, screen, ship, bullets, aliens, stats, playButton, sb)
        if stats.gameActive:
            ship.update()
            gf.updateBullets(aiSettings, bullets, aliens, screen, ship, stats, sb)
            gf.updateAliens(aiSettings, stats, screen, aliens, bullets, ship, sb)
        gf.updateScreen(aiSettings, screen, ship, bullets, aliens, stats, playButton, sb)


runGame()