from Spot import Directions
#from Characters import *
from Map import GameMap
#mport random

map = GameMap.makeMap()

dict = GameMap.fillMap(map)
cur = dict["Spot"]
player = dict["Player"]

GameMap.printMap(map)

dir = input("Where would you like to go? >> ")
while(dir.lower() != "quit"):
	if(dir.lower() == "north"):
		cur = cur.move(Directions.NORTH)
	elif(dir.lower() == "east"):
		cur = cur.move(Directions.EAST)
	elif(dir.lower() == "south"):
		cur = cur.move(Directions.SOUTH)
	elif(dir.lower() == "west"):
		cur = cur.move(Directions.WEST)
	else:
		print("That's not a valid direction")
	GameMap.printMap(map)
	dir = input("Where would you like to go? >> ")
