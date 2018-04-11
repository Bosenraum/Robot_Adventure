from Spot import *
#from Characters import *
from Map import GameMap
#mport random

print("WELCOME TO YOUR NIGHTMARE")

map = GameMap.makeMap()

dict = GameMap.fillMap(map)
cur = dict["Spot"]
player = dict["Player"]

Spot.setPlayer(player)
Spot.setCur(cur)

GameMap.printMap(map)

dir = input("Where would you like to go? >> ")
while(dir.lower() != "quit"):
	if(dir.lower() == "north"):
		# cur = cur.move(Directions.NORTH)
		Spot.getCur().move(Directions.NORTH)
	elif(dir.lower() == "east"):
		Spot.getCur().move(Directions.EAST)
	elif(dir.lower() == "south"):
		Spot.getCur().move(Directions.SOUTH)
	elif(dir.lower() == "west"):
		Spot.getCur().move(Directions.WEST)
	else:
		print("That's not a valid direction")
	GameMap.printMap(map)
	dir = input("Where would you like to go? >> ")
