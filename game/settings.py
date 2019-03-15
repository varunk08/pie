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
        self.bulletSpeedFactor = 1
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = (60, 60, 60)
        self.bulletsAllowed = 3

        self.alienSpeedFactor = 1
        self.fleetDropSpeed = 10
        self.fleetDirection = 1