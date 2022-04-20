# pylint: disable=no-member, no-name-in-module
import os
import platform
import sys
from math import cos, pi, radians, sin
from types import FunctionType, NoneType
from typing import Dict, List, Tuple, Union

import pygame

from board import Board
from settings import *

buttons: Dict[str, Optional[pygame.Rect]] = {
    "pause": None,
    "clear": None,
    "step": None,
    "gif": None,
    "outline": None,
    "SCname": None,
    "Stats": None,
}

buttonsName: Dict[str, str] = {
    "pause": "Pause/Resume",
    "clear": "Clear",
    "step": "Step",
    "gif": "GIF",
    "outline": "Outline",
    "SCname": "Name SC",
    "Stats": "Stats",
}

# idk, probably the cause of the pixel offset errors
MAGIC_NUMBER = 1.7


# Easy math to start with
def closest(lst: List[int], K: int) -> int:
    # print(lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))])
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


# https://stackoverflow.com/questions/29064259/drawing-pentagon-hexagon-in-pygame + math = :exploding_head:
# returns the 6 points for a regular hexagon
def getHexCoords(
    radius: int, position: Tuple[float, float]
) -> List[Tuple[float, float]]:
    pi2: float = 2 * pi
    n: int = 6
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
def drawHex(
    screen: pygame.surface.Surface,
    pos: Tuple[int, int],
    alive: bool,
    age: int,
    board: Board = None,
    grid: bool = DOGRID,
    outl: bool = OUTLINE,
    coloured: bool = None,
) -> None:
    color: Tuple[int, int, int] = (255, 255, 255) if not alive else (0, 0, 0)
    if age is not None and alive:
        color = CELLCOLORS[closest(list(CELLCOLORS.keys()), age)]
    else:
        color = CELLCOLORS[0]

    if board is None:
        return

    # Every second hex needs to be slightly higher
    if pos[0] % 2 == 1:
        # Get ready for more math
        hexCoordsOffset: float = sin(radians(60)) * RADIUS
        coords: List[Tuple[float, float]] = getHexCoords(
            RADIUS,
            (
                (pos[0] * RADIUS) * 1.5 + OFFSET,
                (pos[1] * RADIUS) * MAGIC_NUMBER  # idk why 1.7, but oh well
                + OFFSET
                + hexCoordsOffset,
            ),
        )
    else:
        coords = getHexCoords(
            RADIUS,
            (
                (pos[0] * RADIUS) * 1.5 + OFFSET,
                (pos[1] * RADIUS) * MAGIC_NUMBER + OFFSET,
            ),
        )

    # draw the polygon filled
    if not outl or coloured:
        pygame.draw.polygon(screen, color, coords)

    if grid:
        # Draw the grid for the cells
        if not outl:
            for i in range(len(coords)):
                # Draw each side of the cell
                pygame.draw.line(
                    screen, (0, 0, 0), coords[i], coords[(i + 1) % len(coords)]
                )

        # This part draws the outline of the board

    # Just draw the outline
    if not grid and outl and alive:  # This skips drawing if we are dead
        # Itterate over all of the neighboring cells
        # If the cell is dead, skip drawinng. If it is alive, go over each neighbouring cell and if it is dead then draw the edge, else do not draw
        for idx, a in enumerate(board.around(*pos)):
            # Draw the edge if it is dead
            if not a:
                t = 4  # The neibour and draw are out of sync by 4 so this corrects that
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    coords[(idx + t) % 6],
                    coords[((idx + 1 + t) % 6) % len(coords)],
                    width=THICKNESS,
                )

    # Draw the outline and grid
    elif grid and outl and alive:
        # Draw the oultine
        for i in range(len(coords)):
            # Draw each side of the cell one at a time
            pygame.draw.line(
                screen,
                (0, 0, 0),
                coords[i],
                coords[(i + 1) % len(coords)],
                width=THICKNESS,
            )


