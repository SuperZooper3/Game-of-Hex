# pylint: disable=no-member
import random

import pygame

from board import Board
from render import renderBoard, handleEvents
from settings import x, y, MAX_FPS, RESOLUTION

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)

b = Board(x, y)
paused = True

def clickHandler(pos):
    b.write(*pos, not b.state(*pos))

def calcSim():
    if not paused:
        # Make all changes to board here
        # rn its sets a random hex to a random state
        b.write(
            random.randint(0, x - 1), random.randint(0, y - 1), random.choice([True, False])
        )

def togglepause():
    global paused
    paused = not paused


while True:
    handleEvents(onclick=clickHandler, onchangepause=togglepause)
    calcSim()
    renderBoard(screen, b)
