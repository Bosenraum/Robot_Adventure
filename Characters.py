# Create different enemies
# Create player character'

from enum import Enum
import random

class EnemyType(Enum):
	EASY   = 1
	MEDIUM = 2
	HARD   = 3

class Player:
	maxHP = 100

	def __init__(self, name):
		self.name = name
		self.hp = Player.maxHP
		self.damageMin = 10
		self.damageMax = 20

	def getName(self):
		return self.name

	def getHealth(self):
		return self.hp

	def loseHealth(self, val):
		self.hp -= val

	def attack(self, enemy):
		damage = random.choice(range(self.damageMin, self.damageMax+1))
		enemy.loseHealth(damage);

	def heal(self):
		self.hp = Player.maxHP

class Enemy:

	def __init__(self, type):
		self.type = type
		self.hp = 0
		self.strength = 0
		self.damageMin = 5
		self.damageMax = 10

		if(type == EnemyType.EASY):
			self.hp = 25
			self.strength = 1
		elif(type == EnemyType.MEDIUM):
			self.hp = 50
			self.strength = 1.5
		else:
			self.hp = 75
			self.strength = 2

	def getType(self):
		return self.type

	def loseHealth(self, val):
		self.hp -= val

	def getHealth(self):
		return self.hp

	# return a random value based on the strength of the enemy
	def attack(self, player):
		if(self.type == EnemyType.HARD):
			print("Hard attack")
		damage = self.strength * (random.choice(range(self.damageMin, self.damageMax)))
		player.loseHealth(damage)
		if(self.type == EnemyType.HARD):
			print(f"Hard attack for {damage} damage")
		pass
