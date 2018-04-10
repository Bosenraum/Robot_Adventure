from Spot import *
from Characters import *
from Map import GameMap
import random

def selectRow(seq):
    val = random.choice(seq)
    return val

def selectColumn(seq):
    val = random.choice(seq)
    return val


map = GameMap.makeMap()

# Get player name
name = input("What is your name? >> ")
player = Player(name)

coinFlip = random.random() * 2

if(coinFlip < 1):
    row = selectRow([0,1,2,3,4])
    column = selectColumn([0,4])
else:
    column = selectColumn([0,1,2,3,4])
    row = selectRow([0,4])

print(f"Row: {row + 1}   Column: {column + 1}")

cur = map[row][column]
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
