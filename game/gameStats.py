class GameStats():

	def __init__(self, aiSettings):
		self.aiSettings = aiSettings
		self.resetStats()
		self.gameActive = False

	def resetStats(self):
		self.shipsLeft = self.aiSettings.shipLimit