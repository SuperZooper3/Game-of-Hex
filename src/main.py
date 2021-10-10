# pylint: disable=no-member
import argparse
from copy import deepcopy

import datetime
import gif
import rules
import utils
from board import Board
from render import handleEvents, renderBoard
from settings import *

paused = not text

b1 = Board.genAlive(
    startCells, x, y
)  # This is the board that we will be displaying to the user
b2 = Board(
    x, y
)  # This is the board to which we will write the next step's board, which will then be transfered to b1 and cleared

# Get rid of all of the gifs until now
gif.clearImg()

if not text:
    import pygame

    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
else:
    screen = None

# Simulate a step of the board
def simStep(stepping=False):
    global b1, b2
    if not paused or stepping:
        # b2.clear() # Clear the current board Note: **we dont need to do this caus all of the cells are gona be overwitten anyways**
        # Itterate over all of the cells
        for cell in b1:
            cx = cell.x
            cy = cell.y
            cs = cell.state
            ca = cell.age

            # Compute all the rules
            freeze = rules.freeze(b1, cx, cy)

            # Combine all the rules (for now simple because we don't have many rules)
            nextstate = freeze
            if nextstate == True:
                ca = ca + 1 if ca is not None else 1
            else:
                ca = None

            # Write to the b2
            b2.write(cx, cy, nextstate, ca)

        # Copy b2 to b1
        b1 = deepcopy(b2)
        # Take a screenshot of the board for a gif
        if not text:
            gif.screenshot(screen)


def clickHandler(pos):
    b1.write(*pos, not b1.state(*pos), age=None if b1.state(*pos) else 1)


def togglepause():
    global paused
    paused = not paused


def clearBoard():
    gif.clearImg()
    global paused
    paused = True
    b1.clear()
    b2.clear()


def step():
    simStep(stepping=True)
    renderBoard(screen, b1)

def outlineSC():
    # Draw the screen
    renderBoard(screen, b1, lines=True, outl=True)
    # Take the shot
    gif.screenshot(screen, path="outline"+str(round(datetime.datetime.now().timestamp() * 10))[4:])
    # Draw the board again
    renderBoard(screen, b1)

while True:
    if not text:
        handleEvents(
            onclick=clickHandler,
            onchangepause=togglepause,
            onclear=clearBoard,
            onstep=step,
            ongif=gif.compileGif,
            onoutline=outlineSC,
        )
    simStep()
    renderBoard(screen, b1, text=text)
