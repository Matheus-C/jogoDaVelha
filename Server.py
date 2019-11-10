from Player import Player
import socket, threading, time
from queue import Queue

contRodada = 1

# thread para conexoes simultaneas
class Conexoes(threading.Thread):
	"""Construtor de Conexoes parâmetros: con = conexao, p = objeto Player, game = objeto Jogo"""
	def __init__(self, con, p):
		threading.Thread.__init__(self)
		self.con = con
		self.p = p

	def run(self):
		global contRodada
		while True:
			lock.acquire()
			print(self.name)
			if contRodada == self.p.getN():
				data = self.con.recv(1024)
				print(data.decode() + self.name)
				q.put(data)
				lock.release()
				time.sleep(0.1)
			else:
				data = q.get()
				print(data.decode() + self.name)
				self.con.send(data)
				if contRodada == 1:
					contRodada = 2
				else:
					contRodada = 1
				lock.release()
				

lock = threading.Lock()
HOST = ""
PORT = 6854
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
i = 1#identificador do player
q = Queue()

while True:
	if i >= 3:
		i = 1
	tcp.listen(1)
	con, cliente = tcp.accept()
	print('Conectado por', cliente)
	if i == 1:
		p1 = Player("O", i)
		player1 = Conexoes(con, p1)
		con.send(p1.getSimb().encode())
	elif i == 2:
		p2 = Player("X", i)
		player2 = Conexoes(con, p2)
		con.send(p2.getSimb().encode())
		player1.start()
		player2.start()
	i += 1
