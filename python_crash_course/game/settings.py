class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screenWidth = 800
        self.screenHeight = 600
        self.screenBgColor  = (230, 230, 230)
        self.shipSpeedFactor = 1.5

        # Bullet settings
        self.bulletSpeedFactor = 3
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60, 60, 60)
        self.bulletsAllowed = 3

        self.alienSpeedFactor = 0.5
        self.fleetDropSpeed = 5
        self.fleetDirection = 1
        self.speedupScale = 1.1
        self.shipLimit = 3

        self.scoreScale = 1.5
        self.initializeDynamicSettings()


    def initializeDynamicSettings(self):
        self.shipSpeedFactor = 1.5
        self.bulletSpeedFactor = 3
        self.alienSpeedFactor = 1
        self.alienPoints = 50


    def increaseSpeed(self):
        self.shipSpeedFactor *= self.speedupScale
        self.bulletSpeedFactor *= self.speedupScale
        self.alienSpeedFactor *= self.speedupScale
        self.alienPoints = int(self.alienPoints * self.scoreScale)