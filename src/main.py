# pylint: disable=no-member
import pygame
from pygame.event import clear

from board import Board
from render import renderBoard, handleEvents
from settings import x, y, MAX_FPS, RESOLUTION
import rules
import utils

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)

b = Board(x, y)
paused = True

def clickHandler(pos):
    b.write(*pos, not b.state(*pos))

def calcSim():
    if not paused:
        # Run all of the checks
        crowded = utils.crowded
        utils.boardRandom(1)

def togglepause():
    global paused
    paused = not paused

def clearBoard():
    b.clear()

while True:
    handleEvents(onclick=clickHandler, onchangepause=togglepause, onclear=clearBoard)
    calcSim()
    renderBoard(screen, b)
