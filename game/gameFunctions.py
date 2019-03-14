import sys
import pygame
from bullet import Bullet

def updateBullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fireBullet(aiSettings, bullets, screen, ship):
    if len(bullets) < aiSettings.bulletsAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)

def checkKeyDownEvents(event, aiSettings, screen, ship, bullets):
    """ Responds to key presses """
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        fireBullet(aiSettings, bullets, screen, ship)    

def checkKeyUpEvents(event, ship):
    """ Responds to key releases """
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False

def checkEvents(aiSettings, screen, ship, bullets):
    """ Respond to key presses and mouse events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, aiSettings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, ship)

def updateScreen(aiSettings, screen, ship, bullets):
    """ Update images on the screen and flip to the new screen. """

    screen.fill(aiSettings.screenBgColor)
    
    for bullet in bullets.sprites():
        bullet.drawBullet()

    ship.blitme()

    pygame.display.flip()
