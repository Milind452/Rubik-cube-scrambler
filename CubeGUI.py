import pygame
import time
pygame.font.init()

class CubeGUI:
    faces = cube
        # colors
        white = [255, 255, 255]
        green = [0, 255, 0]
        blue = [0, 0, 255]
        orange = [255, 165, 0]
        yellow = [255, 255, 0]
        red = [255, 0, 0]

        def __init__(self, rows, cols, width, height, win):
            self.rows = rows
            self.cols = cols
            self.width = width
            self.height = height
            self.win = win
        def grid(self):
            for i in range(self.rows+1):
                if(i % 3 == 0):
                    pygame.draw.line(self.win, (0, 0, 0), (0, 0 +
                                                           i*self.width/3), (1200, i*self.width/3), 4)
                else:
                    pygame.draw.line(self.win, (0, 0, 0), (0, 0 +
                                                           i*self.width/3), (1200, i*self.width/3), 2)
            for i in range(self.cols+1):
                if(i % 3 == 0):
                    pygame.draw.line(self.win, (0, 0, 0), (0 + i *
                                                           self.width/3, 0), (0 + i*self.width/3, 900), 4)
                else:
                    pygame.draw.line(self.win, (0, 0, 0), (0 + i *
                                                           self.width/3, 0), (0 + i*self.width/3, 900), 2)
