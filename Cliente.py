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
while Jogo.getStatus():
	comando = input()
	#caso o jogador desista, manda uma mensagem para o servidor para terminar o jogo
	if comando == 0:
		Player.surrender()
		break
	#envia o comando  para o servidor e monstra o tabuleiro
	tcp.send(comando.encode())
	recvMsg = tcp.recv(1024)
	print(recvMsg.decode())
	#indica que é a vez do oponente e espera que o oponente faça sua jogada e mostra o tabuleiro
	print("vez do oponente")
	recvMsg = tcp.recv(1024)
	print(recvMsg.decode())
	print("sua vez")
#recebe e imprime a mensagem mostrando quem ganhou
print("O jogo acabou")
recvMsg = tcp.recv(1024)
print(recvMsg.decode())
tcp.close()