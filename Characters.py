# Create different enemies
# Create player character'

from Music import *
from Enumerations import *
# from numpy import roll
import random, time
from Network import *
#from pygame import mixer

Sounds.init()

class Player:
	maxHP = 200
	maxMoves = 30

	def __init__(self, name):
		if(name.lower() != "suw"):
			self.name = name
			self.hp = Player.maxHP
			self.damageMin = 20
			self.damageMax = 40
			self.cheated = False
		else:
			self.name = "CHEATER"
			self.hp = 1000
			self.damageMin = 1000
			self.damageMax = 2000
			self.cheated = True

		self.movesTaken = 0
		self.orientation = [Directions.NORTH, Directions.EAST, Directions.SOUTH, Directions.WEST]

	def getName(self):
		return self.name

	def getHealth(self):
		return self.hp

	def getMovesTaken(self):
		return self.movesTaken

	def getOrientation(self):
		return self.orientation

	# update directions based on current robot orientation
	def turnRight(self):
		self.orientation.append(self.orientation.pop(0))

	def turnLeft(self):
		for i in range(3):
			self.turnRight()

	def getRelativeDir(self, cardinalDir):
		i = -1

		# Reverse map cardinal directions to orientation
		if(cardinalDir == "north"):
			i = self.orientation.index(Directions.NORTH)
		elif(cardinalDir == "east"):
			i = self.orientation.index(Directions.EAST)
		elif(cardinalDir == "south"):
			i = self.orientation.index(Directions.SOUTH)
		elif(cardinalDir == "west"):
			i = self.orientation.index(Directions.WEST)

		if(i == 0):
			relativeDir = "forward"
		elif(i == 1):
			relativeDir = "right"
		elif(i == 2):
			relativeDir = "backward"
		elif(i == 3):
			relativeDir = "left"
		else:
			relatvieDir = "error"

		return relativeDir


	def loseHealth(self, val):
		self.hp -= val

	def attack(self, enemy):
		damage = random.choice(range(self.damageMin, self.damageMax+1))
		enemy.loseHealth(damage)

		Sounds.playSound(SoundEffect.MEDIUM)

		#print(f"YOU ATTACKED FOR {damage} damage -- ", end="")
		print("YOU ATTACKED FOR %d damage -- " % damage, end="")
		#print(f"ENEMY HAS {enemy.getHealth()} HP REMAINING")
		print("ENEMY HAS %d HP REMAINING" % enemy.getHealth())

	def strongAttack(self, enemy):
		damage = 2*random.choice(range(self.damageMin, self.damageMax+1))
		enemy.loseHealth(damage)
		Sounds.playSound(SoundEffect.HARD)

		#print(f"YOU ATTACKED FOR {damage} damage -- ", end="")
		print("YOU ATTACKED FOR %d damage -- " % damage, end="")
		#print(f"ENEMY HAS {enemy.getHealth()} HP REMAINING")
		print("ENEMY HAS %d HP REMAINING" % enemy.getHealth())

	def heal(self):
		self.hp = Player.maxHP
		print("HP REFILLED")
		#print(f"{self.name.upper()}'s HP: {self.hp}")
		print("%s's HP: %d" % (self.name.upper(), self.hp))

	def getStatus(self):
		#print(f"{self.getRemaining()} MOVES REMAINING")
		print("%d MOVES REMAINING" % self.getRemaining())
		#print(f"{self.name.upper()}'s HP: {self.hp}")
		print("%s's HP: %d" % (self.name.upper(), self.hp))

	def getRemaining(self):
		return Player.maxMoves - self.movesTaken

	def move(self):
		self.movesTaken += 1

	def isCheater(self):
		return self.cheated

	def win(self):
		# fade main theme
		# Play the win music
		if(not self.cheated):
			print("YOU WIN!!")
			createSendThread("YOU WIN", 20, 10, "f")
		else:
			print("CHEATERS NEVER WIN!")
			createSendThread("CHEATERS NEVER WIN!", 5, 10, "f")
		Sounds.fadeSound(Sounds.getPlaying())
		time.sleep(1)
		Sounds.playSound(SoundEffect.WIN)
		time.sleep(2)
		exit()

	def lose(self):
		if(self.cheated):
			print("HOW COULD YOU CHEAT AND STILL LOSE?!")
		else:
			print("GAME OVER")
			createSendThread("GAME OVER", 1, 5, "f")
		Sounds.fadeSound(Sounds.getPlaying())
		time.sleep(1)
		Sounds.playSound(SoundEffect.LOSE)
		time.sleep(2)
		exit()

class Enemy:

	def __init__(self, type):
		self.type = type
		self.hp = 0
		self.strength = 0
		self.damageMin = 10
		self.damageMax = 15

		if(type == EnemyType.EASY):
			self.hp = 50
			self.strength = 1
		elif(type == EnemyType.MEDIUM):
			self.hp = 75
			self.strength = 2
		elif(type == EnemyType.HARD):
			self.hp = 100
			self.strength = 3
		else:
			self.hp = 200
			self.strength = 2

	def getType(self):
		return self.type

	def loseHealth(self, val):
		self.hp -= val

	def getHealth(self):
		return self.hp

	# return a random value based on the strength of the enemy
	def attack(self, player):
		if(self.type == EnemyType.HARD or self.type == EnemyType.BOSS):
			soundType = SoundEffect.HARD
		elif(self.type == EnemyType.MEDIUM):
			soundType = SoundEffect.MEDIUM
		else:
			soundType = SoundEffect.WEAK

		damage = self.strength * (random.choice(range(self.damageMin, self.damageMax)))
		player.loseHealth(damage)

		#print(f"Enemy attacked for {damage} damage -- ", end="")
		print("Enemy attacked for %d damage -- " % damage, end="")
		#print(f"You have {player.getHealth()} HP remaining")
		print("You have %d HP remaining" % player.getHealth())

		Sounds.playSound(soundType)

	def getStatus(self):
		#print(f"ENEMY HP: {self.hp}")
		print("ENEMY HP: %d" % self.hp)
