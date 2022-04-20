# pylint: disable=no-member
import argparse
import datetime
import sys
from copy import deepcopy
from typing import Tuple

import gif
import rules
import utils
from board import Board
from exceptions import OutOfBoundsError
from render import drawText, handleEvents, renderBoard
from settings import *

print("---Game of Hex: starting!---")
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
    screen: pygame.surface.Surface = pygame.display.set_mode(RESOLUTION)

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
            nextstate: Optional[bool] = cs

            # Compute all the rules
            freeze: Optional[bool] = FREEZERULE(b1, cx, cy)

            # Combine all the rules (for now simple because we don't have many rules)
            nextstate = freeze
            if nextstate == True:
                ca = ca + 1 if ca is not None else 1

            # Write to the b2
            b2.write(cx, cy, nextstate, age=ca if nextstate else None)

        # Copy b2 to b1
        b1 = deepcopy(b2)
        # Take a screenshot of the board for a gif
        if not text:
            gif.screenshot(screen)


def clickHandler(pos: Tuple[int, int]) -> None:
    try:
        b1.write(*pos, not b1.alive(*pos), age=None if b1.alive(*pos) else 1)
    except OutOfBoundsError:
        pass


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

def stats() -> None:
    # run stats function
    print("Stats!")
    return


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


def onnameSC() -> None:
    name = str(input("Name: "))
    renderBoard(screen, b1, grid=True, outl=True, coloured=True)
    drawText(screen, name)
    gif.screenshot(screen, path="img/name/" + name)
    renderBoard(screen, b1)


while True:
    try:
        if not text:
            handleEvents(
                onclick=clickHandler,
                onchangepause=togglepause,
                onclear=clearBoard,
                onstep=step,
                ongif=gif.compileGif,
                onoutline=outlineSC,
                onnamesc=onnameSC,
                onstats=stats
            )
        simStep()
        renderBoard(screen, b1, text=text)
    except KeyboardInterrupt:
        print("---Game of Hex: exiting---")
        sys.exit(0)
