import Player
import Jogo
#classes importadas
import socket

HOST = '127.0.0.1'
PORT = 6854
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('Para desistir digite 0\n')
#o jogo ficará em loop até alguém ganhar/desistir
while True:
	recvMsg = tcp.recv(1024)
	print(recvMsg.decode())
	recvMsg = tcp.recv(1024)
	print(recvMsg.decode())
	comando = input()
	#envia o comando  para o servidor 
	tcp.send(comando.encode())
	#indica que é a vez do oponente e espera que o oponente faça sua jogada e mostra o tabuleiro
	recvMsg = tcp.recv(1024)
	print(recvMsg.decode())
#recebe e imprime a mensagem mostrando quem ganhou
print("O jogo acabou")
recvMsg = tcp.recv(1024)
print(recvMsg.decode())
tcp.close()