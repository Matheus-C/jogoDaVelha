import Player

class Jogo(object):
	"""construtor do Jogo"""
	def __init__(self):
		super(Jogo, self).__init__()
		self.game = [[" 1 ", " 2 ", " 3 "], [" 4 ", " 5 ", " 6 "], [" 7 ", " 8 ", " 9 "]]
		self.status = 0
	#seta o tabuleiro inicial
	"""def setGame():
		return """
	#retorna o status do jogo (se acabou ou não)
	def getStatus(self):
		return self.status

	def setStatus(self, n):
		self.status = n
	#posiciona o X ou O 
	def posSimb(self, pos, p):
		simb = p.getSimb()
		if pos <= 3:
			self.game[0][pos - 1] = simb
		elif pos <= 6:
			self.game[1][pos - 4] = simb
		else:
			self.game[2][pos - 7] = simb
		self.vitoria(p)
	#termina o jogo
	def fimDeJogo(self):
		self.status = 0
	#retorna o estado atual do tabuleiro
	def getGame(self):
		return str(self.game[0]).strip() + "\n" + str(self.game[1]).strip() + "\n" + str(self.game[2]).strip()

	def empate(self):
		self.setStatus(3)
	#analisa todas as linhas verticais se a condição de vitória foi preenchida
	def vitoria(self, p):
		for i in range(3):
			if p.simb == self.game[0][i]:
				if (self.game[0][i] == self.game[1][i]) and (self.game[0][i] == self.game[2][i]):
					self.setStatus(p.getN())
					return
		#analisa todas as linhas horizontais se a condição de vitória foi preenchida
		for i in range(3):
			if p.simb == self.game[i][0]:
				if (self.game[i][0] == self.game[i][1]) and (self.game[i][0] == self.game[i][2]):
					self.setStatus(p.getN())
					return
		#analisa a 1ª linha diagonal
		if p.simb == self.game[0][0]:
			if (self.game[0][0] == self.game[1][1]) and (self.game[0][0] == self.game[2][2]):
				self.setStatus(p.getN())
				return
		#analisa a 2ª linha diagonal
		if p.simb == self.game[0][2]:
			if (self.game[0][2] == self.game[1][1]) and (self.game[0][2] == self.game[2][0]):
				self.setStatus(p.getN())
				return
		#analisa se ocorreu empate
		check = 0
		for x in range(3):
			for y in range(3):
				if (self.game[x][y] == " X ") or (self.game[x][y] == " O "):
					check += 1
		if check == 9:
			self.empate()
			return