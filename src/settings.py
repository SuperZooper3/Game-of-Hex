import pygame

# Width and height, respectively
x, y = 120, 100

# Max frames per seconds
def get_maxfps(text=False):
    return 60 if not text else 2

# Size of the window opened
RESOLUTION = (1280, 1000)

# Radius of the hexes
RADIUS = 5

# Padding around the top and left edges
OFFSET = RADIUS * 1.8

# If to draw the heaxagonal lines
DOLINES = False

# Game clock
clock = pygame.time.Clock()

# Cells to be there at start
startCells = []

# Font for the fps counter
# Function becuase pygame needs to be initialized before calling font methods
def get_fps_font(size=32):
    return pygame.font.SysFont("verdana", size)
