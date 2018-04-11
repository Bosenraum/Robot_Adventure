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

def getOpenSpot():
    seq = [0,1,2,3,4]
    row = random.choice(seq)
    col = random.choice(seq)
    while(map[row][col].getMarked()):
        row = random.choice(seq)
        col = random.choice(seq)

    print(f"Row-Col : {row}-{col}")
    return map[row][col]

def fillMap():
    # put the player down first
    # Get player name
    name = "Austin"#input("What is your name? >> ")
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

    cur = map[row][column]
    cur.setType(SpotType.START)
    cur.enter()

    # Select the end location to be opposite the start
    if(column < 3):
        endCol = random.choice([3,4])
    else:
        endCol = random.choice([0,1,2])
    endRow = random.choice([0,1,2,3,4])
    endSpot = map[endRow][endCol]
    endSpot.setType(SpotType.END)

    # 3 Recharge stations
    # 2 coffee shops
    # 3 fun spots
    for i in range(3):
        # put recharge stations
        spot = getOpenSpot()
        while(spot.checkNeighbors(SpotType.CHARGE)):
            spot = getOpenSpot()
        spot.setType(SpotType.CHARGE)
        #GameMap.printMap(map)
    for i in range(2):
        # put coffee shops
        pass
    for i in range(3):
        # place fun spots
        pass

    # 6 Easy, 5 Medium,3 Hard enemies
    for i in range(6):
        #print(str(i))
        e = Enemy(EnemyType.EASY)
        spot = getOpenSpot()
        spot.setEnemy(e)
        spot.setType(SpotType.FIGHT)
    for i in range(5):
        e = Enemy(EnemyType.MEDIUM)
        spot = getOpenSpot()
        spot.setEnemy(e)
        spot.setType(SpotType.FIGHT)
    for i in range(3):
        e = Enemy(EnemyType.HARD)
        spot = getOpenSpot()
        spot.setEnemy(e)
        spot.setType(SpotType.FIGHT)
        print(str(i))
    print("Done placing")
    #GameMap.printMap(map)

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
