from Player import Player
from Jogo import Jogo
import socket, threading, time

#thread para multiplas conexoes
class Conexoes(threading.Thread):
	"""Construtor de Conexoes parâmetros: con = conexao, jogador = identificador de jogador"""
	def __init__(self, con, cliente, p, game):
		threading.Thread.__init__(self)
		self.con = con
		self.cliente = cliente
		self.p = p
		self.game = game

	def fimDeJogo(self):
		if game.getStatus() != 0:
				if game.getStatus() == self.p.getN():
					self.con.send("parabéns você venceu".encode())
				elif game.getStatus() == 3:
					self.con.send("empatou".encode())
				else:
					self.con.send("você perdeu".encode())
				lock.release()
				self.con.close()

	def run(self):
		while True:
			lock.acquire()
			self.fimDeJogo()
			self.con.send("sua vez".encode())
			#envia o tabuleiro para mostrar o estado atual
			self.con.send(game.getGame().encode())
			#recebe a jogada do player ativo
			jogada = self.con.recv(1024).decode()
			#faz a jogada requisitada
			self.game.posSimb(int(jogada), self.p)
			self.fimDeJogo()
			self.con.send("vez do oponente".encode())
			lock.release()
			time.sleep(1)

lock = threading.Lock()
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
	if i < 3:
		if i == 1:
			game = Jogo()
			p1 = Player(" O ", i)
			player1 = Conexoes(con, cliente, p1, game)
			
		else:
			p2 = Player(" X ", i)
			player2 = Conexoes(con, cliente, p2, game)
			player1.start()
			player2.start()
			
