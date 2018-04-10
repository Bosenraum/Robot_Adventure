from Spot import *
from Characters import *
from Map import GameMap

map = GameMap.makeMap()

cur = map[3][2]
cur.enter()
GameMap.printMap(map)
cur = cur.move(Directions.EAST)
cur = cur.move(Directions.SOUTH)
cur = cur.move(Directions.WEST)
cur = cur.move(Directions.NORTH)

GameMap.printMap(map)
