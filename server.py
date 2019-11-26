from Player import Player
import socket, threading, time
from queue import Queue

turn = 1

# thread para conexoes simultaneas
class Conexoes(threading.Thread):
	def __init__(self, connection, player):
		threading.Thread.__init__(self)
		self.connection = connection
		self.player = player

	def run(self):
		global turn
		while True:
			lock.acquire()
			print(self.name)
			if turn == self.player.getTurn():
				data = self.connection.recv(1024)
				print(data.decode() + self.name)
				q.put(data)
				if data.decode() == "close":
					connection.close()
					lock.release()
					break
				lock.release()
				time.sleep(0.1)
			else:
				data = q.get()
				print(data.decode() + self.name)
				self.connection.send(data)
				if data.decode() == "close":
					connection.close()
					lock.release()
					break
				if turn == 1:
					turn = 2
				else:
					turn = 1
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
	connection, client = tcp.accept()
	print('Conectado por', client)
	if i == 1:
		p1 = Player("X", i)
		player1 = Conexoes(connection, p1)
		connection.send(p1.getSymbol().encode())
	elif i == 2:
		p2 = Player("O", i)
		player2 = Conexoes(connection, p2)
		connection.send(p2.getSymbol().encode())
		player1.start()
		player2.start()
