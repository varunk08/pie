import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class that manages bullets fired from the ship """

    def __init__(self, aiSettings, screen, ship):
        """ Create a bullet object at the ship's current position """
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, aiSettings.bulletWidth,
            aiSettings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = aiSettings.bulletColor
        self.speedFactor = aiSettings.bulletSpeedFactor

    def update(self):
        self.y -= self.speedFactor
        self.rect.y = self.y

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)