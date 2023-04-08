import pygame as pg
import numpy as np
from random import randint
from config import *

# colors
SAND_COLOR = (194, 189, 128)

class Simulation:
    def __init__(self, screen):
        self.screen = screen

        self.cell_width = SCREEN_WIDTH / COLUMNS
        self.cell_height = SCREEN_HEIGHT / ROWS

        self.matrix = np.zeros((ROWS, COLUMNS))

        self.drop = True

    def update(self):
        new_matrix = self.matrix.copy()
        # iteracion de celdas
        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                # draw
                if not cell: continue
                rect = pg.Rect(
                    self.cell_width * j,
                    self.cell_height * i,
                    self.cell_width,
                    self.cell_height)
                pg.draw.rect(self.screen, SAND_COLOR, rect)

                # apply rules
                if i < ROWS - 1:
                    if not self.matrix[i+1,j]:
                        new_matrix[i+1,j] = True
                        new_matrix[i, j] = False
                    elif j > 0 and j < COLUMNS - 1:
                        if not new_matrix[i+1,j-1] and not new_matrix[i+1,j+1]:
                            if randint(0, 1):
                                new_matrix[i,j-1] = True
                            else:
                                new_matrix[i,j+1] = True
                            new_matrix[i, j] = False
                        elif not new_matrix[i+1,j-1]:
                            new_matrix[i,j-1] = True
                            new_matrix[i, j] = False
                        elif not new_matrix[i+1,j+1]:
                            new_matrix[i,j+1] = True
                            new_matrix[i, j] = False
                    elif j == 0:
                        if not new_matrix[i+1,j+1]:
                            new_matrix[i,j+1] = True
                            new_matrix[i, j] = False
                    elif j == COLUMNS - 1:
                        if not new_matrix[i+1,j-1]:
                            new_matrix[i,j-1] = True
                            new_matrix[i, j] = False

        self.matrix = new_matrix

    def add_sand(self, mouse_pos):
        if self.drop:
            x = int(mouse_pos[0] // self.cell_width)
            y = int(mouse_pos[1] // self.cell_height)
            self.matrix[y, x] = 1
            self.drop = False
        else: self.drop = True
