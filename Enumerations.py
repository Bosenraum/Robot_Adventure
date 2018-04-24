from enum import Enum

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
	FUN	   = 4
	EMPTY  = 5
	START  = 6
	END	   = 7

class FunType(Enum):
	RIDDLE = 1 # Sphinx riddle
	PUZZLE = 2 # A basic puzzle
	BOSS   = 3 # Fight a strong enemy that you can't flee from

class SoundEffect(Enum):
	THEME   = 1
	BOSS	= 2
	WEAK	= 3
	MEDIUM  = 4
	HARD	= 5
	LOSE	= 6
	WIN	    = 7
	WRONG   = 8
	TWINKLE = 9
	SPHINX  = 10
	COFFEE  = 11
	HEAL    = 12
	VANISH  = 13
	BEST    = 14

class EnemyType(Enum):
	EASY   = 1
	MEDIUM = 2
	HARD   = 3
	BOSS   = 4
