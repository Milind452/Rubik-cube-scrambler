import pygame 
from Cube import *
from Scrambler import *
from CubeGUI import *

cube = Cube()
scrambler = Scrambler()
scramble = scrambler.generateScramble(cube.faces, cube.turns)
scrambler.Scrambler(scramble, cube)

# scrambler.showScramble(scramble)
# cube.showCube()

# win = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Faces")
# gui = CubeGUI(9, 12, 200, 200, win, cube.cube)
# run = True
# while run:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			run = False
# 		gui.draw()
# 		gui.grid()

# 		pygame.display.update()

# pygame.quit()