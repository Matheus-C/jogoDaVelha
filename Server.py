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
#falta enviar o estado do tabuleiro para outro jogador (ou seja identificar as threads e faze-las enviar para o outro jogador apos uma jogada)
	def run(self):
		while True:
			
			lock.acquire()
			self.con.send("sua vez".encode())
			#envia o tabuleiro para mostrar o estado atual
			self.con.send(game.getGame().encode())
			#recebe a jogada do player ativo
			jogada = self.con.recv(1024).decode()
			#faz a jogada requisitada
			self.game.posSimb(int(jogada), self.p)
			if not game.getStatus():
				self.con.close()
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
			p1 = Player(" O ")
			player1 = Conexoes(con, cliente, p1, game)
			
		else:
			p2 = Player(" X ")
			player2 = Conexoes(con, cliente, p2, game)
			player1.start()
			player2.start()
			
