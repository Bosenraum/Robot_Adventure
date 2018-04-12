from Spot import *
from Map import GameMap
import re
#from Characters import *
#mport random

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
		player.lose()
	else:
		print("INVALID DIRECTION")
		printMap = False
	if(printMap):
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
	print("WHAT HAPPENED?")
