# Create map spots

from enum import Enum

# Enumerate directions for later
class Directions(Enum):
    NORTH = 1
    EAST  = 2
    SOUTH = 3
    WEST  = 4

class SpotType(Enum):
    CHARGE = 1
    COFFEE = 2
    FIGHT  = 3
    FUN    = 4
    EMPTY  = 5

class Spot:

    def __init__(self, val):
        self.marked  = False
        self.entered = False
        self.val = val + 1

    def __str__(self):
        return str(self.val)

    # What to do when the player enters this spot
    def enter(self):
        self.entered = True

    def leave(self):
        self.entered = False

    def move(self, dir):
        if(self.isValidDir(dir)):
            self.leave()
            if(dir == Directions.NORTH):
                self.northSpot.enter()
                return self.northSpot
            if(dir == Directions.EAST):
                self.eastSpot.enter()
                return self.eastSpot
            if(dir == Directions.SOUTH):
                self.southSpot.enter()
                return self.southSpot
            if(dir == Directions.WEST):
                self.westSpot.enter()
                return self.westSpot
        else:
            print("INVALID MOVE")
            return self

    def isValidDir(self, dir):
        if(dir == Directions.NORTH and self.north):
            return True
        elif(dir == Directions.EAST and self.east):
            return True
        elif(dir == Directions.SOUTH and self.south):
            return True
        elif(dir == Directions.WEST and self.west):
            return True
        else:
            return False

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type
        self.marked = True

    def setConnections(self, north=False, east=False, south=False, west=False):
        self.north = north
        self.east  = east
        self.south = south
        self.west  = west

    def getNorth(self):
        return self.north

    def setNorthSpot(self, spot):
        self.northSpot = spot

    def getEast(self):
        return self.east

    def setEastSpot(self, spot):
        self.eastSpot = spot

    def getSouth(self):
        return self.south

    def setSouthSpot(self, spot):
        self.southSpot = spot

    def getWest(self):
        return self.west

    def setWestSpot(self, spot):
        self.westSpot = spot

    def printRow(self):
        if(self.entered):
            print("XX", end="")
        else:
            if(self.val <= 10):
                print(" " + str(self.val), end="")
            else:
                print(self.val, end="")

        if(self.east):
            print("---", end="")
        else:
            print("   ", end="")

    def printColumn(self):
        if(self.south):
            print(" |   ", end="")
        else:
            print("     ", end="")
