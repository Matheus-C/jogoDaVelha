import Player

class Jogo(object):
	"""construtor do Jogo"""
	def __init__(self):
		super(Jogo, self).__init__()
		self.game = setGame()
		self.status = 1
	#seta o tabuleiro inicial
	def setGame():
		return [[" . "][" . "][" . "], [" . "][" . "][" . "], [" . "][ ". "][" . "]]
	#retorna o status do jogo (se acabou ou não)
	def getStatus(self):
		return self.status
	#posiciona o X ou O 
	def posicionaSimbolo(self, simb, pos):
		pass
	#termina o jogo
	def fimDeJogo(self):
		self.status = 0
	#retorna o estado atual do tabuleiro
	def getGame(self):
		return strip(str(self.game[0])) + "\n" + strip(str(self.game[1])) + "\n" + strip(str(self.game[2]))