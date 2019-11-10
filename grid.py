import pygame
import os

playerX = pygame.image.load(os.path.join('assets', 'X.png'))
playerO = pygame.image.load(os.path.join('assets', 'O.png'))

class Grid:
	def __init__(self):
		self.gridLines = [
			# Horizontais
			((0, 200), (600, 200)), 
			((0, 400), (600, 400)),
			# Verticais
			((200, 0), (200, 600)),
			((400, 0), (400, 600)),
		]

		# Gera uma matriz => [3][3]
		self.grid = [[0 for x in range(3)] for y in range(3)]

		#self.changePlayer = True
		self.gameOver = False
	def getGameOver():
		return self.gameOver

	def getGameOver(self):
		self.gameOver = False

	def getSquareValue(self, x , y):
		return self.grid[x][y]

	def setSquareValue(self, x, y, value):
		self.grid[x][y] = value

	def getSquareClick(self, x, y, player):
		if (self.getSquareValue(x, y) == 0):
			self.setSquareValue(x, y, player)
			return 1
		else:
			return 0


	def buildGrid(self, surface):
		for line in self.gridLines:
			# Args... => (Janela, cor, inicio, fim, largura)
			pygame.draw.line(surface, (0,0,0), line[0], line[1], 5)
		# PESQUISAR SOBRE 
		for x in range(len(self.grid)):
			for y in range(len(self.grid[x])):
				if (self.getSquareValue(x, y) == "X"):
					surface.blit(playerX, (y * 200, x * 200))
				elif (self.getSquareValue(x, y) == "O"):
					surface.blit(playerO, (y * 200, x * 200))
		# PESQUISAR SOBRE 

	# Para debugar	 
	def gridPrint(self):
		for line in self.grid:
			print(line)

	def gridClear(self):
		for x in range(len(self.grid)):
			for y in range(len(self.grid[x])):
				self.setSquareValue(x, y, 0)

	def winGame(self, player):
		print('O Player "'+ player + '" Venceu!')
		self.gameOver = True

	def tie(self):
		print("Deu empate!")
		self.gameOver = True

	def checkGame(self, x, y, player):
		# Analisa a condição de vitória nas linhas horizontais
		for x in range(3):
			if player == self.getSquareValue(x, 0):
				if self.getSquareValue(x, 0) == self.getSquareValue(x, 1) and self.getSquareValue(x, 0) == self.getSquareValue(x, 2):
					self.winGame(player)
					return

		# Analisa a condição de vitória nas linhas verticais
		for y in range(3):
			if player == self.getSquareValue(0, y):
				if self.getSquareValue(0, y) == self.getSquareValue(1, y) and self.getSquareValue(0, y) == self.getSquareValue(2, y):
					self.winGame(player)
					return
		# Analisa a 1ª linha diagonal
		if player == self.getSquareValue(0, 0):
			if self.getSquareValue(0, 0) == self.getSquareValue(1, 1) and self.getSquareValue(0, 0) == self.getSquareValue(2, 2):
				self.winGame(player)
				return
		# Analisa a 2ª linha diagonal
		if player == self.getSquareValue(0, 2):
			if self.getSquareValue(0, 2) == self.getSquareValue(1, 1) and self.getSquareValue(0, 2) == self.getSquareValue(2, 0):
				self.winGame(player)
				return
		# Analisa se ocorreu empate
		check = 0
		for x in range(3):
			for y in range(3):
				if (self.getSquareValue(x, y) == "X") or (self.getSquareValue(x, y) == "O"):
					check += 1
		if check == 9:
			self.tie()
			return