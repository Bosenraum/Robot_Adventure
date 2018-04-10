from Spot import *

class GameMap:
    map = []

    def __init__(self):
        pass

    @staticmethod
    def makeMap():
        GameMap.map = [[]*5 for i in range(5)]
        offset = 0
        for i in range(len(GameMap.map)):
            for j in range(len(GameMap.map)):
                GameMap.map[i].append(Spot(j + offset))
            offset += 5

        # Set all map connections
                            #(  N  ,   E ,   S  ,   W  )
        GameMap.map[0][0].setConnections(False, True, False, False)
        GameMap.map[0][1].setConnections(False, True, True, True)
        GameMap.map[0][2].setConnections(False, False, True, True)
        GameMap.map[0][3].setConnections(False, True, False, False)
        GameMap.map[0][4].setConnections(False, False, True, True)

        GameMap.map[1][0].setConnections(False, True, True, False)
        GameMap.map[1][1].setConnections(True, False, True, True)
        GameMap.map[1][2].setConnections(True, False, False, False)
        GameMap.map[1][3].setConnections(False, True, True, False)
        GameMap.map[1][4].setConnections(True, False, True, True)

        GameMap.map[2][0].setConnections(True, False, True, False)
        GameMap.map[2][1].setConnections(True, True, False, False)
        GameMap.map[2][2].setConnections(False, True, False, True)
        GameMap.map[2][3].setConnections(True, False, True, True)
        GameMap.map[2][4].setConnections(True, False, True, False)

        GameMap.map[3][0].setConnections(True, True, False, False)
        GameMap.map[3][1].setConnections(False, False, True, True)
        GameMap.map[3][2].setConnections(False, False, True, False)
        GameMap.map[3][3].setConnections(True, True, True, False)
        GameMap.map[3][4].setConnections(True, False, False, True)

        GameMap.map[4][0].setConnections(False, True, False, False)
        GameMap.map[4][1].setConnections(True, True, False, True)
        GameMap.map[4][2].setConnections(True, False, False, True)
        GameMap.map[4][3].setConnections(True, True, False, False)
        GameMap.map[4][4].setConnections(False, False, False, True)

        # connect all spots
        for i in range(len(GameMap.map)):
            for j in range(len(GameMap.map)):
                if(GameMap.map[i][j].getNorth()):
                    GameMap.map[i][j].setNorthSpot(GameMap.map[i-1][j])
                if(GameMap.map[i][j].getEast()):
                    GameMap.map[i][j].setEastSpot(GameMap.map[i][j+1])
                if(GameMap.map[i][j].getSouth()):
                    GameMap.map[i][j].setSouthSpot(GameMap.map[i+1][j])
                if(GameMap.map[i][j].getWest()):
                    GameMap.map[i][j].setWestSpot(GameMap.map[i][j-1])
        return GameMap.map
    # print the map
    @staticmethod
    def printMap(map):
        for r in map:
            for c in r:
                c.printRow()
            print()
            for c in r:
                c.printColumn()
            print()

        #print(str(i))
