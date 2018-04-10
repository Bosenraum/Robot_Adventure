# Create different enemies
# Create player character'

from enum import Enum

class EnemyType(Enum):
    EASY   = 1
    MEDIUM = 2
    HARD   = 3

class Player:

    def __init__(self):
        pass

class Enemy:

    def __init__(self, type):
        self.type = type
        pass
