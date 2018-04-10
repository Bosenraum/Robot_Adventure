from Spot import *
from Characters import *

# Create 2D array of spots
map = [[]*5 for i in range(5)]

    #print(str(i))
offset = 0
for i in range(len(map)):
    for j in range(len(map)):
        map[i].append(Spot(j + offset))
    offset += 5

# Set all map connections
                    #(  N  ,   E ,   S  ,   W  )
map[0][0].setConnections(False, True, False, False)
map[0][1].setConnections(False, True, True, True)
map[0][2].setConnections(False, False, True, True)
map[0][3].setConnections(False, True, False, False)
map[0][4].setConnections(False, False, True, True)

map[1][0].setConnections(False, True, True, False)
map[1][1].setConnections(True, False, True, True)
map[1][2].setConnections(True, False, False, False)
map[1][3].setConnections(False, True, True, False)
map[1][4].setConnections(True, False, True, True)

map[2][0].setConnections(True, False, True, False)
map[2][1].setConnections(True, True, False, False)
map[2][2].setConnections(False, True, False, True)
map[2][3].setConnections(True, False, True, True)
map[2][4].setConnections(True, False, True, False)

map[3][0].setConnections(True, True, False, False)
map[3][1].setConnections(False, False, True, True)
map[3][2].setConnections(False, False, True, False)
map[3][3].setConnections(True, True, True, False)
map[3][4].setConnections(True, False, False, True)

map[4][0].setConnections(False, True, False, False)
map[4][1].setConnections(True, True, False, True)
map[4][2].setConnections(True, False, False, True)
map[4][3].setConnections(True, True, False, False)
map[4][4].setConnections(False, False, False, True)

# connect all spots
for i in range(len(map)):
    for j in range(len(map)):
        if(map[i][j].getNorth()):
            map[i][j].setNorthSpot(map[i-1][j])
        if(map[i][j].getEast()):
            map[i][j].setEastSpot(map[i][j+1])
        if(map[i][j].getSouth()):
            map[i][j].setSouthSpot(map[i+1][j])
        if(map[i][j].getWest()):
            map[i][j].setWestSpot(map[i][j-1])

cur = map[0][0]
cur.enter()
cur = cur.move(Directions.EAST)
cur = cur.move(Directions.SOUTH)
cur = cur.move(Directions.WEST)
cur = cur.move(Directions.NORTH)

# print the map
for r in map:
    for c in r:
        c.printRow()
    print()
    for c in r:
        c.printColumn()
    print()
