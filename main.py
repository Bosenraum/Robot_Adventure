# CSCI-455 Final Project - Robot Adventure
# Austin Rosenbaum and Andrew Beck

# Sound effects obtained from https://www.zapsplat.com

from Spot import *
from Music import *
from Map import GameMap
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


northWords = ["north", "up", "orth", "nrth", "noth", "norh", "nort", "onrth"]
eastWords  = ["east", "right", "ast", "eat", "eas", "aest"]
southWords = ["south", "down", "outh", "suth", "soth", "souh", "sout", "suoth", "osuth"]
westWords  = ["west", "left", "wst", "wet", "wes", "ewst"]

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
dir = input("Where would you like to go? >> ")
while(dir.lower() != "quit" and player.getMovesTaken() != Player.maxMoves):
	printMap = True
	if(dir.lower() in northWords):
		Spot.getCur().move(Directions.NORTH)
	elif(dir.lower() in eastWords):
		Spot.getCur().move(Directions.EAST)
	elif(dir.lower() in southWords):
		Spot.getCur().move(Directions.SOUTH)
	elif(dir.lower() in westWords):
		Spot.getCur().move(Directions.WEST)
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
	dir = input("Where would you like to go? >> ")

remaining = player.getRemaining()
if(dir.lower() == "quit"):
	print("QUITTER!")
elif(remaining == 0):
	player.lose()
else:
	player.lose()
