# pylint: disable=no-member
from math import cos, sin

import pygame


# https://stackoverflow.com/questions/29064259/drawing-pentagon-hexagon-in-pygame :)
def getHexCoords(radius, position):
    pi2 = 2 * 3.14
    n = 6
    return [(cos(i / n * pi2) * radius + position[0], sin(i / n * pi2) * radius + position[1]) for i in range(0, n)] 

def main():
    pygame.init()

    screen = pygame.display.set_mode([500, 500])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        pygame.draw.polygon(screen, (255, 0, 255), getHexCoords(100, (150, 150)))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()