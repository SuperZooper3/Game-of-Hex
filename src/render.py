# pylint: disable=no-member, no-name-in-module
from math import cos, pi, radians, sin
import os
import platform
import sys
import pygame

from settings import *

buttons = {"pause": None, "clear": None, "step": None, "gif": None}

# Easy math to start with
def closest(lst, K):
    # print(lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))])
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


# https://stackoverflow.com/questions/29064259/drawing-pentagon-hexagon-in-pygame + math = :exploding_head:
# returns the 6 points for a regular hexagon
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


# Draws a hex from the coords `pos` (from board), takes care of converting
# into irl coords
# Also does some math
def drawHex(screen, pos, alive, age, board=None, lines=DOLINES, outl=OUTLINE):
    color = (255, 255, 255) if not alive else (0, 0, 0)
    if age is not None and alive:
        color = CELLCOLORS[closest(list(CELLCOLORS.keys()), age)]
    else:
        color = CELLCOLORS[0]

    # Every second hex needs to be slightly higher
    if pos[0] % 2 == 1:
        # Get ready for more math
        hexCoordsOffset = sin(radians(60)) * RADIUS
        coords = getHexCoords(
            RADIUS,
            (
                (pos[0] * RADIUS) * 1.5 + OFFSET,
                (pos[1] * RADIUS) * 1.7  # idk why 1.7, but oh well
                + OFFSET
                + hexCoordsOffset,
            ),
        )
    else:
        coords = getHexCoords(
            RADIUS, ((pos[0] * RADIUS) * 1.5 + OFFSET, (pos[1] * RADIUS) * 1.7 + OFFSET)
        )

    # draw the polygon filled
    if not outl:
        pygame.draw.polygon(screen, color, coords)

    if lines:
        # Draw the grid for the cells
        if not outl:
            for i in range(len(coords)):
                # Draw each side of the cell
                pygame.draw.line(
                    screen, (0, 0, 0), coords[i], coords[(i + 1) % len(coords)]
                )

        # This part draws the outline of the board
        # If the cell is dead, skip drawinng. If it is alive, go over each neighbouring cell and if it is dead then draw the edge, else do not draw
        elif alive: # This skips drawing if we are dead
            # Itterate over all of the neighboring cells
            for idx, a in enumerate(board.around(*pos)):
                # Draw the edge if it is dead
                if not a:
                    t = 4 # The neibour and draw are out of sync by 4 so this corrects that
                    pygame.draw.line(
                        screen, (0, 0, 0), coords[(idx+t)%6], coords[((idx + 1 + t)%6) % len(coords)], width=THICKNESS
                    )            



# handle click events
# propagates onclick; onchangepause; onclear; onstep
# Requires the args to be funcs
def handleEvents(
    onclick = None, onchangepause = None, onclear = None, onstep = None, ongif = None, onoutline = None
):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            onchangepause()
        elif event.type == pygame.MOUSEBUTTONUP:
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
            elif buttons["gif"].collidepoint(event.pos):
                ongif()
                return
            elif buttons["outline"].collidepoint(event.pos):
                onoutline()
                return

            eventX -= OFFSET
            eventX /= 1.5
            eventX /= RADIUS

            roundedX = round(eventX)
            if roundedX % 2 == 1:
                eventY -= RADIUS

            eventY -= OFFSET
            eventY /= 1.7
            eventY /= RADIUS

            roundedY = round(eventY)

            onclick((roundedX, roundedY))


# Render the board on the pygame screen
def renderBoard(screen, board, text = False, lines=DOLINES, outl = OUTLINE):
    clock.tick(get_maxfps(text=text))
    if text:
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(board)
        return
    renderDebug(screen)

    for cell in board:
        drawHex(screen, (cell.x, cell.y), cell.alive, cell.age, board=board, lines=lines, outl=outl)

    pygame.display.flip()


# Render debug buttons and text
def renderDebug(screen):
    screen.fill((255, 255, 255))
    fps = "FPS: " + str(int(clock.get_fps()))
    fps_text = get_fps_font().render(fps, 1, pygame.Color("black"))
    screen.blit(fps_text, (RESOLUTION[0] - 150, 20))

    buttons["pause"] = pygame.Rect(RESOLUTION[0] - 150, 75, 125, 50)
    pygame.draw.rect(screen, [42, 106, 209], buttons["pause"])
    pause_text = get_fps_font(size=14).render("Pause/Resume", 1, pygame.Color("white"))
    screen.blit(pause_text, (RESOLUTION[0] - 140, 90))

    buttons["clear"] = pygame.Rect(RESOLUTION[0] - 150, 150, 125, 50)
    pygame.draw.rect(screen, [0, 0, 0], buttons["clear"])
    clear_text = get_fps_font(size=14).render("Clear", 1, pygame.Color("white"))
    screen.blit(clear_text, (RESOLUTION[0] - 140, 165))

    buttons["step"] = pygame.Rect(RESOLUTION[0] - 150, 225, 125, 50)
    pygame.draw.rect(screen, [0, 0, 0], buttons["step"])
    step_text = get_fps_font(size=14).render("Step", 1, pygame.Color("white"))
    screen.blit(step_text, (RESOLUTION[0] - 140, 240))

    buttons["gif"] = pygame.Rect(RESOLUTION[0] - 150, 300, 125, 50)
    pygame.draw.rect(screen, [0, 0, 0], buttons["gif"])
    gif_text = get_fps_font(size=14).render("Make Gif", 1, pygame.Color("white"))
    screen.blit(gif_text, (RESOLUTION[0] - 140, 315))

    buttons["outline"] = pygame.Rect(RESOLUTION[0] - 150, 375, 125, 50)
    pygame.draw.rect(screen, [0, 0, 0], buttons["outline"])
    outline_text = get_fps_font(size=14).render("Outline SC", 1, pygame.Color("white"))
    screen.blit(outline_text, (RESOLUTION[0] - 140, 390))