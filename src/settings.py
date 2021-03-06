import argparse
import json
from collections import OrderedDict
from types import FunctionType
from typing import Callable, Dict, List, Optional, Tuple

import pygame

from board import Board
from rules import eternalFreeze, freeze

parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description="Run the game of life using hexagonal grids"
)

scaling = 0.2

parser.add_argument("-x", type=int, default=int(190*scaling), help="Width of the grid")
parser.add_argument("-y", type=int, default=int(130*scaling), help="Height of the grid")
parser.add_argument(
    "-f", "--maxfps", type=int, dest="maxfps", help="Maximum frames per seconds"
)
parser.add_argument("-r", "--radius", type=int, default=int(3/scaling), help="Radius of the hexes")
parser.add_argument(
    "-o", "--outline", action="store_true", help="Only display hex outlines"
)
parser.add_argument(
    "-t", "--thickness", type=int, default=1, help="Only display hex outlines"
)
parser.add_argument("--text", action="store_true", help="Use a text UI")
parser.add_argument("-g", "--grid", action="store_true", help="Draw hexagon grid")
parser.add_argument(
    "--resolution",
    nargs=2,
    default=(1050, 700),
    type=int,
    help="Resolution of the window to open",
)
parser.add_argument(
    "-p", "--previous", action="store_true", help="Use previous settings"
)
parser.add_argument(
    "-d", "--candie", action="store_true", help="Changes the rule so that cells can die"
)
args = parser.parse_args()
text: bool = args.text

# Width and height, respectively
x, y = args.x, args.y

# Max frames per seconds
def get_maxfps(text: bool = False) -> int:
    if args.maxfps is None:
        return 30 if not text else 2
    else:
        return args.maxfps


# If to draw the outline of teh cells instead of the colour
OUTLINE: bool = args.outline

# Size of the window opened
RESOLUTION: Tuple[int, ...] = tuple(args.resolution)

# How many times to divide the size of the gif (not that important so I have 1)
GIFCOMPRESSION: int = 1

# Image cropping x:
CROPPING: int = 150

# Thickness of the outline drawing
THICKNESS: int = args.thickness

# Set the colours depending on the ages

BGCOLOR: Tuple[int, int, int, int] = (
    (186, 186, 186, 255) if not OUTLINE else (0, 0, 0, 0)
)

CELLCOLORS: OrderedDict = OrderedDict()
CELLCOLORS[0] = BGCOLOR
CELLCOLORS[1] = (31, 143, 132)
CELLCOLORS[3] = (17, 163, 173)
CELLCOLORS[5] = (20, 173, 196)
CELLCOLORS[7] = (33, 171, 217)
CELLCOLORS[10] = (49, 143, 232)
CELLCOLORS[15] = (37, 99, 207)
CELLCOLORS[20] = (17, 59, 133)
CELLCOLORS[25] = (40, 77, 143)
CELLCOLORS[30] = (89, 122, 181)
CELLCOLORS[40] = (150, 172, 212)
CELLCOLORS[50] = (218, 226, 240)
CELLCOLORS[float("inf")] = (255, 255, 255)

# A greyscale colour pallet for laser engraving
# CELLCOLORS = OrderedDict()
# CELLCOLORS[0] = (255, 255, 255)
# CELLCOLORS[1] = (240, 240, 240)
# CELLCOLORS[3] = (210, 210, 210)
# CELLCOLORS[5] = (180, 180, 180)
# CELLCOLORS[10] = (150, 150, 150)
# CELLCOLORS[20] = (120, 120, 120)
# CELLCOLORS[30] = (90, 90, 90)
# CELLCOLORS[40] = (60, 60, 60)
# CELLCOLORS[50] = (30, 30, 30)
# CELLCOLORS[float("inf")] = (0, 0, 0)

# Radius of the hexes
RADIUS: int = args.radius

# Padding around the top and left edges
OFFSET: float = RADIUS * 1.8

# If to draw the heaxagonal lines
DOGRID: bool = args.grid

# Number of seconds per frame of the gif
GIFSPEED: float = 0.4


# Rule for cell freezing
FREEZERULE: Callable[[Board, int, int], Optional[bool]] = (
    freeze if args.candie else eternalFreeze
)

# Game clock
clock: pygame.time.Clock = pygame.time.Clock()

# Cells to be there at start (list of tuples)
# [(x, y), (x, y), ...]
startCells: List[Tuple[int, int]] = []

# Font for the fps counter
# Function becuase pygame needs to be initialized before calling font methods
def get_fps_font(size: int = 32) -> pygame.font.Font:
    return pygame.font.SysFont("verdana", size)


if args.previous:
    with open("settings.json", "r", encoding="UTF-8") as f:
        previous: Dict = json.load(f)
        x = previous["x"]
        y = previous["y"]
        maxfps = previous["maxfps"]
        RADIUS = previous["radius"]
        text = previous["text"]
        DOGRID = previous["grid"]
        RESOLUTION = tuple(previous["resolution"])
        OUTLINE = previous["outline"]
        if previous["candie"]:
            FREEZERULE = freeze
        else:
            FREEZERULE = eternalFreeze

with open("settings.json", "w+", encoding="UTF-8") as f:
    json.dump(
        {
            "x": x,
            "y": y,
            "maxfps": args.maxfps,
            "radius": RADIUS,
            "text": text,
            "grid": DOGRID,
            "resolution": RESOLUTION,
            "outline": OUTLINE,
            "candie": args.candie,
        },
        f,
    )
