# Create different enemies
# Create player character'

from enum import Enum

class EnemyType(Enum):
    EASY   = 1
    MEDIUM = 2
    HARD   = 3

class Player:

    def __init__(self, name):
        self.name = name
        self.hp = 100

    def getName(self):
        return self.name

class Enemy:

    def __init__(self, type):
        self.type = type
        self.hp = 0
        self.strength = 0
        if(type == EnemyType.EASY):
            self.hp = 25
            self.strength = 1
        elif(type == EnemyType.MEDIUM):
            self.hp = 50
            self.strength = 1.5
        else:
            self.hp = 75
            self.strenght = 2

    def getType(self):
        return self.type

    # return a random value based on the strength of the enemy
    def attack(self):
        pass
