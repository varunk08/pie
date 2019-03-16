import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def shipHit(aiSettings, stats, screen, ship, aliens, bullets):
    if stats.shipsLeft > 0:
        stats.shipsLeft -= 1
        aliens.empty()
        bullets.empty()
        createFleet(aiSettings, screen, aliens, ship)
        ship.centerShip()
        sleep(0.5)
    else:
        stats.gameActive = False
        

def checkBulletAlienCollisions(aiSettings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        createFleet(aiSettings, screen, aliens, ship)


def updateBullets(aiSettings, bullets, aliens, screen, ship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    checkBulletAlienCollisions(aiSettings, screen, ship, aliens, bullets)


def fireBullet(aiSettings, bullets, screen, ship):
    if len(bullets) < aiSettings.bulletsAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)


def getNumRows(aiSettings, shipHeight, alienHeight):
    availableHeight = aiSettings.screenHeight - 3 * alienHeight - shipHeight
    return int(availableHeight / (2 * alienHeight))


def createAlien(aiSettings, screen, aliens,  alienNum, rowNum):
    alien = Alien(aiSettings, screen)
    alienWidth = alien.rect.width
    alien.x = alienWidth + 2 * alienWidth * alienNum
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNum
    aliens.add(alien)

 
def getNumAliens(aiSettings, alienWidth):
    availableSpace = aiSettings.screenWidth - (2 * alienWidth)
    numAliens = int(availableSpace / (2 * alienWidth))
    return numAliens


def createFleet(aiSettings, screen, aliens, ship):
    alien = Alien(aiSettings, screen)
    numRows = getNumRows(aiSettings, ship.rect.height, alien.rect.height)
    numAliensPerRow = getNumAliens(aiSettings, alien.rect.width)
    for rowNum in range(numRows):
        for alienNum in range(numAliensPerRow):
            createAlien(aiSettings, screen, aliens, alienNum, rowNum)


def checkKeyDownEvents(event, aiSettings, screen, ship, bullets):
    """ Responds to key presses """
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        fireBullet(aiSettings, bullets, screen, ship)    
    elif event.key == pygame.K_q:
        sys.exit()


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


def updateScreen(aiSettings, screen, ship, bullets, aliens):
    """ Update images on the screen and flip to the new screen. """
    screen.fill(aiSettings.screenBgColor)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def checkAliensBottom(aiSettings, stats, screen, ship, aliens, bullets):
    screenRect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenRect.bottom:
            shipHit(aiSettings, stats, screen, ship, aliens, bullets)
            break


def updateAliens(aiSettings, stats, screen, aliens, bullets, ship):
    checkFleetEdges(aiSettings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        shipHit(aiSettings, stats, screen, ship, aliens, bullets)
    checkAliensBottom(aiSettings, stats, screen, ship, aliens, bullets)


def changeFleetDirection(aiSettings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += aiSettings.fleetDropSpeed
    aiSettings.fleetDirection *= -1


def checkFleetEdges(aiSettings, aliens):
    for alien in aliens.sprites():
        if alien.checkEdges():
            changeFleetDirection(aiSettings, aliens)
            break