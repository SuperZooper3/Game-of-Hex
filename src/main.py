# pylint: disable=no-member
import random

import pygame

from board import Board
from render import renderBoard
from settings import x, y, MAX_FPS, RESOLUTION

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
font = pygame.font.SysFont("verdana", 32)

b = Board(x, y)

running = True
while running:
    # Useless but needed, also debug stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("black"))
    screen.blit(fps_text, (RESOLUTION[0] - 150, 20))

    renderBoard(screen, b)
    b.write(
        random.randint(0, x - 1), random.randint(0, y - 1), random.choice([True, False])
    )

    # Update screen
    pygame.display.flip()
    clock.tick(MAX_FPS)
