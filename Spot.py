# Create map spots
from enum import Enum
from Characters import EnemyType, Player
from Music import *
import random
import time
#from pygame import mixer

Sounds.init()

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

class FunType(Enum):
	RIDDLE = 1 # Sphinx riddle
	PUZZLE = 2 # A basic puzzle
	BOSS   = 3 # Fight a strong enemy that you can't flee from

class Spot:
	player = None
	cur = None

	def __init__(self, val):
		self.marked  = False
		self.entered = False
		self.visited = False
		self.val = val + 1
		self.type = SpotType.EMPTY
		self.enemy	   = None
		self.funType   = None
		self.northSpot = None
		self.eastSpot  = None
		self.southSpot = None
		self.westSpot  = None

	def __str__(self):
		return str(self.val)

	@staticmethod
	def setPlayer(player):
		Spot.player = player

	@staticmethod
	def setCur(spot):
		Spot.cur = spot

	@staticmethod
	def getCur():
		return Spot.cur

	@staticmethod
	def checkLose():
		if(Spot.player.getHealth() <= 0):
			Spot.player.lose()

	# What to do when the player enters this spot
	def enter(self):
		print()
		self.entered = True
		# Perform type specific action
		# Give description of spot
		if(self.type == SpotType.END):
			Spot.player.win()
		elif(self.type == SpotType.CHARGE):
			# Refill hp
			Spot.player.heal()

		elif(self.type == SpotType.COFFEE):
			print("THE BITTER TASTE OF COFFEE FILLS YOU WITH DETERMINATION")
			# Need to clear the visited label for all spots before searching
			nextDir = self.DFS()
			if(nextDir == None):
				print("ERROR: NO END FOUND")
			elif(nextDir == "error"):
				print("ERROR: ERROR WAS RETURNED")
			else:
				print(f"YOU MUST GO {nextDir.upper()} FROM HERE TO REACH THE END\n")
		elif(self.type == SpotType.FIGHT):
			self.fight()

		# Need multiple fun spots
		elif(self.type == SpotType.FUN):
			self.haveFun()
			self.type = SpotType.EMPTY

		else:
			print("NOTHING TO SEE HERE")
			print()

	def flee(self):
		#self.leave()
		# check for valid spots adjacent to current spot, pick one randomly and enter
		dirs = []
		if(self.northSpot != None):
			dirs.append(Directions.NORTH)
		if(self.eastSpot != None):
			dirs.append(Directions.EAST)
		if(self.southSpot != None):
			dirs.append(Directions.SOUTH)
		if(self.westSpot != None):
			dirs.append(Directions.WEST)

		Spot.cur.move(random.choice(dirs))


	def leave(self):
		self.entered = False

	def move(self, dir):
		if(self.isValidDir(dir)):
			self.leave()
			if(dir == Directions.NORTH):
				Spot.cur = self.northSpot
				self.northSpot.enter()
				Spot.player.move()
				return self.northSpot
			if(dir == Directions.EAST):
				Spot.cur = self.eastSpot
				self.eastSpot.enter()
				Spot.player.move()
				return self.eastSpot
			if(dir == Directions.SOUTH):
				Spot.cur = self.southSpot
				self.southSpot.enter()
				Spot.player.move()
				return self.southSpot
			if(dir == Directions.WEST):
				Spot.cur = self.westSpot
				self.westSpot.enter()
				Spot.player.move()
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

	def setFunType(self, type):
		self.funType = type

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

	def validMoves(self):
		dirs = []
		if(self.north):
			dirs.append("NORTH")
		if(self.east):
			dirs.append("EAST")
		if(self.south):
			dirs.append("SOUTH")
		if(self.west):
			dirs.append("WEST")

		if(len(dirs) == 1):
			output = "THERE IS A PATH LEADING " + dirs[0]
		elif(len(dirs) == 2):
			output = "THERE ARE PATHS LEADING " + dirs[0] + " AND " + dirs[1]
		else:
			output = "THERE ARE PATHS LEADING "
			for i in range(len(dirs) - 1):
				output += dirs[i] + ", "
			output += "AND " + dirs[-1]

		print(output)

	# # DFS function to find next direction from coffee shop?
	def DFS(self):
		self.setVisited(True)

		dir = None

		if(self.northSpot != None and not self.northSpot.getVisited()):
			if(self.northSpot.getType() == SpotType.END):
				return "north"
			else:
				dir = self.northSpot.DFS()
				if(dir != None and dir != "error"):
					return "north"
		if(self.eastSpot != None and not self.eastSpot.getVisited()):
			if(self.eastSpot.getType() == SpotType.END):
				return "east"
			else:
				dir = self.eastSpot.DFS()
				if(dir != None and dir != "error"):
					return "east"
		if(self.southSpot != None and not self.southSpot.getVisited()):
			if(self.southSpot.getType() == SpotType.END):
				return "south"
			else:
				dir = self.southSpot.DFS()
				if(dir != None and dir != "error"):
					return "south"
		if(self.westSpot != None and not self.westSpot.getVisited()):
			if(self.westSpot.getType() == SpotType.END):
				return "west"
			else:
				dir = self.westSpot.DFS()
				if(dir != None and dir != "error"):
					return "west"

		return "error"

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
			if(self.funType == FunType.RIDDLE):
				print("RI", end="")
			elif(self.funType == FunType.PUZZLE):
				print("ZZ", end="")
			else:
				print("BB", end="")
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

	def fight(self):
		print("FIGHT!")
		flee = False
		if(self.enemy.getType() == EnemyType.EASY):
			print("EASY PEASY")
		elif(self.enemy.getType() == EnemyType.MEDIUM):
			print("MEDIUM SQUEEZY")
		else:
			print("DIFFICULT DIFFICULT LEMON DIFFICULT")

		while(self.enemy.getHealth() > 0 and Spot.player.getHealth() > 0):
			time.sleep(0.5)
			choice = input("ATTACK OR FLEE? >> ")
			print()
			if(choice.lower() in ["attack", "a"]):

				Spot.player.attack(self.enemy)
				if(self.enemy.getHealth() <= 0):
					print("ENEMY DEFEATED\n")
					break

				time.sleep(0.5)
				self.enemy.attack(Spot.player)
				Spot.checkLose()

			elif(choice.lower() in ["flee", "f"]):
				flee = True
				break
			elif(choice.lower() in ["status", "s"]):
				Spot.player.getStatus()
				self.enemy.getStatus()
			else:
				print("INVALID MOVE")
				self.enemy.attack(Spot.player)
				Spot.checkLose()

		if(not flee):
			self.enemy = None
			self.type = SpotType.EMPTY
		else:
			self.flee()

	def haveFun(self):
		if(self.funType == FunType.RIDDLE):
			Sounds.fadeSound(SoundEffect.THEME)
			time.sleep(1)
			Sounds.playSound(SoundEffect.SPHINX)
			time.sleep(6.5)
			soundType = SoundEffect.WRONG
			print(f"HELLO {Spot.player.getName()}")
			print("ANSWER THIS RIDDLE IF YOU WISH TO LIVE")
			print("WHAT IS THE CREATURE THAT WALKS ON FOUR LEGS IN THE MORNING,\nTWO LEGS AT NOON,\nAND THREE LEGS IN THE EVENING?\n")
			answer = input(">> ")
			print()
			while(answer.lower() != "man"):
				Sounds.playSound(soundType)
				print("INCORRECT")
				Spot.player.loseHealth(50)
				if(Spot.player.getHealth() <= 0):
					Sounds.fadeSound(SoundEffect.SPHINX)
					print("YOU MUST DIE..")
					for i in range(3):
						print("."*(i+1))
						time.sleep(1)
					print("YOU HAVE DIED")
					Spot.player.lose()
				print(f"{Spot.player.getHealth()} HP remaining")
				answer = input(">> ")
				print()
			print("*SPHINX DIES*")
			Sounds.fadeSound(SoundEffect.SPHINX)
			time.sleep(3)
			Sounds.playSound(SoundEffect.THEME)

		elif(self.funType == FunType.PUZZLE):
			print("NAME THIS SONG TO CONTINUE")
			Sounds.fadeSound(SoundEffect.THEME)
			time.sleep(1)
			Sounds.playSound(SoundEffect.TWINKLE)
			time.sleep(5)
			Sounds.stopSound(SoundEffect.TWINKLE)
			while(input("NAME THAT SONG (PRESS R TO REPLAY) >> ").lower() != "twinkle"):
				print("WRONG ANSWER. TURN YOU EARS ON!")
				time.sleep(1)
				Sounds.playSound(SoundEffect.TWINKLE)
				time.sleep(5)
				Sounds.stopSound(SoundEffect.TWINKLE)
			print(f"{Spot.player.getName()} YOU'RE MUSICAL INTUITION IS UNMATCHED")
			Sounds.playSound(SoundEffect.THEME)
			time.sleep(1)

		else:
			print("IT'S THE WIZARD BABY!")
			Sounds.fadeSound(SoundEffect.THEME)
			time.sleep(1)
			Sounds.playSound(SoundEffect.BOSS)

			while(self.enemy.getHealth() > 0 and Spot.player.getHealth() > 0):
				time.sleep(0.5)
				choice = input("ATTACK (WEAK OR STRONG) >> ")
				print()
				if(choice.lower() in ["attack", "a", "weak", "w", "weak attack"]):

					Spot.player.attack(self.enemy)
					if(self.enemy.getHealth() <= 0):
						print("BOSS BABY VANQUISHED!\n")
						break

					time.sleep(0.5)
					self.enemy.attack(Spot.player)
					Spot.checkLose()

				elif(choice.lower() in ["strong", "strong attack"]):
					if(random.choice(range(0, 10)) <= 7):
						Spot.player.strongAttack(self.enemy)
					else:
						print("ATTACK MISSED!")
					if(self.enemy.getHealth() <= 0):
						print("BOSS BABY VANQUISHED!\n")
						break

					time.sleep(0.5)
					self.enemy.attack(Spot.player)
					Spot.checkLose()

				elif(choice.lower() in ["flee", "f"]):
					flee = True
					break
				elif(choice.lower() in ["status", "s"]):
					Spot.player.getStatus()
					self.enemy.getStatus()
				else:
					print("INVALID MOVE")
					self.enemy.attack(Spot.player)
					Spot.checkLose()

			Sounds.fadeSound(SoundEffect.BOSS)
			time.sleep(1)
			Sounds.playSound(SoundEffect.THEME)
