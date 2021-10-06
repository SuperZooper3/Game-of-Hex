# pylint: disable=no-member
import pygame
from copy import deepcopy
from pygame.event import clear

from board import Board
from render import renderBoard, handleEvents
from settings import x, y, MAX_FPS, RESOLUTION
import rules
import utils

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)

b1 = Board(x, y) # This is the board that we will be displaying to the user
b2 = Board(x, y) # This is the board to which we will write the next step's board, which will then be transfered to b1 and cleared
paused = True

# Simulate a step of the board
def simStep(stepping=False):
    global b1, b2
    if not paused or stepping:
        #b2.clear() # Clear the current board Note: **we dont need to do this caus all of the cells are gona be overwitten anyways**
        # Itterate over all of the cells
        for cell in b1:
            cx = cell["x"]
            cy = cell["y"]
            cs = cell["state"]

            # Compute all the rules
            freeze = rules.freeze(b1, cx, cy)

            # Combine all the rules (for now simple because we don't have many rules)
            nextstate = freeze

            # Write to the b2
            b2.write(cx, cy, nextstate)

        # Copy b2 to b1
        b1 = deepcopy(b2)

def clickHandler(pos):
    b1.write(*pos, not b1.state(*pos))

def togglepause():
    global paused
    paused = not paused

def clearBoard():
    b1.clear()

def step():
    simStep(stepping=True)
    renderBoard(screen, b1)

while True:
    handleEvents(onclick=clickHandler, onchangepause=togglepause, onclear=clearBoard, onstep=step)
    simStep()
    renderBoard(screen, b1)
