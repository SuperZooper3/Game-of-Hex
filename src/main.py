# pylint: disable=no-member
import random

import pygame

from render import renderBoard
from board import Board

pygame.init()
screen = pygame.display.set_mode([1500, 1500])

x, y = 10, 3
b = Board(10, 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    renderBoard(screen, b)
    b.write(random.randint(0, x-1), random.randint(0, y-1), random.choice([True, False]))
    pygame.display.flip()