import Jogo

class Player(object):
	"""construtor do Player"""
	def __init__(self, simb):
		super(Player, self).__init__()
		self.simb = simb
	#
	def getSimb(self):
		return self.simb
	#termina o jogo caso o jogador queira se render
	def surrender(self):
		self.perdeJogo()
	#
	def perdeJogo():
		pass

	def venceJogo():
		pass