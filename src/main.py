# pylint: disable=no-member
import argparse
from copy import deepcopy

import datetime
from typing import Tuple
import gif
import rules
import utils
from board import Board
from render import handleEvents, renderBoard
from settings import *

print("---Game of Hex, starting!---")
paused: bool = not text

b1: Board = Board.genAlive(
    startCells, x, y
)  # This is the board that we will be displaying to the user
b2: Board = Board(
    x, y
)  # This is the board to which we will write the next step's board, which will then be transfered to b1 and cleared

# Get rid of all of the gifs until now
gif.clearImg()

if not text:
    import pygame

    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(RESOLUTION)
else:
    screen = None

# Simulate a step of the board
def simStep(stepping: bool = False) -> None:
    global b1, b2
    if not paused or stepping:
        # b2.clear() # Clear the current board Note: **we dont need to do this caus all of the cells are gona be overwitten anyways**
        # Itterate over all of the cells
        for cell in b1:
            cx: int = cell.x
            cy: int = cell.y
            cs: bool = cell.alive
            ca: int = cell.age
            nextstate: bool = cs

            # Compute all the rules
            freeze: bool = FREEZERULE(b1, cx, cy)

            # Combine all the rules (for now simple because we don't have many rules)
            nextstate: bool = freeze
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


def clickHandler(pos: Tuple[int]) -> None:
    b1.write(*pos, not b1.alive(*pos), age=None if b1.alive(*pos) else 1)


def togglepause() -> None:
    global paused
    paused = not paused


def clearBoard() -> None:
    gif.clearImg()
    global paused
    paused = True
    b1.clear()
    b2.clear()


def step() -> None:
    simStep(stepping=True)
    renderBoard(screen, b1)


def outlineSC() -> None:
    t: str = str(round(datetime.datetime.now().timestamp() * 10))[3:]

    # DRAW THE JUST OUTLINE
    renderBoard(screen, b1, grid=False, outl=True)

    # Take the shot
    gif.screenshot(screen, path="img/outline/outline" + t)

    # DRAW THE OUTLINE WITH HEXAGONS FOR ALIVE CELLS
    renderBoard(screen, b1, grid=True, outl=True)
    # Take the shot
    gif.screenshot(screen, path="img/outline/outlineGrid" + t)
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
