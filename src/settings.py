import pygame
from collections import OrderedDict

# Width and height, respectively
x, y = 24, 24

# Max frames per seconds
def get_maxfps(text=False):
    return 30 if not text else 2


# Size of the window opened
RESOLUTION = (1000, 700)

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
RADIUS = 15

# Padding around the top and left edges
OFFSET = RADIUS * 1.8

# If to draw the heaxagonal lines
DOLINES = True

# Game clock
clock = pygame.time.Clock()

# Cells to be there at start
startCells = [[20, 20]]

# Font for the fps counter
# Function becuase pygame needs to be initialized before calling font methods
def get_fps_font(size=32):
    return pygame.font.SysFont("verdana", size)
