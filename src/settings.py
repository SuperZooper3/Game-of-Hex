import argparse
from collections import OrderedDict

import pygame

parser = argparse.ArgumentParser(description='Run the game of life using hexagonal grids')
parser.add_argument('-x', type=int, default=120, help='Width of the grid')
parser.add_argument('-y', type=int, default=120, help='Height of the grid')
parser.add_argument('-f', '--maxfps', dest="maxfps", type=int, help='Maximum frames per seconds')
parser.add_argument('--text', action='store_true', help='Use a text UI')
parser.add_argument('--resolution', nargs=2, default=(1000, 700), type=int, help='Resolution of the window to open')
args = parser.parse_args()
text = args.text
print(args)

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
RADIUS = 3

# Padding around the top and left edges
OFFSET = RADIUS * 1.8

# If to draw the heaxagonal lines
DOLINES = False

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
