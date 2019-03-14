import pygame

class Ship():
    """Class to manage behaviour of our ship."""

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""

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

    def update(self):
        """ Update the ship's position based on the movement flags"""
        if self.movingRight:
            self.rect.centerx += 1
        elif self.movingLeft:
            self.rect.centerx -= 1

    def blitme(self):
        """ Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)