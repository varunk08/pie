import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Class to manage behaviour of our ship."""

    def __init__(self, aiSettings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.aiSettings = aiSettings
        self.screen = screen

        # Load the ship image and get it's rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

        # Movement attributes
        self.movingRight = False
        self.movingLeft = False

        self.center = float(self.rect.centerx)

    def update(self):
        """ Update the ship's position based on the movement flags"""
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.center += self.aiSettings.shipSpeedFactor
        elif self.movingLeft and self.rect.left > self.screenRect.left:
            self.center -= self.aiSettings.shipSpeedFactor


        self.rect.centerx = self.center
    def blitme(self):
        """ Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


    def centerShip(self):
        self.center = self.screenRect.centerx