# Write text in the bottom left of the board
def drawText(screen: pygame.surface.Surface, text: str) -> None:
    font = pygame.font.SysFont("Comic Sans MS", 40)
    rendered_text = font.render(text, True, (0, 0, 0))
    screen.blit(rendered_text, (0, RESOLUTION[1] - 50))


# handle click events
# propagates onclick; onchangepause; onclear; onstep
# Requires the args to be funcs
def handleEvents(
    onclick: Callable[[Tuple[int, int]], None] = None,
    onchangepause: Callable[[], None] = None,
    onclear: Callable[[], None] = None,
    onstep: Callable[[], None] = None,
    ongif: Callable[[], None] = None,
    onoutline: Callable[[], None] = None,
    onnamesc: Callable[[], None] = None,
    onstats: Callable[[], None] = None,

) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_SPACE
            and onchangepause is not None
        ):
            onchangepause()
        elif event.type == pygame.MOUSEBUTTONUP:
            eventX: float = event.pos[0]
            eventY: float = event.pos[1]

            if (
                buttons["pause"] is not None
                and onchangepause is not None
                and buttons["pause"].collidepoint(event.pos)
            ):
                onchangepause()
                return
            elif (
                buttons["clear"] is not None
                and onclear is not None
                and buttons["clear"].collidepoint(event.pos)
            ):
                onclear()
                return
            elif (
                buttons["step"] is not None
                and onstep is not None
                and buttons["step"].collidepoint(event.pos)
            ):
                onstep()
                return
            elif (
                buttons["gif"] is not None
                and ongif is not None
                and buttons["gif"].collidepoint(event.pos)
            ):
                ongif()
                return
            elif (
                buttons["outline"] is not None
                and onoutline is not None
                and buttons["outline"].collidepoint(event.pos)
            ):
                onoutline()
                return
            elif (
                buttons["SCname"] is not None
                and onnamesc is not None
                and buttons["SCname"].collidepoint(event.pos)
            ):
                onnamesc()
            elif (
                buttons["Stats"] is not None
                and onnamesc is not None
                and buttons["Stats"].collidepoint(event.pos)
            ):
                onstats()
                return

            eventX -= OFFSET
            eventX /= 1.5
            eventX /= RADIUS

            roundedX = round(eventX)
            if roundedX % 2 == 1:
                eventY -= RADIUS

            eventY -= OFFSET
            eventY /= MAGIC_NUMBER
            eventY /= RADIUS

            roundedY = round(eventY)
            if onclick is not None:
                onclick((roundedX, roundedY))


# Render the board on the pygame screen
def renderBoard(
    screen: pygame.surface.Surface,
    board: Board,
    text: bool = False,
    grid: bool = DOGRID,
    outl: bool = OUTLINE,
    coloured: bool = None,
) -> None:
    clock.tick(get_maxfps(text=text))
    if text:
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(board)
        return
    renderDebug(screen)

    for cell in board:
        drawHex(
            screen,
            (cell.x, cell.y),
            cell.alive,
            cell.age,
            board=board,
            grid=grid,
            outl=outl,
            coloured=coloured,
        )

    pygame.display.flip()


# Render debug buttons and text
def renderDebug(screen: pygame.surface.Surface) -> None:
    screen.fill((255, 255, 255))
    fps: str = "FPS: " + str(int(clock.get_fps()))
    fps_text: pygame.surface.Surface = get_fps_font().render(
        fps, True, pygame.Color("black")
    )
    screen.blit(fps_text, (RESOLUTION[0] - 150, 20))

    paintButtons(screen)


def paintButtons(screen: pygame.surface.Surface) -> None:
    for idx, name in enumerate(buttons):
        buttons[name] = pygame.Rect(RESOLUTION[0] - 150, 75 + (75 * idx), 125, 50)
        button_rect = buttons[name]

        if button_rect is not None:
            pygame.draw.rect(screen, [0, 0, 0], button_rect)

        outline_text: pygame.surface.Surface = get_fps_font(size=14).render(
            buttonsName[name], True, pygame.Color("white")
        )
        screen.blit(outline_text, (RESOLUTION[0] - 140, 90 + (75 * idx)))
