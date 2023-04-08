import sys
import pygame as pg
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from simulation import Simulation

pg.init()

# Colores
BLACK = (0, 0, 0)
GRAY = (65, 65, 65)
WHITE = (255, 255, 255)
PINK = (255, 207, 224)
LBLUE = (135, 206, 235)

# Inicialización de la ventana
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Falling Sand')

# Variables
clock = pg.time.Clock()
run = False

simulation = Simulation(screen)
mouse_is_clicked = False

# Bucle principal
while not run:
    # Manejo de eventos del juego
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = True

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_is_clicked = True

        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            mouse_is_clicked = False

    screen.fill(GRAY)
    # Code
    simulation.update()

    if mouse_is_clicked:
        mouse_pos = pg.mouse.get_pos()
        simulation.add_sand(mouse_pos)


    pg.display.flip()
    clock.tick(FPS)

# Cierre del bucle
pg.quit()
sys.exit()
