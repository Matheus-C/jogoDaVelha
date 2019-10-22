import pygame
import os

from grid import Grid

# Seta aonde a janela vai aparecer
os.environ['SDL_VIDEO_WINDOW_POS'] = '450,100'

# Seta o tamanho da janela
surface = pygame.display.set_mode((600,600))

# Define o título da janela
pygame.display.set_caption('Jogo da Velha - TCP')

grid = Grid()

player =  "X"
started = True

while started:
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			started = False
		if (event.type == pygame.MOUSEBUTTONDOWN and not grid.gameOver):
			# Botão esquerdo do mouse
			if (pygame.mouse.get_pressed()[0]):
				position = pygame.mouse.get_pos()

				x = position[1] // 200
				y = position[0] // 200
				grid.getSquareClick(x, y, player)
				grid.checkGame(x, y, player)

				if (grid.changePlayer):
					if (player == "X"):
						player = "O"
					else:
						player = "X"
		
		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_SPACE and grid.gameOver):
				grid.gridClear()
				grid.gameOver = False
			elif(event.key == pygame.K_ESCAPE):
				started = False
			
	# Cor do background 
	surface.fill((255,255,255))

	grid.buildGrid(surface)

	# Da "refresh" na janela
	pygame.display.flip()