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

def fillMap():
    # put the player down first
    # Get player name
    name = input("What is your name? >> ")
    if(name.lower() == "jake"):
        print("Sorry, you can't play.")
        exit()
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

    # 6 Easy enemies
    # 5 Medium enemies
    # 3 Hard enemies
    for i in range(6):
        Enemy(EnemyType.EASY)
    for i in range(5):
        Enemy(EnemyType.MEDIUM)
    for i in range(3):
        Enemy(EnemyType.HARD)

    # 3 Recharge stations
    # 2 coffee shops
    # 3 fun spots
    # 3 empty

    return {"Spot": cur, "Player": player}


map = GameMap.makeMap()

dict = fillMap()
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
