from Spot import *
from Characters import *
import random



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

	@staticmethod
	def selectRow(seq):
		val = random.choice(seq)
		return val

	@staticmethod
	def selectColumn(seq):
		val = random.choice(seq)
		return val

	@staticmethod
	def getOpenSpot():
		seq = [0,1,2,3,4]
		row = random.choice(seq)
		col = random.choice(seq)
		while(GameMap.map[row][col].getMarked()):
			row = random.choice(seq)
			col = random.choice(seq)

		#print(f"Row-Col : {row}-{col}")
		return GameMap.map[row][col]

	@staticmethod
	def fillMap(map):
		# put the player down first
		# Get player name
		name = input("What is your name? >> ")
		if(name.lower() == "jake"):
			print("Sorry, you can't play.")
			exit()
		player = Player(name)

		coinFlip = random.choice([True, False])

		if(coinFlip):
			row = GameMap.selectRow([0,1,2,3,4])
			column = GameMap.selectColumn([0,4])
		else:
			column = GameMap.selectColumn([0,1,2,3,4])
			row = GameMap.selectRow([0,4])

		cur = map[row][column]
		cur.setType(SpotType.START)
		cur.enter()

		# Select the end location to be on opposite edge from start

		if(column == 0):
			endCol = 4
			endRow = random.choice([0,1,2,3,4])
		elif(column == 4):
			endCol = 0
			endRow = random.choice([0,1,2,3,4])
		elif(row == 0):
			endRow = 4
			endCol = random.choice([0,1,2,3,4])
		else:
			endRow = 0
			endCol = random.choice([0,1,2,3,4])
		#endRow = random.choice([0,1,3,4])
		endSpot = map[endRow][endCol]
		endSpot.setType(SpotType.END)

		# 3 Recharge stations
		# 2 coffee shops
		# 3 fun spots
		for i in range(3):
			# put recharge stations
			spot = GameMap.getOpenSpot()
			while(spot.checkNeighbors(SpotType.CHARGE)):
				spot = GameMap.getOpenSpot()
			spot.setType(SpotType.CHARGE)
			#GameMap.printMap(map)
		for i in range(2):
			# put coffee shops
			spot = GameMap.getOpenSpot()
			while(spot.checkNeighbors(SpotType.COFFEE)):
				spot = GameMap.getOpenSpot()
			spot.setType(SpotType.COFFEE)

		for i in range(3):
			# place fun spots
			spot = GameMap.getOpenSpot()
			while(spot.checkNeighbors(SpotType.FUN)):
				spot = GameMap.getOpenSpot()
			spot.setType(SpotType.FUN)

		# 6 Easy, 5 Medium,3 Hard enemies
		for i in range(3):
			e = Enemy(EnemyType.HARD)
			spot = GameMap.getOpenSpot()
			while(spot.checkNeighborEnemies(EnemyType.HARD)):
				spot = GameMap.getOpenSpot()
			spot.setEnemy(e)
			spot.setType(SpotType.FIGHT)
			#print(str(i))
		for i in range(6):
			#print(str(i))
			e = Enemy(EnemyType.EASY)
			spot = GameMap.getOpenSpot()
			spot.setEnemy(e)
			spot.setType(SpotType.FIGHT)
		for i in range(5):
			e = Enemy(EnemyType.MEDIUM)
			spot = GameMap.getOpenSpot()
			spot.setEnemy(e)
			spot.setType(SpotType.FIGHT)

		print("Done placing")
		#GameMap.printMap(map)

		return {"Spot": cur, "Player": player}
