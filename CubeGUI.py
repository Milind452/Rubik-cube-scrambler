import pygame
pygame.font.init()


class CubeGUI:
    # colors
    white = [255, 255, 255]
    green = [0, 255, 0]
    blue = [0, 0, 255]
    orange = [255, 165, 0]
    yellow = [255, 255, 0]
    red = [255, 0, 0]

    def __init__(self, rows, cols, width, height, win, cube):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.win = win
        self.faces = cube

    def grid(self):
        """
        Draw the grid
        """

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

    def drawFace(self, face, gap):
        """
        Draw one square of the cube
        @param face - represents a face of the cube
        @param gap - coordinate iterator
        """

        x = 1
        y = 0
        if(face == 0):
            x = 1
            y = 0
        elif(face == 5):
            x = 1
            y = 400
        else:
            x = face - 1
            y = 200

        for i in range(0, 3):
            for j in range(0, 3):
                if(self.faces[face][i][j] == 'w'):
                    pygame.draw.rect(self.win, self.white, [
                        j*gap+200*x,  i*gap+y, self.width/3, self.height/3])

                if(self.faces[face][i][j] == 'g'):
                    pygame.draw.rect(self.win, self.green, [
                        j*gap+200*x,  i*gap+y, self.width/3, self.height/3])

                if(self.faces[face][i][j] == 'b'):
                    pygame.draw.rect(self.win, self.blue, [
                        j*gap+200*x,  i*gap+y, self.width/3, self.height/3])

                if(self.faces[face][i][j] == 'o'):
                    pygame.draw.rect(self.win, self.orange, [
                        j*gap+200*x,  i*gap+y, self.width/3, self.height/3])

                if(self.faces[face][i][j] == 'r'):
                    pygame.draw.rect(self.win, self.red, [
                        j*gap+200*x,  i*gap+y, self.width/3, self.height/3])

                if(self.faces[face][i][j] == 'y'):
                    pygame.draw.rect(self.win, self.yellow, [
                        j*gap+200*x,  i*gap+y, self.width/3, self.height/3])

    def draw(self):
        """
        Draw the cube
        """

        self.win.fill((0, 0, 0))
        gap = self.width/3
        for face in range(len(self.faces)):
            self.drawFace(face, gap)
