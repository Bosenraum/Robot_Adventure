# Create different enemies
# Create player character'

from enum import Enum
import random, time
from pygame import mixer

mixer.init()

class EnemyType(Enum):
	EASY   = 1
	MEDIUM = 2
	HARD   = 3

class Player:
	maxHP = 200
	maxMoves = 30

	def __init__(self, name):
		if(name.lower() != "superultrawinning"):
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

	def getName(self):
		return self.name

	def getHealth(self):
		return self.hp

	def getMovesTaken(self):
		return self.movesTaken

	def loseHealth(self, val):
		self.hp -= val

	def attack(self, enemy):
		damage = random.choice(range(self.damageMin, self.damageMax+1))
		enemy.loseHealth(damage);
		print(f"You attacked for {damage} damage -- ", end="")
		print(f"Enemy has {enemy.getHealth()} HP remaining")

	def heal(self):
		self.hp = Player.maxHP
		print("HP REFILLED")
		print(f"{self.name.upper()}'s HP: {self.hp}")

	def getStatus(self):
		print(f"{self.getRemaining()} MOVES REMAINING")
		print(f"{self.name.upper()}'s HP: {self.hp}")

	def getRemaining(self):
		return Player.maxMoves - self.movesTaken

	def move(self):
		self.movesTaken += 1

	def isCheater(self):
		return self.cheated

	def win(self):
		if(not self.cheated):
			print("YOU WIN!!")
		else:
			print("CHEATERS NEVER WIN!")
		exit()

	def lose(self):
		if(self.cheated):
			print("HOW COULD YOU CHEAT AND STILL LOSE?!")
		else:
			print("YOU LOSE")
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
		else:
			self.hp = 100
			self.strength = 3

	def getType(self):
		return self.type

	def loseHealth(self, val):
		self.hp -= val

	def getHealth(self):
		return self.hp

	# return a random value based on the strength of the enemy
	def attack(self, player):
		if(self.type == EnemyType.HARD):
			mixer.music.load("audio/hard_hit.mp3")
		elif(self.type == EnemyType.MEDIUM):
			mixer.music.load("audio/medium_hit.mp3")
		else:
			mixer.music.load("audio/weak_hit.mp3")

		damage = self.strength * (random.choice(range(self.damageMin, self.damageMax)))
		player.loseHealth(damage)

		print(f"Enemy attacked for {damage} damage -- ", end="")
		print(f"You have {player.getHealth()} HP remaining")

		mixer.music.play()
		time.sleep(1)

	def getStatus(self):
		print(f"ENEMY HP: {self.hp}")
