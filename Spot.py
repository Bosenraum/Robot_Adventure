# Create map spots
from enum import Enum
from Characters import EnemyType, Player

# Enumerate directions for later
class Directions(Enum):
	NORTH = 1
	EAST  = 2
	SOUTH = 3
	WEST  = 4

class SpotType(Enum):
	CHARGE = 1
	COFFEE = 2
	FIGHT  = 3
	FUN	= 4
	EMPTY  = 5
	START  = 6
	END	= 7

class Spot:
	player = None

	def __init__(self, val):
		self.marked  = False
		self.entered = False
		self.visited = False
		self.val = val + 1
		self.type = SpotType.EMPTY
		self.enemy	 = None
		self.northSpot = None
		self.eastSpot  = None
		self.southSpot = None
		self.westSpot  = None

	def __str__(self):
		return str(self.val)

	@staticmethod
	def setPlayer(player):
		Spot.player = player

	# What to do when the player enters this spot
	def enter(self):
		self.entered = True
		# Perform type specific action
		# Give description of spot
		if(self.type == SpotType.END):
			print("YOU WIN!!")
			exit()
		elif(self.type == SpotType.CHARGE):
			# Refill hp
			Spot.player.heal()
			print("HP REFILLED")
			print(str(Spot.player.getHealth()))

		elif(self.type == SpotType.COFFEE):
			print("THE BITTER TASTE OF COFFEE FILLS YOU WITH DETERMINATION")
		elif(self.type == SpotType.FIGHT):
			print("FIGHT!")
			if(self.enemy.getType() == EnemyType.EASY):
				print("EASY PEASY")
			elif(self.enemy.getType() == EnemyType.MEDIUM):
				print("MEDIUM SQUEEZY")
			else:
				print("DIFFICULT DIFFICULT LEMON DIFFICULT")
				
			while(self.enemy.getHealth() > 0 and Spot.player.getHealth() > 0):
				Spot.player.attack(self.enemy)
				if(self.enemy.getHealth() <= 0):
					print("ENEMY DEFEATED")
					print(str(Spot.player.getHealth()))
					break
				self.enemy.attack(Spot.player)
				if(Spot.player.getHealth() <= 0):
					print("YOU LOSE")
					exit()
			self.enemy = None
			self.setType(SpotType.EMPTY)
		elif(self.type == SpotType.FUN):
			print("GLHF")
		else:
			print("NOTHING TO SEE HERE")

	def leave(self):
		self.entered = False

	def move(self, dir):
		if(self.isValidDir(dir)):
			self.leave()
			if(dir == Directions.NORTH):
				self.northSpot.enter()
				return self.northSpot
			if(dir == Directions.EAST):
				self.eastSpot.enter()
				return self.eastSpot
			if(dir == Directions.SOUTH):
				self.southSpot.enter()
				return self.southSpot
			if(dir == Directions.WEST):
				self.westSpot.enter()
				return self.westSpot
		else:
			print("INVALID MOVE")
			return self

	def getMarked(self):
		return self.marked

	def getVisited(self):
		return self.visited

	def setVisited(self, status):
		self.visited = status

	def getType(self):
		return self.type

	def setType(self, type):
		self.type = type
		self.marked = True

	def getEnemy(self):
		return self.enemy

	def setEnemy(self, enemy):
		self.enemy = enemy

	def setConnections(self, north=False, east=False, south=False, west=False):
		self.north = north
		self.east  = east
		self.south = south
		self.west  = west

	def getNorth(self):
		return self.north

	def setNorthSpot(self, spot):
		self.northSpot = spot

	def getEast(self):
		return self.east

	def setEastSpot(self, spot):
		self.eastSpot = spot

	def getSouth(self):
		return self.south

	def setSouthSpot(self, spot):
		self.southSpot = spot

	def getWest(self):
		return self.west

	def setWestSpot(self, spot):
		self.westSpot = spot

	# Return true if any neighboring spots are of the input type
	# Used to disallow the same spotType's being adjacent
	def checkNeighbors(self, type):
		match = False
		if(self.northSpot != None and self.northSpot.getType() == type):
			match = True
		elif(self.eastSpot != None and self.eastSpot.getType() == type):
			match = True
		elif(self.southSpot != None and self.southSpot.getType() == type):
			match = True
		elif(self.westSpot != None and self.westSpot.getType() == type):
			match = True

		return match

	def checkNeighborEnemies(self, enemyType):
		match = False
		if(self.northSpot != None and self.northSpot.getEnemy() != None and self.northSpot.getEnemy().getType() == enemyType):
			match = True
		elif(self.eastSpot != None and self.eastSpot.getEnemy() != None and self.eastSpot.getEnemy().getType() == enemyType):
			match = True
		elif(self.southSpot != None and self.southSpot.getEnemy() != None and self.southSpot.getEnemy().getType() == enemyType):
			match = True
		elif(self.westSpot != None and self.westSpot.getEnemy() != None and self.westSpot.getEnemy().getType() == enemyType):
			match = True

		return match

	def isValidDir(self, dir):
		if(dir == Directions.NORTH and self.north):
			return True
		elif(dir == Directions.EAST and self.east):
			return True
		elif(dir == Directions.SOUTH and self.south):
			return True
		elif(dir == Directions.WEST and self.west):
			return True
		else:
			return False

	# # DFS function to find next direction from coffee shop?
	# def DFS(self):
	# 	self.setVisited(True)
	#
	#
	# 	# if(self.type = SpotType.END):
	# 	# 	return numHops
	#
	# 	if(self.northSpot != None and not self.northSpot.getVisited()):
	# 		northHops = self.northSpot.DFS() + 1
	# 	if(self.eastSpot != None and not self.eastSpot.getVisited()):
	# 		eastHops = self.eastSpot.DFS() + 1
	# 	if(self.southSpot != None and not self.southSpot.getVisited()):
	# 		southHops = self.southSpot.DFS() + 1
	# 	if(self.westSpot != None and not self.westSpot.getVisited()):
	# 		westHops = self.westSpot.DFS() + 1
	#
	# 	return min(northHops, eastHops, southHops, westHops)

	def printRow(self):
		if(self.entered):
			print("XX", end="")
		elif(self.type == SpotType.START):
			print("SS", end="")
		elif(self.type == SpotType.END):
			print("@@", end="")
		elif(self.type == SpotType.CHARGE):
			print("CH", end="")
		elif(self.type == SpotType.COFFEE):
			print("CO", end="")
		elif(self.type == SpotType.FIGHT):
			if(self.enemy.getType() == EnemyType.EASY):
				print("EE", end="")
			elif(self.enemy.getType() == EnemyType.MEDIUM):
				print("MM", end="")
			else:
				print("HH", end="")
		elif(self.type == SpotType.FUN):
			print("FU", end="")
		else:
			if(self.val <= 10):
				print(" " + str(self.val), end="")
			else:
				print(self.val, end="")

		if(self.east):
			print("---", end="")
		else:
			print("   ", end="")

	def printColumn(self):
		if(self.south):
			print(" |   ", end="")
		else:
			print("     ", end="")
