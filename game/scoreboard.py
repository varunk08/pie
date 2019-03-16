import pygame.font

class Scoreboard():
	def __init__(self, aiSettings, screen, stats):
		self.screen = screen
		self.screenRect = screen.get_rect()
		self.aiSettings = aiSettings
		self.stats = stats
	
		self.textColor = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 45)
	
		self.prepScore()


	def prepScore(self):
		scoreStr = str(self.stats.score)
		self.scoreImage = self.font.render(scoreStr, True, self.textColor, self.aiSettings.screenBgColor)
		self.scoreRect = self.scoreImage.get_rect()
		self.scoreRect.right = self.screenRect.right - 20
		self.scoreRect.top = 20


	def showScore(self):
		self.screen.blit(self.scoreImage, self.scoreRect)