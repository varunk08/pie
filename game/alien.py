import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, aiSettings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.aiSettings = aiSettings

        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)