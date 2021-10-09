import argparse
from collections import OrderedDict
import json

import pygame

parser = argparse.ArgumentParser(
    description="Run the game of life using hexagonal grids"
)
parser.add_argument("-x", type=int, default=190, help="Width of the grid")
parser.add_argument("-y", type=int, default=135, help="Height of the grid")
parser.add_argument(
    "-f", "--maxfps", type=int, dest="maxfps", help="Maximum frames per seconds"
)
parser.add_argument("-r", "--radius", type=int, default=3, help="Radius of the hexes")
parser.add_argument("--text", action="store_true", help="Use a text UI")
parser.add_argument("-l", "--lines", action="store_true", help="Draw hexagon outine")
parser.add_argument(
    "--resolution",
    nargs=2,
    default=(1000, 700),
    type=int,
    help="Resolution of the window to open",
)
parser.add_argument("-p", "--previous", action="store_true", help="Use previous settings")
args = parser.parse_args()
text = args.text

# Width and height, respectively
x, y = args.x, args.y

# Max frames per seconds
def get_maxfps(text=False):
    if args.maxfps is None:
        return 30 if not text else 2
    else:
        return args.maxfps


# Size of the window opened
RESOLUTION = tuple(args.resolution)

# How many times to divide the size of the gif (not that important so I have 1)
GIFCOMPRESSION = 2

# Set the colours depending on the ages
BGCOLOR = (186, 186, 186)

CELLCOLORS = OrderedDict()
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

# Radius of the hexes
RADIUS = args.radius

# Padding around the top and left edges
OFFSET = RADIUS * 1.8

# If to draw the heaxagonal lines
DOLINES = args.lines

# Number of seconds per frame of the gif
GIFSPEED = 0.4

# Game clock
clock = pygame.time.Clock()

# Cells to be there at start
startCells = []

# Font for the fps counter
# Function becuase pygame needs to be initialized before calling font methods
def get_fps_font(size=32):
    return pygame.font.SysFont("verdana", size)


if args.previous:
    with open("settings.json", "r", encoding="UTF-8") as f:
        previous = json.load(f)
        x = previous["x"]
        y = previous["y"]
        maxfps = previous["maxfps"]
        RADIUS = previous["radius"]
        text = previous["text"]
        DOLINES = previous["lines"]
        RESOLUTION = tuple(previous["resolution"])

with open("settings.json", "w+", encoding="UTF-8") as f:
    json.dump({
        "x": x,
        "y": y,
        "maxfps": args.maxfps,
        "radius": RADIUS,
        "text": text,
        "lines": DOLINES,
        "resolution": RESOLUTION
    }, f)
