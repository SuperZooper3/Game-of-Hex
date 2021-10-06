# pylint: disable=no-member, no-name-in-module
from math import cos, pi, radians, sin
import sys
import pygame

from settings import RADIUS, OFFSET, get_fps_font, clock, RESOLUTION, MAX_FPS

buttons = {
    "pause": None,
    "clear": None,
    "step": None
}

# https://stackoverflow.com/questions/29064259/drawing-pentagon-hexagon-in-pygame + math = :exploding_head:
def getHexCoords(radius, position):
    pi2 = 2 * pi
    n = 6
    return [
        (
            cos(i / n * pi2) * radius + position[0],
            sin(i / n * pi2) * radius + position[1],
        )
        for i in range(0, n)
    ]


def drawHex(screen, pos, alive):
    color = (255, 255, 255) if not alive else (0, 0, 0)
    # Every second hex needs to be slightly higher
    if pos[0] % 2 == 1:
        # Get ready for more math
        hexCoordsOffset = sin(radians(60)) * RADIUS
        coords = getHexCoords(
            RADIUS,
            (
                (pos[0] * RADIUS) * 1.5 + OFFSET,
                (pos[1] * RADIUS) * 1.7 + OFFSET + hexCoordsOffset,
            ),
        )
    else:
        coords = getHexCoords(
            RADIUS, ((pos[0] * RADIUS) * 1.5 + OFFSET, (pos[1] * RADIUS) * 1.7 + OFFSET)
        )

    pygame.draw.polygon(screen, color, coords)
    for i in range(len(coords)):
        pygame.draw.line(screen, (0, 0, 0), coords[i], coords[(i + 1) % len(coords)])


def handleEvents(onclick=None, onchangepause=None, onclear=None, onstep=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            onchangepause()
        elif event.type == pygame.MOUSEBUTTONUP:
            # Guess what: even more sketchy math :)
            # obv this isn't correct cause of hexCoordsOffset
            # but it works well enough if you click on the top of the hex
            eventX = event.pos[0]
            eventY = event.pos[1]

            if buttons["pause"].collidepoint(event.pos):
                onchangepause()
                return
            elif buttons["clear"].collidepoint(event.pos):
                onclear()
                return
            elif buttons["step"].collidepoint(event.pos):
                onstep()
                return


            eventX -= OFFSET
            eventX /= 1.5
            eventX /= RADIUS


            roundedX = round(eventX)
            if roundedX % 2 == 1:
                eventY -= RADIUS
                print(eventY)
    
            eventY -= OFFSET
            eventY /= 1.7
            eventY /= RADIUS

            
            roundedY = round(eventY)

            onclick((roundedX, roundedY))


def renderBoard(screen, board):
    renderDebug(screen)

    for x, valy in enumerate(board.grid):
        for y, alive in enumerate(valy):
            drawHex(screen, (x, y), alive)

    clock.tick(MAX_FPS)
    pygame.display.flip()


def renderDebug(screen):
    screen.fill((255, 255, 255))
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_text = get_fps_font().render(fps, 1, pygame.Color("black"))
    screen.blit(fps_text, (RESOLUTION[0] - 150, 20))

    pause_text = get_fps_font(size=14).render("Pause/Resume", 1, pygame.Color("white"))
    buttons["pause"] = pygame.Rect(RESOLUTION[0] - 150, 75, 125, 50)
    pygame.draw.rect(screen, [42, 106, 209], buttons["pause"])
    screen.blit(pause_text, (RESOLUTION[0] - 140, 90))

    clear_text = get_fps_font(size=14).render("Clear", 1, pygame.Color("white"))
    buttons["clear"] = pygame.Rect(RESOLUTION[0] - 150, 150, 125, 50)
    pygame.draw.rect(screen, [0, 0, 0], buttons["clear"])
    screen.blit(clear_text, (RESOLUTION[0] - 140, 165))

    step_text = get_fps_font(size=14).render("Step", 1, pygame.Color("white"))
    buttons["step"] = pygame.Rect(RESOLUTION[0] - 150, 225, 125, 50)
    pygame.draw.rect(screen, [0, 0, 0], buttons["step"])
    screen.blit(step_text, (RESOLUTION[0] - 140, 240))




def main():
    from board import Board

    pygame.init()

    screen = pygame.display.set_mode([1500, 1500])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        b = Board(3, 7)
        renderBoard(screen, b)

        # drawHex(screen, (0, 0), False)
        # drawHex(screen, (1, 0), False)
        # drawHex(screen, (2, 0), False)
        # drawHex(screen, (3, 0), False)
        # drawHex(screen, (4, 0), False)

        # drawHex(screen, (0, 1), False)
        # drawHex(screen, (1, 1), False)
        # drawHex(screen, (2, 1), False)
        # drawHex(screen, (3, 1), False)
        # drawHex(screen, (4, 1), False)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
