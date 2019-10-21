import Jogo

class Player(object):
	"""construtor do Player"""
	def __init__(self, simbolo):
		super(Player, self).__init__()
		self.simbolo = simbolo
	#
	def jogada(self, game, pos, simbolo):
		pass
	#termina o jogo caso o jogador queira se render
	def surrender(self):
		Jogo.FimDeJogo()
	#
	def perdeJogo():
		pass

	def venceJogo():
		pass