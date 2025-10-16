from Error import Error

class Game:
	def __init__(self, players, worldMap):
		if len(players) < 3:
			raise ValueError(Error.NOT_ENOUGH_PLAYERS)
		self.players = players
		self.worldMap = worldMap
		self.currentPlayerID = 0
	
	def checkCurrentPlayerID(self, playerID):
		if playerID != self.currentPlayerID:
			raise ValueError(Error.NOT_YOUR_TURN)
	
	def nextPlayer(self):
		candidate = self.currentPlayerID
		for i in range(1, len(self.players)):
			candidate = self.players[(self.currentPlayerID + i) % len(self.players)]
			if candidate.isDead() == False:
				break
		self.currentPlayerID = candidate
	
	def move(self, playerID, direction):
		self.checkCurrentPlayerID(playerID)
		self.worldMap.move(playerID, direction)
		self.players[playerID].looseHP()
	
	def getCurrentInventory(self, playerID):
		self.checkCurrentPlayer(player)
		return self.players[playerID].getInventory()

	def skip(self):
		self.nextPlayer()
	
	def shoot(self):
		pass

