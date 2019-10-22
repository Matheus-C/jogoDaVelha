import Jogo

class Player(object):
	"""construtor do Player"""
	def __init__(self, simb, n):
		super(Player, self).__init__()
		self.simb = simb
		self.n = n
	#
	def getSimb(self):
		return self.simb

	def getN(self):
		return self.n