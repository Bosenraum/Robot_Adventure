# CSCI-455 Final Project - Robot Adventure
# Austin Rosenbaum and Andrew Beck

# Sound effects obtained from https://www.zapsplat.com

from Spot import *
from Music import *
from Map import GameMap
from Enumerations import *
from Instruction import *
from Network import *
import time

Sounds.init()

Sounds.playSound(SoundEffect.THEME)

# Choose gameplay mode
createSendThread("CHOOSE DIFFICULTY EASY OAR HARD", 10, 10, "t")
print("CHOOSE DIFFICULTY:")
print("  (1) EASY")
print("  (2) HARD")

mode = receive()
while(mode.lower() != 'easy' and mode.lower() != 'hard'):
	print("CHOOSE EASY OR HARD")
	createSendThread("CHOOSE EASY OR HARD", 10, 10, "t")
	mode = receive()



northWords = ["north", "up", "orth", "nrth", "noth", "norh", "nort", "onrth", "forward", "forwards"]
eastWords  = ["east", "right", "ast", "eat", "eas", "aest"]
southWords = ["south", "down", "outh", "suth", "soth", "souh", "sout", "suoth", "osuth", "backward", "backwards"]
westWords  = ["west", "left", "wst", "wet", "wes", "ewst"]

forwardList = ["forward", "forwards", "up", "f", "u"]
rightList   = ["right", "r", "write"]
leftList    = ["left", "l"]
backList	= ["back", "backward", "backwards", "down", "b", "d"]



movesAllowed = Player.maxMoves

print("WELCOME TO THE ADVENTURE")
createSendThread("WELCOME TO THE ADVENTURE!", 10, 10, "f")
wave()


map = GameMap.makeMap()

dict = GameMap.fillMap(map)
cur = dict["Spot"]
player = dict["Player"]

Spot.setPlayer(player)
Spot.setCur(cur)
if(mode == "easy"):
	GameMap.printMap(map)

Spot.getCur().validMoves()
# dir = input("WHERE WOULD YOU LIKE TO GO? >> ")
createSendThread("WHERE WOULD YOU LIKE TO GO?", 10, 10, "t")
dir = receive()
while(dir.lower() != "quit" and player.getMovesTaken() != Player.maxMoves):
	printMap = True
	cur = Spot.getCur()
	if(dir.lower() in forwardList):
		forward.execute()
		# Spot.getCur().move(Directions.NORTH)
		cur.move(player.getOrientation()[0])
	elif(dir.lower() in rightList):
		turnRight.execute()
		forward.execute()
		# Spot.getCur().move(Directions.EAST)
		cur.move(player.getOrientation()[1])
		# Rotate the orientation list
		player.turnRight()
	elif(dir.lower() in backList):
		turnAround.execute()
		forward.execute()
		# Spot.getCur().move(Directions.SOUTH)
		cur.move(player.getOrientation()[2])
		player.turnRight()
		player.turnRight()
	elif(dir.lower() in leftList):
		turnLeft.execute()
		forward.execute()
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

	cur = Spot.getCur()
	if(cur.getType() == SpotType.COFFEE):
		nextDir = cur.DFS()
		#print(nextDir)

		# convert this cardinal direction to a relative one based on the player's orientation
		nextDir = player.getRelativeDir(nextDir)
		if(nextDir == None):
			print("ERROR: NO END FOUND")
		elif(nextDir == "error"):
			print("ERROR: ERROR WAS RETURNED")
		else:
			sentence = "YOU MUST GO " + nextDir.upper() + " FROM HERE TO REACH THE END"
			print("YOU MUST GO %s FROM HERE TO REACH THE END\n" % nextDir.upper())
			createSendThread(sentence, 10, 10, "f")


	if(printMap and mode == "easy"):
		GameMap.printMap(map)
	GameMap.clearVisited()

	remaining = player.getRemaining()
	if(remaining == 1):
		print("LAST MOVE")
		createSendThread("LAST MOVE", 10, 10, "f")
	elif(remaining == 0):
		break
	elif(remaining <= 5):
		#print(f"{remaining} MOVES LEFT")	doesn't work in python 3.4
		move_left = str(remaining) + " MOVES LEFT"
		print("%d MOVES LEFT" % remaining)
		createSendThread(move_left, 10, 10, "f")
	Spot.getCur().validMoves()
	createSendThread("WHERE WOULD YOU LIKE TO GO?", 10, 10, "t")
	dir = receive()

remaining = player.getRemaining()
if(dir.lower() == "quit"):
	print("QUITTER!")
	createSendThread("QUITTER!", 20, 10, "f")
	player.lose()
elif(remaining == 0):
	player.lose()
else:
	player.lose()
