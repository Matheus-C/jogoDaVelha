from grid import Grid

import socket, select
import pygame
import os

# Seta aonde a janela vai aparecer
os.environ['SDL_VIDEO_WINDOW_POS'] = '450,100'

# Seta o tamanho da janela
surface = pygame.display.set_mode((600,600))

# Define o título da janela
pygame.display.set_caption('Jogo da Velha - TCP')

grid = Grid()

HOST = '127.0.0.1'
PORT = 6854
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
tcp.settimeout(None)
player = tcp.recv(1024).decode()

started = True

if player == 'X':
	yourTurn = True
else:
	yourTurn = False

while started:
	for event in pygame.event.get():
		
		if (event.type == pygame.QUIT):
			started = False

		if (event.type == pygame.MOUSEBUTTONDOWN and not grid.gameOver):
			# Botão esquerdo do mouse
			if (pygame.mouse.get_pressed()[0] and yourTurn):
				position = pygame.mouse.get_pos()

				x = position[1] // 200
				y = position[0] // 200

				valid = grid.getSquareClick(x, y, player)
				if valid:
					sendData = str(x) + '-' + str(y) + '-' + player
					tcp.send(sendData.encode())
					grid.checkGame(x, y, player)
					yourTurn = False
				
		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_SPACE and grid.gameOver and yourTurn):
				grid.gridClear()
				grid.gameOver = False
				tcp.send("reset".encode())
				yourTurn = False
			elif(event.key == pygame.K_ESCAPE and yourTurn):
				started = False
				tcp.send("close".encode())

	# Cor do background 
	surface.fill((255,255,255))

	grid.buildGrid(surface)

	# Da "refresh" na janela
	pygame.display.flip()

	# detecta se há mensagens no buffer
	r, w, e = select.select((tcp,), (), (), 0)
	# se há mensagens no buffer processa elas
	if r:
		rcvMsg = tcp.recv(1024).decode()
		if rcvMsg == "reset":
			grid.gridClear()
			grid.gameOver = False
			yourTurn = True
		elif rcvMsg == "close":
			started = False
			tcp.close()
		else:
			print(rcvMsg)
			rcvMsg = rcvMsg.split('-')
			grid.getSquareClick(int(rcvMsg[0]), int(rcvMsg[1]), rcvMsg[2])
			grid.checkGame(int(rcvMsg[0]), int(rcvMsg[1]), rcvMsg[2])
			yourTurn = True
