import pygame 
import Cube
import Scrambler
import CubeGUI

cube = Cube()
scrambler = Scrambler()
gui = CubeGUI()

win = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Faces")
board = CubeGUI(9, 12, 300, 300, win)
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		board.draw()
		board.grid()

		pygame.display.update()


pygame.quit()