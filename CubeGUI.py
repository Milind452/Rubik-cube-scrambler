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
