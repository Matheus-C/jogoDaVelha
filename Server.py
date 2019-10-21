import Player
import Jogo
import socket, threading
#thread para multiplas conexoes
class Conexoes(threading.Thread):
	"""Construtor de Conexoes parâmetros: con = conexao, jogador = identificador de jogador"""
	def __init__(self, con, cliente, jogador):
		threading.Thread.__init__(self)
		self.con = con
		self.cliente = cliente
		self.jogador = jogador

	def run():
		while True:
			#recebe a jogada do player ativo
			jogada = self.con.recv(1024)
			if Jogo.fimDeJogo():
				break
			#faz a jogada requisitada
			Player.jogada(jogada, self.jogador)
			#envia o tabuleiro para mostrar o estado atual
			self.con.send(Jogo.getGame().encode())
		print('Finalizando conexao do cliente', self.cliente)
		self.con.close()

		


HOST = ""
PORT = 6854
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
i = 0#identificador do player
while True:
	tcp.listen(1)
	con, cliente = tcp.accept()
	print('Conectado por', cliente)
	i += 1
	newConnection = Conexoes(con, cliente, i)
	newConnection.start()