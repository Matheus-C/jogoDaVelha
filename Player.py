class Player(object):
	"""construtor do Player"""
	def __init__(self, symbol, turn):
		super(Player, self).__init__()
		self.symbol = symbol
		self.turn = turn
	#
	def getSymbol(self):
		return self.symbol

	def getTurn(self):
		return self.turn