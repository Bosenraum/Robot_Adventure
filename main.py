from Spot import *
from Characters import *
from Map import GameMap

map = GameMap.makeMap()

cur = map[3][2]
cur.enter()

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
