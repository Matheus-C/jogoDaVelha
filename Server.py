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
				if data.decode() == "close":
					con.close()
					lock.release()
					break
				lock.release()
				time.sleep(0.1)
			else:
				data = q.get()
				print(data.decode() + self.name)
				self.con.send(data)
				if data.decode() == "close":
					con.close()
					lock.release()
					break
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
q = Queue()
# loop para conectar os jogadores max 2 jogadores
for i in range(1, 3):
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
