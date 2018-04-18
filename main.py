# CSCI-455 Final Project - Robot Adventure
# Austin Rosenbaum and Andrew Beck

# Sound effects obtained from https://www.zapsplat.com

from Spot import *
from Music import *
from Map import GameMap
from Enumerations import *
# from numpy import roll
import threading, time
# import pygame.mixer
#from Characters import *
#import random

Sounds.init()

Sounds.playSound(SoundEffect.THEME)

# Choose gameplay mode
print("CHOOSE DIFFICULTY:")
print("  (1) EASY")
print("  (2) HARD")

mode = input(">> ")
while(mode != '1' and mode != '2'):
	print("CHOOSE 1 OR 2")
	mode = input(">> ")



northWords = ["north", "up", "orth", "nrth", "noth", "norh", "nort", "onrth", "forward", "forwards"]
eastWords  = ["east", "right", "ast", "eat", "eas", "aest"]
southWords = ["south", "down", "outh", "suth", "soth", "souh", "sout", "suoth", "osuth", "backward", "backwards"]
westWords  = ["west", "left", "wst", "wet", "wes", "ewst"]

forwardList = ["forward", "forwards", "up", "f", "u"]
rightList   = ["right", "r"]
leftList    = ["left", "l"]
backList	= ["back", "backward", "backwards", "down", "b", "d"]



movesAllowed = Player.maxMoves

print("WELCOME TO YOUR NIGHTMARE")

map = GameMap.makeMap()

dict = GameMap.fillMap(map)
cur = dict["Spot"]
player = dict["Player"]

Spot.setPlayer(player)
Spot.setCur(cur)
if(mode == "1"):
	GameMap.printMap(map)

Spot.getCur().validMoves()
dir = input("WHERE WOULD YOU LIKE TO GO? >> ")
while(dir.lower() != "quit" and player.getMovesTaken() != Player.maxMoves):
	printMap = True
	cur = Spot.getCur()
	if(dir.lower() in forwardList):
		# Spot.getCur().move(Directions.NORTH)
		cur.move(player.getOrientation()[0])
	elif(dir.lower() in rightList):
		# Spot.getCur().move(Directions.EAST)
		cur.move(player.getOrientation()[1])
		# Rotate the orientation list
		player.turnRight()
	elif(dir.lower() in backList):
		# Spot.getCur().move(Directions.SOUTH)
		cur.move(player.getOrientation()[2])
		player.turnRight()
		player.turnRight()
	elif(dir.lower() in leftList):
		# Spot.getCur().move(Directions.WEST)
		cur.move(player.getOrientation()[3])
		player.turnLeft()
	elif(dir.lower() == "status"):
		player.getStatus()
	elif(dir.lower() == "skip"):
		player.move()
	elif(dir.lower() == "die"):
		break
	else:
		print("INVALID DIRECTION")
		printMap = False
	if(printMap and mode == "1"):
		pass
		GameMap.printMap(map)
	GameMap.clearVisited()

	remaining = player.getRemaining()
	if(remaining == 1):
		print("LAST MOVE")
	elif(remaining == 0):
		break
	elif(remaining <= 5):
		print(f"{remaining} MOVES LEFT")
	Spot.getCur().validMoves()
	dir = input("WHERE WOULD YOU LIKE TO GO? >> ")

remaining = player.getRemaining()
if(dir.lower() == "quit"):
	print("QUITTER!")
	player.lose()
elif(remaining == 0):
	player.lose()
else:
	player.lose()
